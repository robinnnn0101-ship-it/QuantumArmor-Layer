"""QuantumArmor-Layer — hybrid quantum-proof cryptographic overlay for Bitcoin."""

from .lamport import LamportKeyPair, MerkleLamportKeyPair, LamportSignature
from .wots import WOTSKeyPair, WOTSSignature
from .hybrid import HybridKeyManager, HybridPublicKey
from .utils import sha256, hash160, ripemd160

__all__ = [
    "LamportKeyPair",
    "MerkleLamportKeyPair",
    "LamportSignature",
    "WOTSKeyPair",
    "WOTSSignature",
    "HybridKeyManager",
    "HybridPublicKey",
    "sha256",
    "hash160",
    "ripemd160",
]

__version__ = "0.4.0"
