"""
Lamport One-Time Signature (Post-Quantum)
Security rests only on SHA-256 pre-image resistance.
Immune to Shor's algorithm.
"""

from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List, Tuple
from utils import sha256

N_BITS = 256
PREIMAGE_SIZE = 32


@dataclass(frozen=True)
class LamportPublicKey:
    hashes: Tuple[bytes, ...]

    def serialize(self) -> bytes:
        return b"".join(self.hashes)

    def fingerprint(self) -> bytes:
        return sha256(self.serialize())


@dataclass
class LamportSecretKey:
    preimages: List[bytes]


@dataclass(frozen=True)
class LamportSignature:
    revealed: Tuple[bytes, ...]

    def serialize(self) -> bytes:
        return b"".join(self.revealed)


class LamportKeyPair:
    def __init__(self, secret: LamportSecretKey, public: LamportPublicKey):
        self._secret = secret
        self._public = public
        self._used = False

    @classmethod
    def generate(cls) -> "LamportKeyPair":
        preimages = [os.urandom(PREIMAGE_SIZE) for _ in range(2 * N_BITS)]
        hashes = tuple(sha256(p) for p in preimages)
        return cls(LamportSecretKey(preimages), LamportPublicKey(hashes))

    @property
    def public_key(self) -> LamportPublicKey:
        return self._public

    def sign(self, message: bytes) -> LamportSignature:
        if self._used:
            raise RuntimeError("Lamport key already used (one-time only)")
        self._used = True

        msg_hash = sha256(message)
        bits = []
        for byte in msg_hash:
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)

        revealed = []
        for i, bit in enumerate(bits):
            idx = 2 * i + bit
            revealed.append(self._secret.preimages[idx])

        return LamportSignature(tuple(revealed))

    def verify(self, message: bytes, signature: LamportSignature) -> bool:
        if len(signature.revealed) != N_BITS:
            return False

        msg_hash = sha256(message)
        bits = []
        for byte in msg_hash:
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)

        for i, bit in enumerate(bits):
            idx = 2 * i + bit
            if sha256(signature.revealed[i]) != self._public.hashes[idx]:
                return False
        return True

    def fingerprint(self) -> bytes:
        return self._public.fingerprint()
