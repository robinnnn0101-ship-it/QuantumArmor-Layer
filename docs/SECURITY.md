# Security Model — QuantumArmor-Layer

## Threat Model

QuantumArmor protects Bitcoin UTXOs against future cryptographically relevant quantum computers (CRQCs) that can run Shor’s algorithm against secp256k1.

### What is protected
- Hash-based one-time signatures (Lamport / WOTS) are not vulnerable to Shor’s algorithm.
- Security reduces to pre-image resistance of SHA-256.
- Merkle roots allow multi-use under a single 32-byte commitment.

### What is NOT protected
- Classical ECDSA path remains vulnerable once a public key is revealed on-chain.
- No side-channel resistance (timing, cache, etc.).
- No constant-time implementation.
- Secret keys must never leave the device; this is a reference implementation.
- One-time keys: reuse = total break (classic Lamport property).

## Recommendations

1. Prefer Merkle or WOTS mode for any real commitment.
2. Keep classical key offline or use only for low-value / short-term UTXOs.
3. Treat the quantum signature as the ultimate unlock condition.
4. Audit any integration that touches key material.
5. Do not use for production funds without independent review and hardened implementation.

## Known Limitations

- Pure Python, not optimized.
- Educational quality.
- Signature sizes are large (especially pure Lamport).
- No formal verification.

**Armor up. Stay skeptical.**
