"""Basic CLI smoke (educational)."""

import subprocess
import sys


def test_cli_generate():
    result = subprocess.run(
        [sys.executable, "-m", "quantumarmor.cli", "generate", "--mode", "merkle", "--leaves", "2"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "classical_pubkey_hex" in result.stdout
