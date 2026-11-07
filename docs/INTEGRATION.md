# Integration Guide — Using QuantumArmor with Bitcoin

## Commitment patterns (no fork)

### 1. OP_RETURN
Simplest. Embed the 32-byte Merkle root or fingerprint.

```python
commitment = km.export_commitment()  # hex
# Build OP_RETURN output with commitment
```

See `examples/bitcoin_commit.py`.

### 2. Taproot leaf
Embed the root in a script path leaf. Spend via classical ECDSA + reveal quantum path when needed.

### 3. Multisig / Covenant style
Require both classical signature and knowledge of the quantum commitment.

## Wallet flow
1. Generate HybridKeyManager (Merkle recommended).
2. Store classical private key securely (as today).
3. Store quantum secret material offline (one-time keys).
4. Publish commitment on-chain (OP_RETURN or script).
5. For spend:
   - Classical path for normal tx.
   - When quantum threat active: reveal OTS signature + path + classical.

## Hybrid mode recommendation
Use `sign_hybrid()` (v0.6+) to require both proofs in high-value scenarios.

Educational only — always audit before real funds.
