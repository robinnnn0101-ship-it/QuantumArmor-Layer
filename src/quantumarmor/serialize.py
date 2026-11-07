"""Serialization helpers (educational, v0.6)."""

from __future__ import annotations
import json
from typing import Any, Dict


def to_json(obj: Any) -> str:
    """Best-effort JSON dump."""
    return json.dumps(obj, indent=2, default=str)


def commitment_bytes(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str)


def public_to_dict(pub: Any) -> Dict[str, Any]:
    """Normalize HybridPublicKey or export dict."""
    if hasattr(pub, "__dict__"):
        return {k: v.hex() if isinstance(v, bytes) else v for k, v in pub.__dict__.items()}
    return dict(pub)


def save_public(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
