# Bitcoin Integration Sketches — QuantumArmor v0.7.1

Educational patterns only. Not production scripts.

## OP_RETURN commitment

```python
from quantumarmor import HybridKeyManager
from quantumarmor.utils import format_commitment

km = HybridKeyManager.generate(n_leaves=16)
raw = km.commitment_bytes()
print(format_commitment(raw))
# Embed in OP_RETURN
```

## Taproot leaf sketch

Commit the Merkle root or fingerprint inside a Taproot script path or annex.

- Pure quantum path: reveal Lamport/WOTS + Merkle proof in script
- Hybrid: require ECDSA + quantum proof

## Recommendations

- Use hybrid until quantum threat is immediate
- Rotate after remaining reaches low number
- Store secrets offline
- See examples/bitcoin_commit.py and taproot_sketch.py

**Armor the UTXO. Don't wait for consensus.**
