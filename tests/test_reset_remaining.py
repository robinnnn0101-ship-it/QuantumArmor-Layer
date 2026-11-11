"""Ensure reset does not restore leaves."""
from quantumarmor.hybrid import HybridKeyManager


def test_reset_does_not_restore_leaves():
    km = HybridKeyManager.generate(n_leaves=2)
    assert km.remaining_quantum() == 2
    km.sign_quantum(b"msg")
    assert km.remaining_quantum() == 1
    km.reset_sign_count()
    assert km.remaining_quantum() == 1
    assert km.sign_count() == 0
