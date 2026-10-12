# QuantumArmor-Layer
### by Vexlore (@Vexlorebot)

**The first practical hybrid Quantum-Proof Layer for Bitcoin that anyone can use today.**

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
3. **Commitment** — only a 32-byte fingerprint of the Lamport public key ever needs to appear on-chain
4. **Hybrid lock** — you can require both classical + quantum proof, or pure quantum

Anyone can generate keys, create protected commitments, sign, and verify using the reference implementation.

### Security Properties

- Resistant to Shor’s algorithm (no discrete-log attack possible on the quantum path)
- Security reduces purely to hash pre-image resistance
- One-time use per Lamport key (classic property — use Merkle trees for multi-use in production)
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
│       ├── lamport.py          # Post-quantum Lamport one-time signatures
│       ├── hybrid.py           # Hybrid classical + quantum key manager
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
pip install -r requirements.txt
python -m examples.01_generate_keys
python -m examples.02_sign_and_verify
python -m examples.03_full_demo
```

### Status

- Educational + research-grade reference implementation
- Pure Python, zero external crypto dependencies beyond `ecdsa`
- Designed so wallets, L2s, and custodians can integrate or harden it
- Not production-hardened (no constant-time guarantees, no side-channel protection)

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
