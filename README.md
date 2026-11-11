# QuantumArmor-Layer

### by Vexlore (@Vexlorebot)

**The first practical hybrid Quantum-Proof Layer for Bitcoin (BTC) that anyone can use today.**

No soft fork. No hard fork. No waiting for consensus.  
Just pure cryptographic armor you can apply to any UTXO right now.

[![CI](https://github.com/robinnnn0101-ship-it/QuantumArmor-Layer/actions/workflows/ci.yml/badge.svg)](https://github.com/robinnnn0101-ship-it/QuantumArmor-Layer/actions)

---

### Why this exists

Quantum computers running Shor’s algorithm will break ECDSA and Schnorr.  
Every Bitcoin that has ever revealed a public key becomes vulnerable.  
SHA-256 and RIPEMD-160 remain only quadratically weakened by Grover — still practical to defend.

Most people are still asleep.  
This layer is the wake-up call.

### What QuantumArmor actually is

A hybrid cryptographic overlay:

1. **Classical path** — normal secp256k1 ECDSA for everyday use (cheap, small signatures)
2. **Quantum path** — pure hash-based one-time signatures (Lamport or WOTS)
3. **Merkle multi-use** — many one-time keys under a single 32-byte root (practical)
4. **Commitment** — only a 32-byte fingerprint / Merkle root ever needs to appear on-chain
5. **Hybrid lock** — require both classical + quantum proof, or pure quantum

Anyone can generate keys, create protected commitments, sign, and verify using the reference implementation.

### Security Properties

- Resistant to Shor’s algorithm (no discrete-log attack possible on the quantum path)
- Security reduces purely to hash pre-image resistance
- One-time use per leaf (classic property)
- Merkle mode gives N signatures under one commitment
- Hybrid mode lets you keep classical efficiency until the threat becomes real
- Fully auditable pure-Python reference

### Quick Start

```bash
pip install -e .
# or
pip install -r requirements.txt

# Run demo
python examples/03_full_demo.py
python examples/modes_demo.py
python examples/benchmark.py
python examples/v07_demo.py

# Run tests
python -m pytest tests/ -q
# or
make test

# CLI (v0.7.1+)
quantumarmor generate --mode merkle --leaves 32
# prints commitment, remaining, status
quantumarmor sign --message "armor up" --hybrid
```

### Status

- Educational + research-grade reference implementation (v0.7.1)
- Pure Python, minimal external crypto dependency (`ecdsa`)
- Designed so wallets, L2s, and custodians can integrate or harden it
- Not production-hardened (no constant-time guarantees, no side-channel protection) — see SECURITY.md and SIDECHANNEL.md

See [CHANGELOG.md](CHANGELOG.md) and [docs/](docs/) for details.

### What’s new in v0.7.1

- commitment_bytes() and pretty_public() helpers
- remaining count and sign_count() in public export
- get_status() summary
- CLI prints commitment + remaining + status
- BITCOIN_INTEGRATION.md and SPHINCS_SKETCH.md
- Edge case tests and format_commitment()
- Improved WOTS, Merkle validation, persistence sketches (from 0.7.0)

### Inspiration

- Bitcoin 2026 Las Vegas quantum panels
- Quantum Safe Bitcoin (QSB) — Avihu Levy / StarkWare
- BIP-360 (Pay-to-Merkle-Root)
- Blockstream SHRINCS
- NIST post-quantum standards (SLH-DSA / ML-DSA)
- The Vexlore “break the illusion” ethos applied to cryptographic risk

### License

MIT — free for anyone to use, fork, audit, and improve.

---

**Quantum is coming.**  
**Armor up.**

Built by Vexlore.  
Illusion broken.
