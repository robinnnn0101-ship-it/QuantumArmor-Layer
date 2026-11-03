"""Minimal serialization helpers (educational)."""

from __future__ import annotations
import json
from typing import Any


def to_json(obj: Any) -> str:
    """Best-effort JSON dump for public info."""
    return json.dumps(obj, indent=2, default=str)


def commitment_bytes(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str)
