# Bitcoin Integration Sketches — QuantumArmor v0.7+

Educational patterns only. Not production scripts.

## OP_RETURN commitment

```python
from quantumarmor import HybridKeyManager
km = HybridKeyManager.generate(n_leaves=16)
commit = km.commitment_bytes()  # 32 bytes
# Embed commit in OP_RETURN <commit>
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
