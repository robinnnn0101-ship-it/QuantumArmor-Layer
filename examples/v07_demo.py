#!/usr/bin/env python3
"""v0.7.1 demo: WOTS size, Merkle validation, public persistence sketch, pretty print, sign_count."""
from quantumarmor import HybridKeyManager
from quantumarmor.wots import WOTSKeyPair
from quantumarmor.persistence import sketch_export_public_only, warning
import os

print(warning())
print()

# WOTS size
w = WOTSKeyPair.generate()
print(f"WOTS estimated sig size: {w.estimated_sig_size()} bytes")
sig = w.sign(b"quantum armor")
print(f"Actual sig size: {sig.size_bytes} bytes")
print(f"Verify: {w.verify(b'quantum armor', sig)}")
print()

# Merkle + hybrid
km = HybridKeyManager.generate(n_leaves=8)
print("Pretty public:")
print(km.pretty_public())
print("Remaining:", km.remaining_quantum())
print("Sign count:", km.sign_count())

km.sign_quantum(b"demo")
print("After one sign - remaining:", km.remaining_quantum(), "count:", km.sign_count())

# Sketch export
out = "/tmp/qa_pub.json"
sketch_export_public_only(km, out)
print(f"Public sketch written to {out}")
print("Size:", os.path.getsize(out), "bytes")
