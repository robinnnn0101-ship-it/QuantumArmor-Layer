"""Pretty public for WOTS."""
from quantumarmor.hybrid import HybridKeyManager
import json


def test_pretty_wots():
    km = HybridKeyManager.generate(use_wots=True)
    data = json.loads(km.pretty_public())
    assert data["mode"] == "wots"
    assert data["remaining"] == 1
