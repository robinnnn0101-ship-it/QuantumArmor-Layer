"""Tests for commitment helpers."""
from quantumarmor.hybrid import HybridKeyManager


def test_commitment_bytes_length():
    km = HybridKeyManager.generate(n_leaves=4)
    cb = km.commitment_bytes()
    assert len(cb) == 32
    assert cb == bytes.fromhex(km.export_commitment())


def test_export_includes_remaining():
    km = HybridKeyManager.generate(n_leaves=8)
    pub = km.export_public()
    assert "remaining" in pub
    assert pub["remaining"] == 8
    assert pub["version"] == "0.7.1"
