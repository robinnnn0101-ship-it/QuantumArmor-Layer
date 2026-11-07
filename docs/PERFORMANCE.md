# Performance Notes — QuantumArmor-Layer

Pure-Python educational implementation. Numbers approximate on modern laptop.

| Operation              | Approx time |
|------------------------|-------------|
| Lamport keygen         | 5-15 ms     |
| Merkle-16 keygen       | 80-200 ms   |
| WOTS keygen            | 10-30 ms    |
| Merkle sign (leaf)     | 1-5 ms      |
| Hybrid sign            | +ECDSA ~1ms |

Run `python examples/benchmark.py` for local numbers.

Bottlenecks:
- Many SHA-256 calls (especially Merkle keygen).
- Pure Python ecdsa + hashing.

Production would use Rust/C or optimized libs. This prioritizes auditability.
