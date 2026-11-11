"""
Winternitz One-Time Signature (WOTS) — educational reference
Much smaller signatures than pure Lamport (~2KB vs 8KB).
Security still reduces to hash pre-image resistance.
Includes checksum to prevent existential forgery.
v0.7 improvements: better docs, size helper, clearer digit logic.
"""

from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List, Tuple
from .utils import sha256

# w=16 → 4 bits per digit. 256-bit hash → 64 message digits + checksum.
W = 16
N_MSG_DIGITS = 64
N_CS_DIGITS = 3
N_CHAINS = N_MSG_DIGITS + N_CS_DIGITS  # 67


def _chain(start: bytes, steps: int) -> bytes:
    x = start
    for _ in range(steps):
        x = sha256(x)
    return x


@dataclass(frozen=True)
class WOTSPublicKey:
    chain_ends: Tuple[bytes, ...]

    def fingerprint(self) -> bytes:
        return sha256(b"".join(self.chain_ends))


@dataclass
class WOTSSecretKey:
    chain_starts: List[bytes]


@dataclass(frozen=True)
class WOTSSignature:
    revealed: Tuple[bytes, ...]

    def serialize(self) -> bytes:
        return b"".join(self.revealed)

    @property
    def size_bytes(self) -> int:
        return len(self.serialize())


class WOTSKeyPair:
    """Simple WOTS with fixed parameters and checksum."""

    def __init__(self, secret: WOTSSecretKey, public: WOTSPublicKey):
        self._secret = secret
        self._public = public
        self._used = False

    @classmethod
    def generate(cls) -> "WOTSKeyPair":
        starts = [os.urandom(32) for _ in range(N_CHAINS)]
        ends = tuple(_chain(s, W - 1) for s in starts)
        return cls(WOTSSecretKey(starts), WOTSPublicKey(ends))

    @property
    def public_key(self) -> WOTSPublicKey:
        return self._public

    def _base_w_digits(self, data: bytes) -> List[int]:
        """Split into base-w (w=16) digits. 64 from hash + 3 checksum digits."""
        h = sha256(data)
        digits = []
        for b in h:
            digits.append((b >> 4) & 0xF)
            digits.append(b & 0xF)
        # Checksum: sum of (W-1 - d) for message digits prevents forgery
        checksum = sum(W - 1 - d for d in digits[:N_MSG_DIGITS])
        cs_digits = []
        for _ in range(N_CS_DIGITS):
            cs_digits.append(checksum & 0xF)
            checksum >>= 4
        return digits[:N_MSG_DIGITS] + cs_digits

    def sign(self, message: bytes) -> WOTSSignature:
        if self._used:
            raise RuntimeError("WOTS key already used (one-time only)")
        self._used = True

        digits = self._base_w_digits(message)
        revealed = [_chain(self._secret.chain_starts[i], d) for i, d in enumerate(digits)]
        return WOTSSignature(tuple(revealed))

    def verify(self, message: bytes, signature: WOTSSignature) -> bool:
        if len(signature.revealed) != N_CHAINS:
            return False
        digits = self._base_w_digits(message)
        for i, d in enumerate(digits):
            end = _chain(signature.revealed[i], W - 1 - d)
            if end != self._public.chain_ends[i]:
                return False
        return True

    def fingerprint(self) -> bytes:
        return self._public.fingerprint()

    def estimated_sig_size(self) -> int:
        """Rough signature size in bytes (N_CHAINS * 32)."""
        return N_CHAINS * 32
