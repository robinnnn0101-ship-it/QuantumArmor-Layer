"""
Educational key persistence sketches for QuantumArmor v0.7.
NOT for production — secrets must stay offline / air-gapped.
Shows patterns only.
"""

from __future__ import annotations
import json
from typing import Dict, Any
from .hybrid import HybridKeyManager


def sketch_export_public_only(km: HybridKeyManager, path: str) -> None:
    """Export only public commitment info (safe)."""
    data = {
        "version": "0.7.0",
        "public": km.export_public(),
        "commitment": km.export_commitment(),
        "note": "Public only. Never store secrets this way in real use."
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def sketch_load_public(path: str) -> Dict[str, Any]:
    """Load public info sketch."""
    with open(path) as f:
        return json.load(f)


def warning() -> str:
    return (
        "WARNING: This is educational only. "
        "Do not persist raw secret preimages or private keys on disk in production. "
        "Use HSMs, air-gapped devices, or proper key management."
    )
