#!/usr/bin/env python3
"""
QuantumArmor CLI v0.7.1
"""

from __future__ import annotations
import argparse
import json
import sys
from .hybrid import HybridKeyManager


def cmd_generate(args):
    try:
        n = args.leaves if args.mode == "merkle" else 1
        use_wots = args.mode == "wots"
        km = HybridKeyManager.generate(n_leaves=n, use_wots=use_wots)
        pub = km.export_public()
        print(json.dumps(pub, indent=2))
        print(f"Commitment: {km.export_commitment()}", file=sys.stderr)
        print(f"Remaining: {km.remaining_quantum()}", file=sys.stderr)
        print(f"Status: {km.get_status()}", file=sys.stderr)
        if args.out:
            with open(args.out, "w") as f:
                json.dump({"public": pub, "commitment": km.export_commitment(), "status": km.get_status(), "mode": args.mode}, f, indent=2)
            print(f"Public info written to {args.out}", file=sys.stderr)
        return km
    except Exception as e:
        print(f"Generate failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_sign(args):
    try:
        n = args.leaves if args.mode == "merkle" else 1
        use_wots = args.mode == "wots"
        km = HybridKeyManager.generate(n_leaves=n, use_wots=use_wots)
        msg = args.message.encode()
        if args.hybrid:
            sig = km.sign_hybrid(msg)
        else:
            sig = {"quantum": km.sign_quantum(msg)}
        out = {"signature": sig, "public": km.export_public(), "status": km.get_status(), "message": args.message}
        print(json.dumps(out, indent=2, default=str))
        if args.out:
            with open(args.out, "w") as f:
                json.dump(out, f, indent=2, default=str)
    except Exception as e:
        print(f"Sign failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_verify(args):
    print("Educational verify: load signature JSON and matching public commitment.", file=sys.stderr)
    if not args.sig:
        print("Provide --sig file", file=sys.stderr)
        sys.exit(1)
    try:
        with open(args.sig) as f:
            data = json.load(f)
        print(json.dumps({"loaded": True, "keys": list(data.keys())}, indent=2))
    except Exception as e:
        print(f"Verify load failed: {e}", file=sys.stderr)
        sys.exit(1)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="quantumarmor",
        description="QuantumArmor-Layer CLI v0.7.1 — Hybrid Quantum-Proof for Bitcoin"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate", help="Generate hybrid key")
    p_gen.add_argument("--mode", choices=["lamport", "merkle", "wots"], default="merkle")
    p_gen.add_argument("--leaves", type=int, default=16)
    p_gen.add_argument("--out", help="Write public info to JSON file")
    p_gen.set_defaults(func=cmd_generate)

    p_sign = sub.add_parser("sign", help="Sign a message (educational)")
    p_sign.add_argument("--message", required=True)
    p_sign.add_argument("--mode", choices=["lamport", "merkle", "wots"], default="merkle")
    p_sign.add_argument("--leaves", type=int, default=4)
    p_sign.add_argument("--hybrid", action="store_true", help="Require classical + quantum")
    p_sign.add_argument("--out")
    p_sign.set_defaults(func=cmd_sign)

    p_ver = sub.add_parser("verify", help="Verify signature sketch")
    p_ver.add_argument("--message", required=True)
    p_ver.add_argument("--sig", help="Signature JSON")
    p_ver.set_defaults(func=cmd_verify)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
