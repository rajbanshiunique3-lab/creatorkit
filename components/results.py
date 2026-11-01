import streamlit as st

from components.copy_button import copy_button
from utils.templates import GAME_NAMES, VIDEO_FORMATS, GAMES
from utils import storage


def generator_inputs(prefix):
    """Game, video type, topic box and idea buttons. Returns (game, format, topic)."""
    s = storage.load_settings()
    g_idx = GAME_NAMES.index(s["default_game"]) if s["default_game"] in GAME_NAMES else 0
    f_idx = VIDEO_FORMATS.index(s["default_format"]) if s["default_format"] in VIDEO_FORMATS else 0
    c1, c2 = st.columns(2)
    game = c1.selectbox("🎮 Game", GAME_NAMES, index=g_idx, key=f"{prefix}_game")
    fmt = c2.selectbox("📺 Video type", VIDEO_FORMATS, index=f_idx, key=f"{prefix}_fmt")
    key = f"{prefix}_topic"

    def use_idea(idea):
        st.session_state[key] = idea

    topic = st.text_input("💡 What is your video about?", key=key,
                          placeholder="Example: Hardcore Survival")
    st.caption("Need an idea? Click one:")
    ideas = GAMES[game]["topic_ideas"]
    cols = st.columns(len(ideas))
    for col, idea in zip(cols, ideas):
        col.button(idea, key=f"{prefix}_idea_{game}_{idea}", on_click=use_idea,
                   args=(idea,), use_container_width=True)
    return game, fmt, topic


def save_bar(kind, game, fmt, topic, content, key):
    """Copy-all button and Save-to-Projects button side by side."""
    c1, c2, _ = st.columns([1.2, 1.6, 3], vertical_alignment="center")
    with c1:
        copy_button(content, label="📋 Copy All")
    with c2:
        if st.button("💾 Save to Projects", key=key):
            storage.add_project(kind, game, fmt, topic, content)
            st.toast("Saved to Projects ✅")
