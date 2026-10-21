#!/usr/bin/env python3
"""Full demonstration of QuantumArmor hybrid layer with Merkle multi-use + WOTS"""

from quantumarmor import HybridKeyManager, sha256


def main():
    print("=" * 60)
    print("  QuantumArmor-Layer · Full Demo (v0.4 — Merkle + WOTS)")
    print("=" * 60)
    print()

    print("[1] Generating hybrid key with 16 Merkle leaves...")
    mgr = HybridKeyManager.generate(n_leaves=16)
    info = mgr.export_public()
    print(f"  Classical pubkey : {info['classical_pubkey_hex'][:24]}...")
    print(f"  Hash160          : {info['classical_hash160_hex']}")
    print(f"  Merkle root      : {info.get('merkle_root_hex', 'n/a')}")
    print(f"  Remaining uses   : {mgr.remaining_quantum()}")
    print()

    print("[2] Commitment (only 32-byte root needed on-chain)...")
    commitment = sha256(
        mgr.public_key.classical_pubkey + mgr.public_key.merkle_root
    )
    print(f"  Commitment: {commitment.hex()}")
    print()

    print("[3] Signing 3 sample transactions...")
    for i in range(3):
        tx = f"example-sighash-{i}".encode()
        c_sig = mgr.sign_classical(tx)
        q_bundle = mgr.sign_quantum(tx)
        print(f"  TX {i}: classical {len(c_sig)}B | quantum leaf {q_bundle['index']} | remaining {mgr.remaining_quantum()}")
        assert mgr.verify_classical(tx, c_sig)
    print()

    print("[4] WOTS mode demo (smaller signatures)...")
    wots_mgr = HybridKeyManager.generate(use_wots=True)
    msg = b"wots-demo"
    q_sig = wots_mgr.sign_quantum(msg)
    print(f"  WOTS signature size: {len(q_sig.serialize())} bytes")
    assert wots_mgr.verify_quantum(msg, q_sig)
    print("  ✓ WOTS verified")
    print()

    print("=" * 60)
    print("  Demo complete. Armor holds. Multi-use + WOTS active.")
    print("=" * 60)


if __name__ == "__main__":
    main()
