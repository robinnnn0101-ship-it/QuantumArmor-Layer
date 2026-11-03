# Contributing to QuantumArmor-Layer

Thanks for looking at the armor.

## Ground rules

- Keep it pure-Python and auditable.
- Prefer small, focused PRs.
- Add tests for any new crypto path.
- Do not introduce constant-time claims without evidence.
- Update README and SECURITY.md if threat model changes.

## Development

```bash
git clone https://github.com/robinnnn0101-ship-it/QuantumArmor-Layer
cd QuantumArmor-Layer
pip install -e .[test]
pytest
```

## Areas that need work

- Better serialization formats
- Bitcoin script examples (Taproot leaf)
- Performance benchmarks
- Optional Rust/C bindings (out of scope for reference)
- Formal verification sketches
- Wallet integration sketches

## Code style

- Black-friendly
- Type hints where useful
- Docstrings on public classes

**Break the illusion. Build the armor.**
