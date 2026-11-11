# Changelog

## [0.7.1] - 2026-11-11

### Added
- `commitment_bytes()` helper on HybridKeyManager
- remaining count in export_public
- CLI prints commitment on generate
- BITCOIN_INTEGRATION.md
- SPHINCS_SKETCH.md
- Edge case tests
- Version bump to 0.7.1

### Changed
- Export version string
- Package version

## [0.7.0] - 2026-11-11

### Added
- Improved WOTS: size estimation helper, clearer constants, better checksum docs
- MerkleLamport: stronger index validation, better error handling, proof checks
- CLI v0.7: improved error handling, updated help, try/except guards
- Persistence sketches module (`persistence.py`) — educational public export only
- Tests for WOTS size, Merkle validation, hybrid version (`tests/test_v07.py`)
- New example `examples/v07_demo.py`
- Expanded API.md, PERFORMANCE.md, SIDECHANNEL.md
- Side-channel resistance guidance

### Changed
- HybridKeyManager exports version 0.7.0
- Package __init__ exports persistence helpers
- README, ROADMAP, SECURITY updated for next level

## [0.6.0] - 2026-11-07

### Added
- Full CLI: generate / sign / verify
- `sign_hybrid()` / `verify_hybrid()` requiring both classical + quantum
- Benchmark example (`examples/benchmark.py`)
- Dockerfile for quick demo
- docs/ROADMAP.md, COMPARISON.md, INTEGRATION.md
- Enhanced serialize helpers
- Hybrid signing tests
- Version bump and packaging polish

### Changed
- HybridKeyManager export version 0.6.0
- Better CLI argument handling

## [0.5.0] - 2026-11-04

### Added
- CLI entry point (`quantumarmor generate`)
- Expanded pytest suite (`tests/test_advanced.py`)
- Bitcoin OP_RETURN commitment example
- SECURITY.md, ARCHITECTURE.md, CONTRIBUTING.md, PERFORMANCE.md
- GitHub Actions CI (Python 3.9–3.12)
- .gitignore and packaging improvements
- `export_commitment()` helper
- Version export in public info

### Changed
- Bumped version to 0.5.0
- Updated README structure and quick start

## [0.4.0] - 2026-10-21

### Added
- WOTS (Winternitz) support for smaller signatures
- `use_wots=True` option

## [0.3.0] - 2026-10-19

### Added
- Merkle-Lamport multi-use under single root
- Proper src/ package layout

## [0.2.0] / earlier

- Initial Lamport + hybrid ECDSA reference
