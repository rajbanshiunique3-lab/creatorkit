import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Thumbnail Concepts · CreatorKit", page_icon="🖼️", layout="wide")
apply_styles()
render_sidebar()
hero("🖼️ AI Thumbnail Concepts", "Written concepts with text, composition, colors and visual elements.")
st.info("These are written concepts for you or a designer. CreatorKit does not generate the thumbnail image itself.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("ait2")
fmt = st.selectbox("📺 Video type", ai_ui.FORMATS, key="ait2_fmt")
topic = st.text_input("💡 What is your video about?", key="ait2_topic", placeholder="Example: Escaping 5 stars in GTA V")

if st.button("✨ Generate 4 Concepts", type="primary"):
    if not topic.strip():
        st.warning("Please describe your video first.")
    else:
        text = ai_ui.run(provider, model, *prompts.thumbnails(game, fmt, topic), temp)
        if text:
            st.session_state["ait2_res"] = {"game": game, "fmt": fmt, "topic": topic,
                                            "blocks": parsing.split_blocks(text, "concept")}

res = st.session_state.get("ait2_res")
if res:
    st.subheader("Your concepts")
    ai_ui.render_blocks(res["blocks"], "AI Thumbnail Concept", res["game"], res["fmt"], res["topic"], "ait2")
    ai_ui.footer(model)
