"""QuantumArmor-Layer — hybrid quantum-proof cryptographic overlay for Bitcoin."""

from .lamport import LamportKeyPair, MerkleLamportKeyPair, LamportSignature
from .hybrid import HybridKeyManager, HybridPublicKey
from .utils import sha256, hash160, ripemd160

__all__ = [
    "LamportKeyPair",
    "MerkleLamportKeyPair",
    "LamportSignature",
    "HybridKeyManager",
    "HybridPublicKey",
    "sha256",
    "hash160",
    "ripemd160",
]

__version__ = "0.3.0"
