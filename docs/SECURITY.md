# Security — QuantumArmor-Layer

## Threat model

- **Classical path**: standard ECDSA. Broken by Shor on quantum computer once public key revealed.
- **Quantum path**: hash pre-image resistance only (SHA-256). Grover reduces security ~sqrt, still practical with 256-bit.
- **Hybrid**: both required. Attacker needs to break ECDSA *and* pre-image (or forge OTS).

## Limitations (educational reference)

- Not constant-time (use timing-safe libs in production).
- No side-channel protection (cache, power, EM).
- Secret material handling is demo-level (do not store raw preimages in production; use HSMs).
- One-time keys: reuse = forge. Always track used leaves.
- Merkle path verification must be implemented carefully by integrators (check proof length, indices).
- No formal verification. Educational only.

## Side-channel notes (v0.7)

- Avoid branching on secret bits in real impls.
- Prefer constant-time hash libs if porting.
- Preimage generation with os.urandom is fine for demo; use CSPRNG properly.
- Do not log secrets.
- For high-value, prefer pure quantum mode with offline keygen.

## Recommendations

- Treat as research code.
- Store quantum secrets offline / air-gapped.
- Rotate commitments after N uses.
- Prefer hybrid mode for high-value until pure quantum wallets exist.
- Audit before any real Bitcoin.
- Consider SLH-DSA for multi-use in future versions.

See ARCHITECTURE.md and source comments.
