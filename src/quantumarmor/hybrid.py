"""
Hybrid Key Manager
Classical secp256k1 ECDSA + Post-Quantum Lamport / Merkle-Lamport / WOTS
v0.7 — next level hybrid sign, better exports, multi-use notes
"""

from __future__ import annotations
from dataclasses import dataclass
import ecdsa
from ecdsa import SigningKey, SECP256k1
from .lamport import LamportKeyPair, LamportSignature, MerkleLamportKeyPair
from .wots import WOTSKeyPair, WOTSSignature
from .utils import sha256, hash160


@dataclass(frozen=True)
class HybridPublicKey:
    classical_pubkey: bytes
    lamport_fingerprint: bytes
    merkle_root: bytes = b""


class HybridKeyManager:
    """Supports pure OTS, Merkle multi-use, or WOTS quantum path. v0.7 enhanced."""

    def __init__(
        self,
        classical_sk: SigningKey,
        lamport: LamportKeyPair | None = None,
        merkle: MerkleLamportKeyPair | None = None,
        wots: WOTSKeyPair | None = None,
    ):
        self._classical_sk = classical_sk
        self._lamport = lamport
        self._merkle = merkle
        self._wots = wots
        vk = classical_sk.get_verifying_key()
        root = merkle.root if merkle else b""
        if wots:
            fp = wots.fingerprint()
        elif lamport:
            fp = lamport.fingerprint()
        else:
            fp = merkle.root if merkle else b""
        self._public = HybridPublicKey(
            classical_pubkey=vk.to_string("compressed"),
            lamport_fingerprint=fp,
            merkle_root=root,
        )

    @classmethod
    def generate(cls, n_leaves: int = 1, use_wots: bool = False) -> "HybridKeyManager":
        sk = SigningKey.generate(curve=SECP256k1)
        if use_wots:
            return cls(sk, wots=WOTSKeyPair.generate())
        if n_leaves <= 1:
            return cls(sk, lamport=LamportKeyPair.generate())
        return cls(sk, merkle=MerkleLamportKeyPair.generate(n_leaves))

    @property
    def public_key(self) -> HybridPublicKey:
        return self._public

    @property
    def mode(self) -> str:
        if self._wots:
            return "wots"
        if self._merkle:
            return "merkle"
        return "lamport"

    def classical_hash160(self) -> bytes:
        return hash160(self._public.classical_pubkey)

    def sign_classical(self, message: bytes) -> bytes:
        return self._classical_sk.sign_digest(
            sha256(message),
            sigencode=ecdsa.util.sigencode_der,
        )

    def verify_classical(self, message: bytes, signature: bytes) -> bool:
        vk = self._classical_sk.get_verifying_key()
        try:
            return vk.verify_digest(
                signature,
                sha256(message),
                sigdecode=ecdsa.util.sigdecode_der,
            )
        except Exception:
            return False

    def sign_quantum(self, message: bytes, index: int | None = None):
        if self._wots:
            return self._wots.sign(message)
        if self._merkle:
            return self._merkle.sign(message, index)
        if self._lamport:
            return self._lamport.sign(message)
        raise RuntimeError("No quantum key available")

    def verify_quantum(self, message: bytes, signature) -> bool:
        if self._wots and isinstance(signature, WOTSSignature):
            return self._wots.verify(message, signature)
        if self._merkle:
            return self._merkle.verify(message, signature)
        if self._lamport and isinstance(signature, LamportSignature):
            return self._lamport.verify(message, signature)
        return False

    def sign_hybrid(self, message: bytes, index: int | None = None) -> dict:
        """Require both classical + quantum proofs (v0.7)."""
        return {
            "classical": self.sign_classical(message).hex(),
            "quantum": self.sign_quantum(message, index),
            "commitment": self.export_commitment(),
        }

    def verify_hybrid(self, message: bytes, hybrid_sig: dict) -> bool:
        try:
            c_ok = self.verify_classical(message, bytes.fromhex(hybrid_sig["classical"]))
            q_ok = self.verify_quantum(message, hybrid_sig["quantum"])
            return c_ok and q_ok
        except Exception:
            return False

    def remaining_quantum(self) -> int:
        if self._wots:
            return 0 if self._wots._used else 1
        if self._merkle:
            return self._merkle.remaining()
        if self._lamport and not self._lamport._used:
            return 1
        return 0

    def is_exhausted(self) -> bool:
        return self.remaining_quantum() == 0

    def export_public(self) -> dict:
        out = {
            "classical_pubkey_hex": self._public.classical_pubkey.hex(),
            "classical_hash160_hex": self.classical_hash160().hex(),
            "lamport_fingerprint_hex": self._public.lamport_fingerprint.hex(),
            "mode": self.mode,
            "version": "0.7.0",
        }
        if self._public.merkle_root:
            out["merkle_root_hex"] = self._public.merkle_root.hex()
        return out

    def export_commitment(self) -> str:
        """Return the 32-byte commitment hex suitable for OP_RETURN or Taproot."""
        if self._public.merkle_root:
            return self._public.merkle_root.hex()
        return self._public.lamport_fingerprint.hex()
