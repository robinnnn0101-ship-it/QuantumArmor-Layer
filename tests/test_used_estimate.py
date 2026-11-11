"""Used leaves estimate tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_used_estimate():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.used_leaves_estimate() == 0
    km.sign_quantum(b"msg")
    assert km.used_leaves_estimate() == 1
    assert km.export_public()["used_estimate"] == 1
    assert km.get_status()["used_estimate"] == 1
