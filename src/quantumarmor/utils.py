"""
Cryptographic helpers
v0.7.1+: hex and commitment formatting
"""

import hashlib
from typing import Union


def sha256(data: Union[bytes, str]) -> bytes:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).digest()


def ripemd160(data: bytes) -> bytes:
    h = hashlib.new("ripemd160")
    h.update(data)
    return h.digest()


def hash160(data: bytes) -> bytes:
    return ripemd160(sha256(data))


def sha256d(data: bytes) -> bytes:
    return sha256(sha256(data))


def to_hex(data: bytes) -> str:
    return data.hex()


def from_hex(h: str) -> bytes:
    return bytes.fromhex(h)


def format_commitment(commit: bytes) -> str:
    """Pretty hex for 32-byte commitment."""
    if len(commit) != 32:
        raise ValueError("Commitment must be 32 bytes")
    return commit.hex()


def constant_time_note() -> str:
    return "Educational: comparisons and hashing are not constant-time. See SIDECHANNEL.md."
