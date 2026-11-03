# Performance Notes

Educational numbers on a typical laptop (Python 3.11):

| Mode          | Keygen (approx) | Sign (approx) | Sig size |
|---------------|-----------------|---------------|----------|
| Lamport       | ~5 ms           | ~1 ms         | ~8 KB    |
| Merkle-16     | ~80 ms          | ~2 ms         | ~8 KB + proof |
| WOTS (w=4)    | ~20 ms          | ~5 ms         | ~2.5 KB  |

These are rough. Real numbers depend on hardware and Python version.

## Tips

- Prefer WOTS or Merkle for practical use.
- Pre-generate keys offline.
- Signature verification is cheap compared to generation.
- For production, port critical paths to Rust/C.

Run your own:

```python
import time
from quantumarmor import HybridKeyManager

t0 = time.perf_counter()
km = HybridKeyManager.generate(n_leaves=32)
print(f"keygen: {(time.perf_counter()-t0)*1000:.1f} ms")
```
