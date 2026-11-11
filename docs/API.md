# API Sketch — QuantumArmor-Layer v0.7.1

## HybridKeyManager

```python
from quantumarmor import HybridKeyManager

print(HybridKeyManager.get_version())  # 0.7.1

km = HybridKeyManager.generate(n_leaves=16)
pub = km.export_public()          # includes remaining, remaining_percent, used_estimate, version, sign_count, leaf_count
print(km.pretty_public())         # indented JSON
print(km.get_status())            # compact status dict
print(km.export_status_json())    # pretty status JSON
commit = km.export_commitment()   # hex
raw = km.commitment_bytes()       # bytes

print(km.mode)
print(km.leaf_count)
print(km.used_leaves_estimate())
print(km.remaining_percent())
print(km.is_hybrid_capable())
print(km.remaining_quantum())
print(km.sign_count())
km.reset_sign_count()             # educational only
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
# prints commitment, remaining, and status to stderr
```

Educational reference — see source for full details.
