"""Remaining percent tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_remaining_percent():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.remaining_percent() == 100.0
    km.sign_quantum(b"msg")
    assert km.remaining_percent() == 75.0
    assert km.export_public()["remaining_percent"] == 75.0
