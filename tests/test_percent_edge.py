"""Percent edge cases."""
from quantumarmor.hybrid import HybridKeyManager


def test_percent_single():
    km = HybridKeyManager.generate(use_wots=True)
    assert km.remaining_percent() == 100.0
    km.sign_quantum(b"msg")
    assert km.remaining_percent() == 0.0
