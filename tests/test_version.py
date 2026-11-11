"""Version and error message tests."""
import pytest
from quantumarmor.hybrid import HybridKeyManager


def test_get_version():
    assert HybridKeyManager.get_version() == "0.7.1"
    km = HybridKeyManager.generate()
    assert km.export_public()["version"] == "0.7.1"


def test_exhausted_error_message():
    km = HybridKeyManager.generate(use_wots=True)
    km.sign_quantum(b"first")
    with pytest.raises(RuntimeError, match="exhausted"):
        km.sign_quantum(b"second")
