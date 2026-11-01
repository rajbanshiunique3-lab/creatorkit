"""Shared interface pieces for the Ollama AI pages."""
import html

import streamlit as st

from ai import config
from ai.ollama_client import has_model
from ai.provider import AIError, get_provider
from components.results import save_bar

GAMES = ["Minecraft", "GTA V", "Roblox", "Fortnite", "Valorant", "Other"]
FORMATS = ["YouTube Shorts", "Long Video"]


def get_ai_provider():
    cfg = config.load()
    return get_provider("ollama", url=cfg["ollama_url"], timeout=cfg["timeout"])


@st.cache_data(ttl=5, show_spinner=False)
def cached_status(url, model):
    return get_provider("ollama", url=url).status(model)


def _problem(status):
    st.error(status.message)
    with st.expander("How to fix this", expanded=True):
        st.markdown(
            "1. Install Ollama from https://ollama.com/download\n"
            "2. Open the **Ollama** app so it runs in the background\n"
            "3. In a terminal run: `ollama pull llama3.2:3b`\n"
            "4. Reload this page"
        )
    st.page_link("pages/21_AI_Setup.py", label="Open AI Setup", icon=":material/memory:")


def ai_controls():
    """Check Ollama, show the model picker, and return (provider, model, temperature)."""
    cfg = config.load()
    status = cached_status(cfg["ollama_url"], cfg["model"])
    if not status.running or not status.models:
        _problem(status)
        st.stop()
    model = cfg["model"] if has_model(status.models, cfg["model"]) else status.models[0]
    with st.expander(f"⚙️ AI engine: {model}"):
        c1, c2 = st.columns(2)
        model = c1.selectbox("Model", status.models, index=status.models.index(model)
                             if model in status.models else 0, key="ai_model_sel")
        temp = c2.slider("Creativity", 0.0, 1.2, float(cfg["temperature"]), 0.1, key="ai_temp_sel",
                         help="Lower = safer and more predictable. Higher = more creative.")
        if model != cfg["model"] or temp != cfg["temperature"]:
            config.save({**cfg, "model": model, "temperature": temp})
    return get_ai_provider(), model, temp


def run(provider, model, system, prompt, temperature):
    """Generate text with a loading spinner. Returns None (and shows an error) on failure."""
    with st.spinner(f"Writing with {model}… the first request can take up to a minute while the model loads."):
        try:
            return provider.generate(prompt, system=system, temperature=temperature, model=model)
        except AIError as exc:
            st.error(str(exc))
            return None


def game_picker(prefix):
    choice = st.selectbox("🎮 Game", GAMES, key=f"{prefix}_game")
    if choice == "Other":
        return st.text_input("Game name", key=f"{prefix}_other", placeholder="Example: Fortnite").strip() or "gaming"
    return choice


def footer(model):
    st.caption(f"Generated locally by {model}. AI can make mistakes, so review everything before publishing.")


def render_blocks(blocks, kind, game, fmt, topic, prefix):
    """Show each AI idea in a card with Copy All and Save buttons."""
    for i, block in enumerate(blocks):
        body = html.escape(block).replace("\n", "<br>")
        st.markdown(f'<div class="ck-card" style="color:#111827;line-height:1.6">{body}</div>',
                    unsafe_allow_html=True)
        save_bar(kind, game, fmt, topic, block, f"{prefix}_save_{i}")
        st.write("")
    if len(blocks) > 1:
        st.subheader("Everything")
        save_bar(f"{kind} Set", game, fmt, topic, "\n\n".join(blocks), f"{prefix}_save_all")


def status_chip():
    """Small AI status indicator for the sidebar."""
    try:
        cfg = config.load()
        s = cached_status(cfg["ollama_url"], cfg["model"])
        if s.ok:
            dot, text = "#16A34A", f"AI ready · {cfg['model']}"
        elif s.running:
            dot, text = "#F59E0B", "AI needs a model"
        else:
            dot, text = "#9CA3AF", "AI offline"
    except Exception:
        dot, text = "#9CA3AF", "AI offline"
    st.markdown(f'<div style="font-size:.8rem;color:#4B5563;margin:-.4rem 0 .6rem .2rem">'
                f'<span style="color:{dot}">●</span> {html.escape(text)}</div>', unsafe_allow_html=True)
