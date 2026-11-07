# API Sketch — QuantumArmor-Layer

## HybridKeyManager

```python
from quantumarmor import HybridKeyManager

km = HybridKeyManager.generate(n_leaves=16)  # Merkle mode
# or HybridKeyManager.generate(use_wots=True)

pub = km.export_public()          # dict
commit = km.export_commitment()   # hex 32-byte

# Classical
sig_c = km.sign_classical(msg)
km.verify_classical(msg, sig_c)

# Quantum
sig_q = km.sign_quantum(msg, index=0)
km.verify_quantum(msg, sig_q)

# Hybrid (v0.6+)
hybrid = km.sign_hybrid(msg, index=0)
km.verify_hybrid(msg, hybrid)

print(km.remaining_quantum())
```

## CLI

```bash
quantumarmor generate --mode merkle --leaves 32 --out pub.json
quantumarmor sign --message "text" --hybrid --out sig.json
```

Educational reference — see source for full details.
