"""Utils helper tests."""
import pytest
from quantumarmor.utils import format_commitment, sha256


def test_format_commitment_ok():
    c = sha256(b"commit")
    assert format_commitment(c) == c.hex()
    assert len(format_commitment(c)) == 64


def test_format_commitment_bad_length():
    with pytest.raises(ValueError):
        format_commitment(b"short")
