#!/usr/bin/env python3
"""Generate a hybrid classical + quantum-resistant key pair"""

from hybrid import HybridKeyManager

def main():
    print("=" * 50)
    print("  QuantumArmor-Layer · Key Generation")
    print("=" * 50)
    print()

    mgr = HybridKeyManager.generate()
    info = mgr.export_public()

    print("Classical Public Key:")
    print(f"  {info['classical_pubkey_hex']}")
    print()
    print("Classical HASH160:")
    print(f"  {info['classical_hash160_hex']}")
    print()
    print("Lamport Fingerprint (quantum commitment):")
    print(f"  {info['lamport_fingerprint_hex']}")
    print()
    print("Done. Store the secret material securely.")

if __name__ == "__main__":
    main()
