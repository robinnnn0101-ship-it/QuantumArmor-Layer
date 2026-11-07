"""Tests for hybrid signing (v0.6)."""

import pytest
from quantumarmor import HybridKeyManager


def test_hybrid_sign_verify():
    km = HybridKeyManager.generate(4)
    msg = b"hybrid armor test"
    sig = km.sign_hybrid(msg, index=0)
    assert km.verify_hybrid(msg, sig)
    assert not km.verify_hybrid(b"wrong", sig)


def test_remaining_after_hybrid():
    km = HybridKeyManager.generate(2)
    start = km.remaining_quantum()
    km.sign_hybrid(b"use one", 0)
    assert km.remaining_quantum() == start - 1
