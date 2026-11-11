"""Leaf count tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_leaf_count_merkle():
    km = HybridKeyManager.generate(n_leaves=8)
    assert km.leaf_count == 8
    assert km.export_public()["leaf_count"] == 8
    assert km.get_status()["leaf_count"] == 8


def test_leaf_count_wots():
    km = HybridKeyManager.generate(use_wots=True)
    assert km.leaf_count == 1
