"""Status helper tests."""
from quantumarmor.hybrid import HybridKeyManager


def test_get_status():
    km = HybridKeyManager.generate(n_leaves=4)
    st = km.get_status()
    assert st["mode"] == "merkle"
    assert st["remaining"] == 4
    assert st["sign_count"] == 0
    assert st["exhausted"] is False
    assert "commitment" in st
    assert st["version"] == "0.7.1"
