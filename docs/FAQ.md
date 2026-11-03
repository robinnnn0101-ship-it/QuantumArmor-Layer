# FAQ

**Is this production-ready?**  
No. Educational / research reference only.

**Does it require a Bitcoin soft fork?**  
No. Uses existing rules (OP_RETURN, scripts, Taproot leaves).

**How many signatures per commitment?**  
Merkle mode: N (you choose). WOTS/Lamport pure: 1.

**Signature size?**  
Lamport ~8 KB, WOTS ~2-3 KB, plus Merkle proof if used.

**Can I use it with existing wallets?**  
You can generate the commitment and track the quantum keys yourself. Full wallet integration is left as exercise.

**What if the quantum computer arrives tomorrow?**  
Move remaining value to a fresh QuantumArmor commitment before spending the classical key.

**License?**  
MIT.
