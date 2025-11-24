import subprocess
import sys

def test_run_program_outputs_expected():
    # executa o main e captura saída
    proc = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
    out = proc.stdout.strip()
    # ajuste a saída esperada conforme seu program.tiny
    assert out == "17"
