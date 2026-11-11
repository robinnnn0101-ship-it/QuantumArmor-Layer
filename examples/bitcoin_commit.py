#!/usr/bin/env python3
"""Educational OP_RETURN commitment sketch using v0.7.1 helpers."""
from quantumarmor import HybridKeyManager

def main():
    km = HybridKeyManager.generate(n_leaves=16)
    commit = km.commitment_bytes()
    print("32-byte commitment:", commit.hex())
    print("Ready for OP_RETURN:", commit.hex())
    print("Remaining leaves:", km.remaining_quantum())
    print("See docs/BITCOIN_INTEGRATION.md")

if __name__ == "__main__":
    main()
