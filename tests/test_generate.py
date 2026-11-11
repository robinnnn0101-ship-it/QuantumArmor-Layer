"""Generate validation tests."""
import pytest
from quantumarmor.hybrid import HybridKeyManager


def test_generate_positive_leaves():
    km = HybridKeyManager.generate(n_leaves=1)
    assert km.mode == "lamport"


def test_generate_zero_fails():
    with pytest.raises(ValueError):
        HybridKeyManager.generate(n_leaves=0)


def test_generate_wots():
    km = HybridKeyManager.generate(use_wots=True)
    assert km.mode == "wots"
