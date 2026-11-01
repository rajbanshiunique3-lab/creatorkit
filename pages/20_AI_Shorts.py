import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Shorts · CreatorKit", page_icon="📱", layout="wide")
apply_styles()
render_sidebar()
hero("📱 AI Shorts Generator", "YouTube Shorts concepts with hooks, short scripts and titles.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("ais")
theme = st.text_input("Theme (optional)", key="ais_theme", placeholder="Example: funny glitches")

if st.button("✨ Generate 5 Shorts", type="primary"):
    text = ai_ui.run(provider, model, *prompts.shorts(game, theme), temp)
    if text:
        st.session_state["ais_res"] = {"game": game, "topic": theme or "Shorts ideas",
                                       "blocks": parsing.split_blocks(text, "short")}

res = st.session_state.get("ais_res")
if res:
    st.subheader("Your Shorts")
    ai_ui.render_blocks(res["blocks"], "AI Short", res["game"], "YouTube Shorts", res["topic"], "ais")
    ai_ui.footer(model)
