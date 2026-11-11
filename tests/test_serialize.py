"""Tests for serialization and utils helpers."""
from quantumarmor.utils import to_hex, from_hex, sha256
from quantumarmor.serialize import commitment_bytes, load_public, save_public
import tempfile
import os


def test_hex_roundtrip():
    data = sha256(b"test")
    h = to_hex(data)
    assert from_hex(h) == data
    assert commitment_bytes(h) == data


def test_public_save_load():
    data = {"root": "aa" * 32, "version": "0.7.0"}
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
        path = f.name
    try:
        save_public(path, data)
        loaded = load_public(path)
        assert loaded == data
    finally:
        os.unlink(path)
