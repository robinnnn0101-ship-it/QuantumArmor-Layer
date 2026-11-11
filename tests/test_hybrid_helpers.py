"""Tests for HybridKeyManager helpers."""
from quantumarmor.hybrid import HybridKeyManager


def test_mode_merkle():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.mode == "merkle"
    assert not km.is_exhausted()


def test_mode_wots():
    km = HybridKeyManager.generate(use_wots=True)
    assert km.mode == "wots"
    assert km.remaining_quantum() == 1
    km.sign_quantum(b"x")
    assert km.is_exhausted()


def test_mode_lamport():
    km = HybridKeyManager.generate(n_leaves=1)
    assert km.mode == "lamport"
