import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Descriptions · CreatorKit", page_icon="📝", layout="wide")
apply_styles()
render_sidebar()
hero("📝 AI Description Generator", "Detailed descriptions with an intro, summary, keywords and calls to action.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("aid")
fmt = st.selectbox("📺 Video type", ai_ui.FORMATS, key="aid_fmt")
topic = st.text_input("💡 Video title or topic", key="aid_topic", placeholder="Example: Hardcore Survival Day 1")
details = st.text_area("What happens in the video? (optional)", key="aid_details", height=90)
keywords = st.text_input("Keywords to include (optional)", key="aid_kw", placeholder="minecraft, hardcore, survival")
o1, o2 = st.columns(2)
chapters = o1.checkbox("Include chapters", value=True, key="aid_ch", disabled=fmt == "YouTube Shorts")
cta = o2.checkbox("Include call to action", value=True, key="aid_cta")

if st.button("✨ Generate Description", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        channel = storage.load_settings()["channel"].strip()
        text = ai_ui.run(provider, model, *prompts.description(
            game, fmt, topic, details, keywords, chapters, cta, channel), temp)
        if text:
            st.session_state["aid_res"] = {"game": game, "fmt": fmt, "topic": topic, "text": text}

res = st.session_state.get("aid_res")
if res:
    st.subheader("Your description")
    st.code(res["text"], language=None, wrap_lines=True)
    save_bar("AI Description", res["game"], res["fmt"], res["topic"], res["text"], "aid_save")
    st.caption("Chapter timestamps are placeholders. Edit them to match your real video.")
    ai_ui.footer(model)
