"""
Bitcoin commitment sketch using QuantumArmor Merkle root.
Educational only — not a full wallet integration.
"""

from quantumarmor.hybrid import HybridKeyManager


def main():
    km = HybridKeyManager.generate(n_leaves=32)
    pub = km.export_public()
    root = pub.get("merkle_root_hex") or pub["lamport_fingerprint_hex"]
    print("QuantumArmor commitment ready")
    print(f"  Mode          : {pub['mode']}")
    print(f"  Classical h160: {pub['classical_hash160_hex']}")
    print(f"  Quantum root  : {root}")
    print()
    print("Example OP_RETURN payload (32 bytes):")
    print(f"  OP_RETURN {root}")
    print()
    print("In a real wallet you would:")
    print("  1. Commit the root in an OP_RETURN or Taproot leaf")
    print("  2. Spend with classical sig + quantum proof when needed")
    print("  3. Rotate root after N uses")


if __name__ == "__main__":
    main()
