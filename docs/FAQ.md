# FAQ — QuantumArmor-Layer

**Is this production ready?**  
No. Educational / research reference. No constant-time, no side-channel hardening.

**Does it require a Bitcoin soft fork?**  
No. Commitment is just 32 bytes (OP_RETURN or script leaf).

**How many signatures per commitment?**  
Merkle mode: N (you choose leaves). Pure Lamport/WOTS: 1.

**What is hybrid mode?**  
Requires both ECDSA + quantum OTS proof. Useful for high-value until pure quantum is practical.

**Signature sizes?**  
- ECDSA: ~70 B  
- Lamport: ~8 KB  
- WOTS: ~2-3 KB  
- Merkle: only 32 B on-chain + path + leaf sig off-chain

**Can I use this with existing wallets?**  
Classical path is standard secp256k1. Quantum path is additional commitment + reveal when needed. See INTEGRATION.md.

**v0.6 new?**  
Full CLI, hybrid sign/verify, benchmarks, Docker, more docs.

More in docs/ and source.
