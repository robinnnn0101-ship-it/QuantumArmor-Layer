"""Needs rotation tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_needs_rotation():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.needs_rotation() is False
    for i in range(3):
        km.sign_quantum(f"m{i}".encode())
    assert km.needs_rotation() is True
    assert km.export_public()["needs_rotation"] is True
