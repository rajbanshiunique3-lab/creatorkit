"""AI settings, stored in data/ai_settings.json (separate from the main settings)."""
import json

from utils.storage import DATA_DIR

FILE = DATA_DIR / "ai_settings.json"
DEFAULTS = {
    "model": "llama3.2:3b",
    "ollama_url": "http://localhost:11434",
    "temperature": 0.8,
    "timeout": 180,
}


def load():
    try:
        saved = json.loads(FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        saved = {}
    return {**DEFAULTS, **saved}


def save(cfg):
    DATA_DIR.mkdir(exist_ok=True)
    FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
