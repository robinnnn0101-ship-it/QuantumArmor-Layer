"""
Lamport One-Time Signature + Merkle multi-use
Security rests only on SHA-256 pre-image resistance.
Immune to Shor's algorithm.
"""

from __future__ import annotations
import os
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict
from .utils import sha256


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


# ── Merkle-Lamport (multi-use under one root) ───────────────────────────────

def _merkle_parent(left: bytes, right: bytes) -> bytes:
    return sha256(left + right)


def build_merkle_tree(leaves: List[bytes]) -> List[List[bytes]]:
    if not leaves:
        return []
    levels = [list(leaves)]
    while len(levels[-1]) > 1:
        current = levels[-1]
        next_level = []
        for i in range(0, len(current), 2):
            left = current[i]
            right = current[i + 1] if i + 1 < len(current) else left
            next_level.append(_merkle_parent(left, right))
        levels.append(next_level)
    return levels


def merkle_proof(levels: List[List[bytes]], index: int) -> List[Tuple[bytes, bool]]:
    """Return list of (sibling, is_right) from leaf to root."""
    proof = []
    idx = index
    for level in levels[:-1]:
        sibling_idx = idx ^ 1
        is_right = sibling_idx > idx
        if sibling_idx < len(level):
            sibling = level[sibling_idx]
        else:
            sibling = level[idx]
        proof.append((sibling, is_right))
        idx //= 2
    return proof


def verify_merkle_proof(leaf: bytes, proof: List[Tuple[bytes, bool]], root: bytes) -> bool:
    current = leaf
    for sibling, is_right in proof:
        if is_right:
            current = _merkle_parent(current, sibling)
        else:
            current = _merkle_parent(sibling, current)
    return current == root


@dataclass
class MerkleLamportKeyPair:
    """N one-time Lamport keys under a single 32-byte Merkle root."""
    n_leaves: int
    keys: List[LamportKeyPair] = field(default_factory=list)
    levels: List[List[bytes]] = field(default_factory=list)
    used: List[bool] = field(default_factory=list)

    @classmethod
    def generate(cls, n_leaves: int = 16) -> "MerkleLamportKeyPair":
        keys = [LamportKeyPair.generate() for _ in range(n_leaves)]
        leaves = [k.fingerprint() for k in keys]
        levels = build_merkle_tree(leaves)
        return cls(
            n_leaves=n_leaves,
            keys=keys,
            levels=levels,
            used=[False] * n_leaves,
        )

    @property
    def root(self) -> bytes:
        return self.levels[-1][0] if self.levels else b"\x00" * 32

    def remaining(self) -> int:
        return sum(1 for u in self.used if not u)

    def sign(self, message: bytes, index: Optional[int] = None) -> Dict:
        if index is None:
            try:
                index = self.used.index(False)
            except ValueError:
                raise RuntimeError("All Merkle-Lamport leaves exhausted")
        if self.used[index]:
            raise RuntimeError(f"Leaf {index} already used")
        self.used[index] = True

        leaf_fp = self.keys[index].fingerprint()
        lamport_sig = self.keys[index].sign(message)
        proof = merkle_proof(self.levels, index)

        return {
            "index": index,
            "lamport_sig": lamport_sig,
            "proof": proof,
            "leaf_fingerprint": leaf_fp,
        }

    def verify(self, message: bytes, sig_bundle: Dict, root: Optional[bytes] = None) -> bool:
        root = root or self.root
        proof = sig_bundle["proof"]
        leaf_fp = sig_bundle["leaf_fingerprint"]
        if not verify_merkle_proof(leaf_fp, proof, root):
            return False
        idx = sig_bundle["index"]
        if idx < len(self.keys):
            return self.keys[idx].verify(message, sig_bundle["lamport_sig"])
        return True

    def export_public(self) -> dict:
        return {
            "root_hex": self.root.hex(),
            "n_leaves": self.n_leaves,
            "remaining": self.remaining(),
        }
