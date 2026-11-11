# Performance Notes — QuantumArmor-Layer v0.7.1

Pure-Python educational implementation. Numbers approximate on modern laptop.

| Operation              | Approx time | Notes |
|------------------------|-------------|-------|
| Lamport keygen         | 5-15 ms     | 512 SHA-256 |
| Merkle-16 keygen       | 80-200 ms   | Dominated by keygens |
| WOTS keygen            | 10-30 ms    | 67 chains × 15 hashes |
| Merkle sign (leaf)     | 1-5 ms      | + proof ~log N |
| Hybrid sign            | +ECDSA ~1ms | |
| WOTS signature size    | ~2144 bytes | 67 × 32 |
| commitment_bytes()     | <1 µs       | hex decode |

Run `python examples/benchmark.py` or `examples/v07_demo.py` for local numbers.

Bottlenecks:
- Many SHA-256 calls (especially Merkle keygen).
- Pure Python ecdsa + hashing.

Production would use Rust/C or optimized libs (or SLH-DSA). This prioritizes auditability.

Use `format_commitment` and `commitment_bytes` for clean 32-byte handling.
