# Changelog

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
