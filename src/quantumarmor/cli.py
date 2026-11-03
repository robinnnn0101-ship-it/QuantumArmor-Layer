#!/usr/bin/env python3
"""
QuantumArmor CLI
Usage:
  quantumarmor generate --mode merkle --leaves 16
  quantumarmor sign --key key.json --message "hello"
"""

from __future__ import annotations
import argparse
import json
import sys
from .hybrid import HybridKeyManager


def cmd_generate(args):
    n = args.leaves if args.mode == "merkle" else 1
    use_wots = args.mode == "wots"
    km = HybridKeyManager.generate(n_leaves=n, use_wots=use_wots)
    pub = km.export_public()
    print(json.dumps(pub, indent=2))
    if args.out:
        with open(args.out, "w") as f:
            json.dump({"public": pub, "mode": args.mode}, f, indent=2)
        print(f"Public info written to {args.out}", file=sys.stderr)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="quantumarmor", description="QuantumArmor-Layer CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate", help="Generate hybrid key")
    p_gen.add_argument("--mode", choices=["lamport", "merkle", "wots"], default="merkle")
    p_gen.add_argument("--leaves", type=int, default=16)
    p_gen.add_argument("--out", help="Write public info to JSON file")
    p_gen.set_defaults(func=cmd_generate)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
