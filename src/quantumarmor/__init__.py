"""QuantumArmor-Layer — Hybrid Quantum-Proof Layer for Bitcoin"""

__version__ = "0.5.0"

from .hybrid import HybridKeyManager, HybridPublicKey
from .lamport import LamportKeyPair, MerkleLamportKeyPair
from .wots import WOTSKeyPair

__all__ = [
    "HybridKeyManager",
    "HybridPublicKey",
    "LamportKeyPair",
    "MerkleLamportKeyPair",
    "WOTSKeyPair",
    "__version__",
]
