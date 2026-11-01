import streamlit as st

from utils.templates import GAME_NAMES, VIDEO_FORMATS, GAMES
from utils import storage


def generator_inputs(prefix):
    """Game, video type, topic box and idea buttons. Returns (game, format, topic)."""
    c1, c2 = st.columns(2)
    game = c1.selectbox("🎮 Game", GAME_NAMES, key=f"{prefix}_game")
    fmt = c2.selectbox("📺 Video type", VIDEO_FORMATS, key=f"{prefix}_fmt")
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
    """A button that saves the current result to Saved Projects."""
    if st.button("💾 Save to Projects", key=key):
        storage.add_project(kind, game, fmt, topic, content)
        st.success("Saved! Open **Saved Projects** in the sidebar to see it.")
