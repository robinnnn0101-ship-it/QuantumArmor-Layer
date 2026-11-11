"""Edge case tests."""
import pytest
from quantumarmor.hybrid import HybridKeyManager
from quantumarmor.wots import WOTSKeyPair


def test_wots_double_sign_fails():
    kp = WOTSKeyPair.generate()
    kp.sign(b"once")
    with pytest.raises(RuntimeError):
        kp.sign(b"twice")


def test_hybrid_exhausted_wots():
    km = HybridKeyManager.generate(use_wots=True)
    km.sign_quantum(b"msg")
    assert km.is_exhausted()
    with pytest.raises(RuntimeError):
        km.sign_quantum(b"again")


def test_bad_verify_returns_false():
    km = HybridKeyManager.generate(n_leaves=2)
    assert not km.verify_quantum(b"msg", None)
    assert not km.verify_hybrid(b"msg", {})
