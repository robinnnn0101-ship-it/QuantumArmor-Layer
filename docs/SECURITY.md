# Security — QuantumArmor-Layer

## Threat model

- **Classical path**: standard ECDSA. Broken by Shor on quantum computer once public key revealed.
- **Quantum path**: hash pre-image resistance only (SHA-256). Grover reduces security ~sqrt, still practical with 256-bit.
- **Hybrid**: both required. Attacker needs to break ECDSA *and* pre-image (or forge OTS).

## Limitations (educational reference)

- Not constant-time.
- No side-channel protection.
- Secret material handling is demo-level (do not store raw preimages in production).
- One-time keys: reuse = forge.
- Merkle path verification must be implemented carefully by integrators.
- No formal verification.

## Recommendations

- Treat as research code.
- Store quantum secrets offline / air-gapped.
- Rotate commitments after N uses.
- Prefer hybrid mode for high-value until pure quantum wallets exist.
- Audit before any real Bitcoin.

See ARCHITECTURE.md and source comments.
