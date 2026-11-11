"""Hybrid capable tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_is_hybrid_capable():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.is_hybrid_capable() is True
    st = km.get_status()
    assert st["hybrid_capable"] is True
