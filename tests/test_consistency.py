"""Consistency tests."""
from quantumarmor.hybrid import HybridKeyManager
from quantumarmor.utils import format_commitment


def test_commitment_consistency():
    km = HybridKeyManager.generate(n_leaves=8)
    raw = km.commitment_bytes()
    assert format_commitment(raw) == km.export_commitment()
    pub = km.export_public()
    assert "merkle_root_hex" in pub or "lamport_fingerprint_hex" in pub
