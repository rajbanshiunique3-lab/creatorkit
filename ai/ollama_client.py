"""Talks to a local Ollama server (default http://localhost:11434). No API key needed."""
import os
import shutil
from pathlib import Path

import requests

from ai.provider import AIError, AIProvider, ProviderStatus

DEFAULT_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2:3b"
INSTALL_URL = "https://ollama.com/download"


def find_ollama_exe():
    """Return the path to ollama.exe if it is installed, else None."""
    exe = shutil.which("ollama")
    if exe:
        return exe
    local = os.environ.get("LOCALAPPDATA")
    if local:
        candidate = Path(local) / "Programs" / "Ollama" / "ollama.exe"
        if candidate.exists():
            return str(candidate)
    return None


def has_model(models, name):
    """True if `name` is among the downloaded models (':latest' is optional)."""
    if not name:
        return False
    if name in models or f"{name}:latest" in models:
        return True
    return ":" not in name and any(m.split(":")[0] == name for m in models)


class OllamaProvider(AIProvider):
    name = "Ollama (local)"

    def __init__(self, url=DEFAULT_URL, timeout=180):
        self.url = (url or DEFAULT_URL).rstrip("/")
        self.timeout = timeout

    # ---------- status ----------
    def _is_running(self):
        try:
            requests.get(f"{self.url}/api/version", timeout=2).raise_for_status()
            return True
        except requests.RequestException:
            return False

    def list_models(self):
        try:
            r = requests.get(f"{self.url}/api/tags", timeout=5)
            r.raise_for_status()
            return sorted(m["name"] for m in r.json().get("models", []))
        except requests.RequestException as exc:
            raise AIError(f"Could not read the model list from Ollama at {self.url}.") from exc

    def status(self, model=None):
        running = self._is_running()
        installed = running or find_ollama_exe() is not None
        st = ProviderStatus(installed=installed, running=running)
        if not installed:
            st.message = f"Ollama is not installed. Download it free from {INSTALL_URL}, install it, then reload this page."
            return st
        if not running:
            st.message = ("Ollama is installed but not running. Open the Ollama app from the Start menu "
                          "(or run `ollama serve` in a terminal), then reload this page.")
            return st
        try:
            st.models = self.list_models()
        except AIError as exc:
            st.message = str(exc)
            return st
        if not st.models:
            st.message = f"Ollama is running but has no models yet. Run: ollama pull {DEFAULT_MODEL}"
        elif model and not has_model(st.models, model):
            st.message = f"The model '{model}' is not downloaded. Run: ollama pull {model}"
        else:
            st.model_ready = True
            st.message = "Ollama is ready."
        return st

    # ---------- generation ----------
    def generate(self, prompt, system="", temperature=0.7, model=None):
        model = model or DEFAULT_MODEL
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature, "num_ctx": 4096},
        }
        try:
            r = requests.post(f"{self.url}/api/chat", json=payload, timeout=(5, self.timeout))
        except requests.ConnectionError as exc:
            raise AIError(f"Cannot reach Ollama at {self.url}. Make sure the Ollama app is running.") from exc
        except requests.Timeout as exc:
            raise AIError(f"Ollama took longer than {self.timeout} seconds. Try a smaller model "
                          "or fewer results.") from exc
        if r.status_code == 404:
            raise AIError(f"The model '{model}' is not downloaded. Run: ollama pull {model}")
        if not r.ok:
            raise AIError(f"Ollama returned an error ({r.status_code}): {r.text[:200]}")
        try:
            text = r.json().get("message", {}).get("content", "").strip()
        except ValueError as exc:
            raise AIError("Ollama sent a reply CreatorKit could not read.") from exc
        if not text:
            raise AIError("The model returned an empty answer. Please try again.")
        return text
