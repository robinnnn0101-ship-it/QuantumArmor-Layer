"""Status JSON export tests."""
from quantumarmor.hybrid import HybridKeyManager
import json


def test_export_status_json():
    km = HybridKeyManager.generate(n_leaves=4)
    s = km.export_status_json()
    data = json.loads(s)
    assert data["mode"] == "merkle"
    assert data["remaining"] == 4
    assert "commitment" in data
