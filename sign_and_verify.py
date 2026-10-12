#!/usr/bin/env python3
"""Sign and verify with both classical and quantum signatures"""

from hybrid import HybridKeyManager

def main():
    print("=" * 50)
    print("  QuantumArmor-Layer · Sign & Verify")
    print("=" * 50)
    print()

    mgr = HybridKeyManager.generate()
    message = b"Bitcoin transaction protected by QuantumArmor"

    # Classical
    c_sig = mgr.sign_classical(message)
    print(f"Classical signature: {c_sig.hex()[:60]}...")
    assert mgr.verify_classical(message, c_sig)
    print("✓ Classical signature verified\n")

    # Quantum (one-time)
    q_sig = mgr.sign_quantum(message)
    print(f"Quantum signature size: {len(q_sig.serialize())} bytes")
    assert mgr.verify_quantum(message, q_sig)
    print("✓ Quantum signature verified\n")

    # One-time check
    try:
        mgr.sign_quantum(b"second use")
        print("ERROR")
    except RuntimeError as e:
        print(f"✓ One-time protection working: {e}")

    print("\nHybrid armor is working.")

if __name__ == "__main__":
    main()
