"""Provider-neutral AI interface.

CreatorKit's pages only talk to `AIProvider`. Today the only provider is Ollama
(local). To add a hosted AI later, create one new class that implements these
three methods and register it in `get_provider`.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class AIError(Exception):
    """A problem with the AI engine, written so it can be shown to the user."""


@dataclass
class ProviderStatus:
    installed: bool = False
    running: bool = False
    models: list = field(default_factory=list)
    model_ready: bool = False
    message: str = ""

    @property
    def ok(self) -> bool:
        return self.running and self.model_ready


class AIProvider(ABC):
    name = "AI"

    @abstractmethod
    def status(self, model=None) -> ProviderStatus:
        """Check the engine (and optionally one model)."""

    @abstractmethod
    def list_models(self) -> list:
        """Names of models that are ready to use."""

    @abstractmethod
    def generate(self, prompt, system="", temperature=0.7, model=None) -> str:
        """Return the model's text answer. Raises AIError on any problem."""


def get_provider(name="ollama", **kwargs) -> AIProvider:
    if name == "ollama":
        from ai.ollama_client import OllamaProvider  # imported here to avoid a cycle
        return OllamaProvider(**kwargs)
    raise AIError(f"Unknown AI provider: {name}")
