import subprocess
import sys

def test_program_runs():
    result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
    assert result.returncode == 0

