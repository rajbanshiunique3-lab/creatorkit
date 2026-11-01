"""Quick check that CreatorKit can talk to Ollama.  Usage:  python test_ollama.py llama3.2:3b"""
import sys
import time

from ai.provider import AIError, get_provider
from ai.ollama_client import DEFAULT_MODEL

model = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
provider = get_provider("ollama")
status = provider.status(model)

print(f"Installed : {status.installed}")
print(f"Running   : {status.running}")
print(f"Models    : {status.models}")
print(f"Model OK  : {status.model_ready} ({model})")
print(f"Message   : {status.message}")
if not status.ok:
    print("\nRESULT: FAIL - fix the message above and run this again.")
    sys.exit(1)

print("\nAsking the model for 3 titles...")
start = time.time()
try:
    answer = provider.generate(
        "Give me 3 short YouTube titles for a Minecraft hardcore survival video. One per line, no numbering.",
        system="You are an expert YouTube title writer.",
        model=model,
    )
except AIError as exc:
    print(f"\nRESULT: FAIL - {exc}")
    sys.exit(1)

print(answer)
print(f"\nRESULT: OK - answered in {time.time() - start:.1f} seconds")
