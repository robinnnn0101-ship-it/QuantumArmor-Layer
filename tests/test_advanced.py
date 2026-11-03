"""Advanced tests for Merkle multi-use and WOTS."""

import pytest
from quantumarmor.hybrid import HybridKeyManager
from quantumarmor.lamport import MerkleLamportKeyPair
from quantumarmor.wots import WOTSKeyPair


def test_merkle_multi_sign():
    km = HybridKeyManager.generate(n_leaves=4)
    assert km.remaining_quantum() == 4
    msg1 = b"first"
    msg2 = b"second"
    sig1 = km.sign_quantum(msg1)
    assert km.verify_quantum(msg1, sig1)
    assert km.remaining_quantum() == 3
    sig2 = km.sign_quantum(msg2)
    assert km.verify_quantum(msg2, sig2)
    assert not km.verify_quantum(msg1, sig2)


def test_wots_roundtrip():
    km = HybridKeyManager.generate(use_wots=True)
    msg = b"wots-test"
    sig = km.sign_quantum(msg)
    assert km.verify_quantum(msg, sig)
    assert km.remaining_quantum() == 0
    with pytest.raises(Exception):
        km.sign_quantum(b"again")


def test_classical_still_works():
    km = HybridKeyManager.generate()
    msg = b"classical"
    sig = km.sign_classical(msg)
    assert km.verify_classical(msg, sig)
    assert not km.verify_classical(b"tampered", sig)


def test_merkle_root_stable():
    m = MerkleLamportKeyPair.generate(8)
    root1 = m.root
    # re-generate should differ
    m2 = MerkleLamportKeyPair.generate(8)
    assert root1 != m2.root
    assert len(root1) == 32
