#!/usr/bin/env python3
"""Core tests for QuantumArmor v0.4"""

from quantumarmor import HybridKeyManager, LamportKeyPair, MerkleLamportKeyPair, WOTSKeyPair


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


def test_merkle():
    ml = MerkleLamportKeyPair.generate(8)
    assert ml.remaining() == 8
    msg = b"merkle-test"
    bundle = ml.sign(msg)
    assert ml.remaining() == 7
    print(f"✓ Merkle signed leaf {bundle['index']}, remaining {ml.remaining()}")


def test_hybrid_merkle():
    mgr = HybridKeyManager.generate(n_leaves=4)
    assert mgr.remaining_quantum() == 4
    msg = b"hybrid-merkle"
    c = mgr.sign_classical(msg)
    q = mgr.sign_quantum(msg)
    assert mgr.verify_classical(msg, c)
    assert mgr.remaining_quantum() == 3
    print("✓ Hybrid + Merkle works")


def test_wots():
    kp = WOTSKeyPair.generate()
    msg = b"wots-test"
    sig = kp.sign(msg)
    assert kp.verify(msg, sig)
    print(f"✓ WOTS works (sig size {len(sig.serialize())}B)")


def test_hybrid_wots():
    mgr = HybridKeyManager.generate(use_wots=True)
    assert mgr.remaining_quantum() == 1
    msg = b"hybrid-wots"
    q = mgr.sign_quantum(msg)
    assert mgr.verify_quantum(msg, q)
    assert mgr.remaining_quantum() == 0
    print("✓ Hybrid + WOTS works")


if __name__ == "__main__":
    test_lamport()
    test_one_time()
    test_merkle()
    test_hybrid_merkle()
    test_wots()
    test_hybrid_wots()
    print("\nAll tests passed.")
