# Comparison — QuantumArmor vs Other Post-Quantum Approaches

| Scheme          | Type          | Sig Size     | Multi-use | On-chain fit | Status here |
|-----------------|---------------|--------------|-----------|--------------|-------------|
| ECDSA/Schnorr   | Classical     | ~70 B        | Yes       | Native       | Classical path |
| Lamport         | Hash OTS      | ~8 KB        | No        | Via commit   | Implemented |
| WOTS            | Hash OTS      | ~2-3 KB      | No        | Via commit   | Implemented |
| Merkle-Lamport  | Hash + Merkle | root 32 B    | N times   | Excellent    | Implemented |
| SPHINCS+        | Hash stateless| ~8-40 KB     | Yes       | Hard (size)  | Planned sketch |
| ML-DSA (Dilithium) | Lattice   | ~2-4 KB      | Yes       | Possible     | Optional future |
| SLH-DSA         | Hash stateless| large        | Yes       | Difficult    | Optional future |

**Why this design?**
- Usable *today* on Bitcoin without soft fork.
- Pure hash security (pre-image) — no lattice assumptions.
- Tiny on-chain footprint (32-byte root).
- Educational pure-Python for audit.

Hybrid lets you keep cheap ECDSA until quantum threat is real, then switch or require both.
