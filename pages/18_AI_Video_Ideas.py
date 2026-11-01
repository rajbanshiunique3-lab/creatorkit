import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Video Ideas · CreatorKit", page_icon="💡", layout="wide")
apply_styles()
render_sidebar()
hero("💡 AI Video Idea Generator", "Original video concepts with hooks and suggested titles.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("aiv")
c1, c2 = st.columns(2)
fmt = c1.selectbox("📺 Video type", ai_ui.FORMATS, key="aiv_fmt")
audience = c2.selectbox("👥 Audience", ["Casual viewers", "Kids and teens", "Competitive players", "Beginners"], key="aiv_aud")
theme = st.text_input("Theme or starting point (optional)", key="aiv_theme", placeholder="Example: building challenges")

if st.button("✨ Generate 5 Ideas", type="primary"):
    text = ai_ui.run(provider, model, *prompts.video_ideas(game, fmt, theme, audience), temp)
    if text:
        st.session_state["aiv_res"] = {"game": game, "fmt": fmt, "topic": theme or "Video ideas",
                                       "blocks": parsing.split_blocks(text, "idea")}

res = st.session_state.get("aiv_res")
if res:
    st.subheader("Your ideas")
    ai_ui.render_blocks(res["blocks"], "AI Video Idea", res["game"], res["fmt"], res["topic"], "aiv")
    ai_ui.footer(model)
