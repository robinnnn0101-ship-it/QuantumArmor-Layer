#!/usr/bin/env python3
"""Core tests"""

from lamport import LamportKeyPair
from hybrid import HybridKeyManager

def test_lamport():
    kp = LamportKeyPair.generate()
    msg = b"test"
    sig = kp.sign(msg)
    assert kp.verify(msg, sig)
    print("✓ Lamport works")

def test_one_time():
    kp = LamportKeyPair.generate()
    kp.sign(b"first")
    try:
        kp.sign(b"second")
        assert False
    except RuntimeError:
        print("✓ One-time enforced")

def test_hybrid():
    mgr = HybridKeyManager.generate()
    msg = b"hybrid test"
    c = mgr.sign_classical(msg)
    q = mgr.sign_quantum(msg)
    assert mgr.verify_classical(msg, c)
    assert mgr.verify_quantum(msg, q)
    print("✓ Hybrid works")

if __name__ == "__main__":
    test_lamport()
    test_one_time()
    test_hybrid()
    print("\nAll tests passed.")
