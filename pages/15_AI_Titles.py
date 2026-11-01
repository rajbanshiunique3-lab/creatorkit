import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Titles · CreatorKit", page_icon="✨", layout="wide")
apply_styles()
render_sidebar()
hero("✨ AI Title Generator", "Ten fresh titles written by an AI model running on your own PC.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("ait")
c1, c2 = st.columns(2)
fmt = c1.selectbox("📺 Video type", ai_ui.FORMATS, key="ait_fmt")
style = c2.selectbox("🎯 Style", list(prompts.TITLE_STYLES), key="ait_style")
topic = st.text_input("💡 What is your video about?", key="ait_topic",
                      placeholder="Example: I survived 100 days in Hardcore Minecraft")

if st.button("✨ Generate 10 Titles", type="primary"):
    if not topic.strip():
        st.warning("Please describe your video first.")
    else:
        text = ai_ui.run(provider, model, *prompts.titles(game, fmt, style, topic), temp)
        if text:
            items = parsing.parse_lines(text, 10)
            if items:
                st.session_state["ait_res"] = {"game": game, "fmt": fmt, "topic": topic, "items": items}
            else:
                st.warning("The model's answer could not be read. Please try again.")
                st.code(text, language=None)

res = st.session_state.get("ait_res")
if res:
    st.subheader("Your titles")
    for t in res["items"]:
        result_row(t)
    save_bar("AI Titles", res["game"], res["fmt"], res["topic"], "\n".join(res["items"]), "ait_save")
    ai_ui.footer(model)
