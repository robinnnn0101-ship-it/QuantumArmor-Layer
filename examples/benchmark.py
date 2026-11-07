#!/usr/bin/env python3
"""Simple benchmarks for QuantumArmor (educational)."""

import time
from quantumarmor import HybridKeyManager


def bench(label, fn, n=5):
    start = time.perf_counter()
    for _ in range(n):
        fn()
    elapsed = (time.perf_counter() - start) / n
    print(f"{label}: {elapsed*1000:.1f} ms avg")


def main():
    print("QuantumArmor v0.6 benchmarks (local pure-Python)")
    bench("Lamport generate", lambda: HybridKeyManager.generate(1, use_wots=False))
    bench("Merkle-16 generate", lambda: HybridKeyManager.generate(16))
    bench("WOTS generate", lambda: HybridKeyManager.generate(use_wots=True))

    km = HybridKeyManager.generate(8)
    msg = b"benchmark message"
    bench("Merkle sign", lambda: km.sign_quantum(msg, 0))
    bench("Hybrid sign", lambda: km.sign_hybrid(msg, 1))
    print("Done.")


if __name__ == "__main__":
    main()
