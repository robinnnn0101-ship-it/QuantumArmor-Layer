# API Sketch — QuantumArmor-Layer v0.7.1

## HybridKeyManager

```python
from quantumarmor import HybridKeyManager

print(HybridKeyManager.get_version())  # 0.7.1

km = HybridKeyManager.generate(n_leaves=16)
pub = km.export_public()          # includes remaining, version
commit = km.export_commitment()   # hex
raw = km.commitment_bytes()       # bytes

print(km.mode)
print(km.remaining_quantum())
print(km.is_exhausted())
```

## Utils

```python
from quantumarmor.utils import format_commitment
print(format_commitment(raw))
```

## CLI

```bash
quantumarmor generate --mode merkle --leaves 32
# prints commitment to stderr
```

Educational reference — see source for full details.
