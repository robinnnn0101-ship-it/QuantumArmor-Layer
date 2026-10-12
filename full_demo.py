#!/usr/bin/env python3
"""Full demonstration of the QuantumArmor hybrid layer"""

from hybrid import HybridKeyManager
from utils import sha256

def main():
    print("=" * 50)
    print("  QuantumArmor-Layer · Full Demo")
    print("=" * 50)
    print()

    print("[1] Generating hybrid key...")
    mgr = HybridKeyManager.generate()
    info = mgr.export_public()
    print(f"  Classical pubkey : {info['classical_pubkey_hex'][:24]}...")
    print(f"  Hash160          : {info['classical_hash160_hex']}")
    print(f"  Lamport fingerprint: {info['lamport_fingerprint_hex']}")
    print()

    print("[2] Creating commitment...")
    commitment = sha256(
        mgr.public_key.classical_pubkey + mgr.public_key.lamport_fingerprint
    )
    print(f"  Commitment: {commitment.hex()}")
    print()

    print("[3] Signing sample transaction digest...")
    tx = b"example-sighash-or-txid"
    c_sig = mgr.sign_classical(tx)
    q_sig = mgr.sign_quantum(tx)
    print(f"  Classical sig size : {len(c_sig)} bytes")
    print(f"  Quantum sig size   : {len(q_sig.serialize())} bytes")
    print()

    print("[4] Verifying...")
    assert mgr.verify_classical(tx, c_sig)
    assert mgr.verify_quantum(tx, q_sig)
    print("  ✓ Both signatures verified")
    print()
    print("=" * 50)
    print("  Demo complete. The armor holds.")
    print("=" * 50)

if __name__ == "__main__":
    main()
