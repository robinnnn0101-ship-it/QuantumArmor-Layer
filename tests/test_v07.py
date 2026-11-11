"""Tests for v0.7 improvements."""
import pytest
from quantumarmor.wots import WOTSKeyPair
from quantumarmor.lamport import MerkleLamportKeyPair
from quantumarmor.hybrid import HybridKeyManager


def test_wots_size_helper():
    kp = WOTSKeyPair.generate()
    assert kp.estimated_sig_size() == 67 * 32
    sig = kp.sign(b"test")
    assert sig.size_bytes == 67 * 32


def test_merkle_invalid_index():
    m = MerkleLamportKeyPair.generate(4)
    with pytest.raises(ValueError):
        m.sign(b"msg", index=10)
    with pytest.raises(ValueError):
        m.sign(b"msg", index=-1)


def test_hybrid_v07_version():
    km = HybridKeyManager.generate(n_leaves=4)
    pub = km.export_public()
    assert pub["version"] == "0.7.0"
    assert "merkle" in pub["mode"]
