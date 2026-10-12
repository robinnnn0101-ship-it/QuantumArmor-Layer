"""
Hybrid Key Manager
Classical secp256k1 ECDSA + Post-Quantum Lamport
"""

from __future__ import annotations
from dataclasses import dataclass
import ecdsa
from ecdsa import SigningKey, SECP256k1
from lamport import LamportKeyPair, LamportSignature
from utils import sha256, hash160


@dataclass(frozen=True)
class HybridPublicKey:
    classical_pubkey: bytes
    lamport_fingerprint: bytes


class HybridKeyManager:
    def __init__(self, classical_sk: SigningKey, lamport: LamportKeyPair):
        self._classical_sk = classical_sk
        self._lamport = lamport
        vk = classical_sk.get_verifying_key()
        self._public = HybridPublicKey(
            classical_pubkey=vk.to_string("compressed"),
            lamport_fingerprint=lamport.fingerprint(),
        )

    @classmethod
    def generate(cls) -> "HybridKeyManager":
        sk = SigningKey.generate(curve=SECP256k1)
        lamport = LamportKeyPair.generate()
        return cls(sk, lamport)

    @property
    def public_key(self) -> HybridPublicKey:
        return self._public

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

    def sign_quantum(self, message: bytes) -> LamportSignature:
        return self._lamport.sign(message)

    def verify_quantum(self, message: bytes, signature: LamportSignature) -> bool:
        return self._lamport.verify(message, signature)

    def export_public(self) -> dict:
        return {
            "classical_pubkey_hex": self._public.classical_pubkey.hex(),
            "classical_hash160_hex": self.classical_hash160().hex(),
            "lamport_fingerprint_hex": self._public.lamport_fingerprint.hex(),
        }
