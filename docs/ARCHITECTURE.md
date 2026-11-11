# Architecture — QuantumArmor-Layer

Hybrid design:

1. Classical secp256k1 ECDSA for everyday efficiency
2. Quantum path: Lamport or WOTS (hash-based, Shor-resistant)
3. Merkle multi-use under one 32-byte root
4. Commitment: only fingerprint/root on-chain
5. Hybrid mode: both proofs required

v0.7.1 helpers:
- pretty_public() for readable export
- commitment_bytes() for raw 32-byte
- remaining tracking
- sign_count() tracker
- reset_sign_count() (educational, does not restore leaves)
- get_status() compact summary
- is_hybrid_capable() always true
- export_status_json()
- leaf_count property (1 for OTS, N for Merkle)
- used_leaves_estimate() = leaf_count - remaining

See source for full flow.
