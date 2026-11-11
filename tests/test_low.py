"""Low remaining tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_low_remaining():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.is_low_remaining() is False
    km.sign_quantum(b"1")
    km.sign_quantum(b"2")
    km.sign_quantum(b"3")
    assert km.is_low_remaining() is True
    assert km.export_public()["low_remaining"] is True
