"""Sign count tracker tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_sign_count_starts_zero():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.sign_count() == 0


def test_sign_count_increments():
    km = HybridKeyManager.generate(n_leaves=4)
    km.sign_quantum(b"one")
    assert km.sign_count() == 1
    km.sign_quantum(b"two")
    assert km.sign_count() == 2
    assert km.export_public()["sign_count"] == 2
