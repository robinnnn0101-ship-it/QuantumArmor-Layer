# SPHINCS-like Sketch Notes — QuantumArmor

Educational foundation only. Not a full implementation.

## Idea

SPHINCS+ uses hypertrees of WOTS + Merkle for many-time signatures under one public key.

## Current status

- We have WOTS + Merkle-Lamport (simpler)
- Full hypertree would allow 2^20+ signatures under one commitment
- Future v0.8 target

## Why not now

- Complexity vs educational clarity
- Larger signatures and keygen time
- Pure Python reference prefers simplicity

See NIST FIPS 205 for real SLH-DSA.
