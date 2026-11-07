#!/usr/bin/env python3
"""Educational sketch: embedding QuantumArmor root in a Taproot leaf."""

from quantumarmor import HybridKeyManager


def main():
    km = HybridKeyManager.generate(16)
    root = km.export_commitment()
    print("Merkle root (32 bytes):", root)
    print()
    print("Sketch script leaf (conceptual):")
    print(f"OP_PUSH <{root}> OP_EQUALVERIFY  # or similar commitment check")
    print("# Spend path: classical ECDSA + reveal quantum signature + Merkle path")
    print("# See docs/INTEGRATION.md for patterns")
    print("Remaining quantum slots:", km.remaining_quantum())


if __name__ == "__main__":
    main()
