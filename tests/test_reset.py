"""Reset sign count tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_reset_sign_count():
    km = HybridKeyManager.generate(n_leaves=4)
    km.sign_quantum(b"msg")
    assert km.sign_count() == 1
    km.reset_sign_count()
    assert km.sign_count() == 0
    assert km.export_public()["sign_count"] == 0
