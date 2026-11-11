# Side-Channel Resistance Guidance — QuantumArmor v0.7

Educational notes only. This reference is not constant-time.

## Risks

- Timing attacks on hash chains or bit extraction.
- Cache-timing on table lookups (none here, but in ports).
- Power / EM if on hardware.

## Mitigations for real ports

- Use constant-time comparison and hashing (e.g. from cryptography libs).
- Avoid secret-dependent branches.
- Generate preimages with secure RNG.
- For WOTS chains, fixed steps or constant-time hash loops.
- Prefer SLH-DSA or ML-DSA for production multi-use.

## Demo safe

- Local only.
- Do not expose secrets.
- Track used keys strictly.

See SECURITY.md.
