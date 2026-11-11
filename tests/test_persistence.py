"""Tests for educational persistence sketches."""
from quantumarmor.hybrid import HybridKeyManager
from quantumarmor.persistence import sketch_export_public_only, sketch_load_public, warning
import tempfile
import os


def test_warning_exists():
    assert "WARNING" in warning()
    assert "educational" in warning().lower()


def test_public_export_load():
    km = HybridKeyManager.generate(n_leaves=2)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as f:
        path = f.name
    try:
        sketch_export_public_only(km, path)
        loaded = sketch_load_public(path)
        assert "public" in loaded
        assert loaded["version"] == "0.7.0"
        assert "commitment" in loaded
    finally:
        os.unlink(path)
