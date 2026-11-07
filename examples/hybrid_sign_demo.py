#!/usr/bin/env python3
"""Demo of hybrid (classical + quantum) signing."""

from quantumarmor import HybridKeyManager
import json


def main():
    print("=== Hybrid Sign Demo (v0.6) ===")
    km = HybridKeyManager.generate(n_leaves=8)
    msg = b"Vexlore Quantum Armor"
    sig = km.sign_hybrid(msg, index=0)
    print(json.dumps({
        "commitment": km.export_commitment(),
        "remaining": km.remaining_quantum(),
        "verified": km.verify_hybrid(msg, sig),
    }, indent=2))
    print("Public:", json.dumps(km.export_public(), indent=2))


if __name__ == "__main__":
    main()
