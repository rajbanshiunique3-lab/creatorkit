
import subprocess
import webbrowser
import time
import sys

port = "8506"

app = subprocess.Popen([
    sys.executable,
    "-m", "streamlit",
    "run", "app.py",
    "--server.port", port
])

time.sleep(4)
webbrowser.open(f"http://localhost:{port}")

app.wait()
