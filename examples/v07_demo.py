#!/usr/bin/env python3
"""v0.7.1 demo: WOTS size, Merkle validation, public persistence sketch, pretty print, sign_count, reset, status JSON, percent, low remaining."""
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
print("Status JSON:")
print(km.export_status_json())
print("Remaining %:", km.remaining_percent())
print("Low remaining:", km.is_low_remaining())
print("Remaining:", km.remaining_quantum())
print("Sign count:", km.sign_count())

km.sign_quantum(b"demo")
print("After one sign - remaining %:", km.remaining_percent(), "low:", km.is_low_remaining())
print("Status JSON:")
print(km.export_status_json())

km.reset_sign_count()
print("After reset - count:", km.sign_count())

# Sketch export
out = "/tmp/qa_pub.json"
sketch_export_public_only(km, out)
print(f"Public sketch written to {out}")
print("Size:", os.path.getsize(out), "bytes")
