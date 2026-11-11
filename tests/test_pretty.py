"""Pretty print tests."""
from quantumarmor.hybrid import HybridKeyManager
import json


def test_pretty_public():
    km = HybridKeyManager.generate(n_leaves=4)
    s = km.pretty_public()
    data = json.loads(s)
    assert data["mode"] == "merkle"
    assert "remaining" in data
    assert data["version"] == "0.7.1"
