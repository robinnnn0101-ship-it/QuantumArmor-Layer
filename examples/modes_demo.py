"""Demonstrate all three quantum modes."""

from quantumarmor import HybridKeyManager


def demo(mode: str):
    print(f"\n=== {mode.upper()} ===")
    if mode == "wots":
        km = HybridKeyManager.generate(use_wots=True)
    elif mode == "merkle":
        km = HybridKeyManager.generate(n_leaves=8)
    else:
        km = HybridKeyManager.generate()
    pub = km.export_public()
    print(f"Mode: {pub['mode']}")
    print(f"Commitment: {km.export_commitment()}")
    msg = b"armor-test"
    sig = km.sign_quantum(msg)
    ok = km.verify_quantum(msg, sig)
    print(f"Sign+verify: {'OK' if ok else 'FAIL'}")
    print(f"Remaining: {km.remaining_quantum()}")


if __name__ == "__main__":
    for m in ["lamport", "merkle", "wots"]:
        demo(m)
