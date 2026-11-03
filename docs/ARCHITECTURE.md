# Architecture — QuantumArmor-Layer

## High-level design

```
[ Classical ECDSA ]  +  [ Hash-based OTS (Lamport/WOTS) ]
          \                        /
           \                      /
            \                    /
             [ HybridKeyManager ]
                      |
                      v
              32-byte commitment
              (fingerprint or Merkle root)
                      |
                      v
                 Bitcoin UTXO
```

## Components

### Lamport OTS (`lamport.py`)
- Classic 256-bit hash-based one-time signature.
- 512 pre-images → 256 revealed on sign.
- Signature size ≈ 8 KB.

### Merkle-Lamport
- N independent Lamport keypairs.
- Leaves = fingerprints of each public key.
- Single 32-byte root committed on-chain.
- Allows N signatures before root must be rotated.

### WOTS (`wots.py`)
- Winternitz one-time signature.
- Smaller signatures (~2-3 KB) at the cost of more hashing.
- Includes checksum to prevent existential forgery.

### HybridKeyManager (`hybrid.py`)
- Combines secp256k1 ECDSA with chosen quantum path.
- Modes: pure Lamport, Merkle, or WOTS.
- Exports classical hash160 + quantum fingerprint/root.

## Commitment strategies

1. **OP_RETURN** — simplest, 32-byte root.
2. **Pay-to-Merkle-Root style** (BIP-360 inspired) — future script path.
3. **Multisig / Taproot leaf** — embed root in script.

## Design goals

- No soft/hard fork required.
- Usable today with existing Bitcoin rules.
- Pure Python reference for auditability.
- Pluggable quantum path (Lamport / WOTS / future).
