# QuantumArmor-Layer

### by Vexlore (@Vexlorebot)

**The first practical hybrid Quantum-Proof Layer for Bitcoin (BTC) that anyone can use today.**

No soft fork. No hard fork. No waiting for consensus.  
Just pure cryptographic armor you can apply to any UTXO right now.

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
2. **Quantum path** — pure hash-based Lamport one-time signatures (security rests *only* on SHA-256 pre-image resistance)
3. **Merkle multi-use** — many one-time keys under a single 32-byte root (practical)
4. **Commitment** — only a 32-byte fingerprint / Merkle root ever needs to appear on-chain
5. **Hybrid lock** — require both classical + quantum proof, or pure quantum

Anyone can generate keys, create protected commitments, sign, and verify using the reference implementation.

### Security Properties

- Resistant to Shor’s algorithm (no discrete-log attack possible on the quantum path)
- Security reduces purely to hash pre-image resistance
- One-time use per Lamport leaf (classic property)
- Merkle mode gives N signatures under one commitment
- Hybrid mode lets you keep classical efficiency until the threat becomes real
- Fully auditable pure-Python reference

### Project Structure

```
QuantumArmor-Layer/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── src/
│   └── quantumarmor/
│       ├── __init__.py
│       ├── lamport.py          # Lamport OTS + Merkle-Lamport
│       ├── hybrid.py           # Hybrid classical + quantum manager
│       ├── scripts.py          # Conceptual Bitcoin script templates
│       └── utils.py
├── examples/
│   ├── 01_generate_keys.py
│   ├── 02_sign_and_verify.py
│   └── 03_full_demo.py
├── docs/
│   └── DESIGN.md
├── tests/
│   └── test_core.py
└── X_POST_TEMPLATE.md
```

### Quick Start

```bash
pip install -e .
# or
pip install -r requirements.txt

# Run examples (from repo root after install)
python -m examples.01_generate_keys
python -m examples.02_sign_and_verify
python -m examples.03_full_demo

# Run tests
pytest tests/ -v
# or
python tests/test_core.py
```

### Status

- Educational + research-grade reference implementation
- Pure Python, minimal external crypto dependency (`ecdsa`)
- Designed so wallets, L2s, and custodians can integrate or harden it
- Not production-hardened (no constant-time guarantees, no side-channel protection)

### What’s new in v0.2

- Proper `src/` packaging
- **Merkle-Lamport** for multi-use under one 32-byte root
- Cleaner hybrid manager with modes (`ots` / `merkle`)
- Conceptual script templates
- Expanded tests + DESIGN.md
- Export helpers and remaining-signature counter

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
