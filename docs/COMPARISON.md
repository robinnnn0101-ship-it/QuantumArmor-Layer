# Comparison Notes

Educational sketches only.

| Scheme | Sig size | Multi-use | Notes |
|--------|----------|-----------|-------|
| Lamport | ~8KB | 1 | Simple, large |
| WOTS | ~2KB | 1 | Smaller, checksum |
| Merkle-Lamport | ~8KB + proof | N | Practical multi |
| SLH-DSA | variable | many | NIST, heavier |
| ML-DSA | ~2-4KB | many | Lattice, different assumptions |

v0.7: WOTS estimated_sig_size() helper for exact comparison.

Hybrid keeps classical ECDSA for everyday until quantum threat is real.
