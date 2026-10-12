# QuantumArmor-Layer
**Hybrid Quantum-Proof Layer for Bitcoin**  
by Vexlore

A practical post-quantum protection layer anyone can use today.  
No soft fork required.

### What this is
- Classical ECDSA (secp256k1) + Post-Quantum Lamport signatures
- Hybrid key generation
- Only a 32-byte fingerprint needs to be committed on-chain
- Fully auditable pure Python

### Files
| File | Purpose |
|------|---------|
| `lamport.py` | Post-quantum one-time signatures (core tech) |
| `hybrid.py` | Hybrid classical + quantum key manager |
| `utils.py` | Hashing helpers |
| `generate_keys.py` | Generate hybrid keys |
| `sign_and_verify.py` | Sign and verify demo |
| `full_demo.py` | Full working demonstration |
| `test_core.py` | Tests |

### How to run
```bash
pip install ecdsa
python generate_keys.py
python sign_and_verify.py
python full_demo.py
python test_core.py
```

### License
MIT
