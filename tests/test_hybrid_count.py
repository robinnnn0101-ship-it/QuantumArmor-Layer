"""Hybrid sign count."""
from quantumarmor.hybrid import HybridKeyManager


def test_hybrid_increments_count():
    km = HybridKeyManager.generate(n_leaves=4)
    km.sign_hybrid(b"msg")
    assert km.sign_count() == 1
    assert km.export_public()["sign_count"] == 1
