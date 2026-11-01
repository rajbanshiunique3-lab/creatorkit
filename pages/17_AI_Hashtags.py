import streamlit as st

from ai import parsing, prompts
from components import ai_ui
from components.copy_button import copy_button, result_row
from components.results import save_bar
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero
from utils import storage

st.set_page_config(page_title="AI Hashtags · CreatorKit", page_icon="#️⃣", layout="wide")
apply_styles()
render_sidebar()
hero("#️⃣ AI Hashtag Generator", "Relevant hashtags and search keywords, kept separate.")
provider, model, temp = ai_ui.ai_controls()

game = ai_ui.game_picker("aih")
fmt = st.selectbox("📺 Video type", ai_ui.FORMATS, key="aih_fmt")
topic = st.text_input("💡 What is your video about?", key="aih_topic", placeholder="Example: Redstone mob farm tutorial")

if st.button("✨ Generate Hashtags", type="primary"):
    if not topic.strip():
        st.warning("Please describe your video first.")
    else:
        text = ai_ui.run(provider, model, *prompts.hashtags(game, fmt, topic), temp)
        if text:
            tags, kws = parsing.parse_hashtags_keywords(text)
            if tags or kws:
                st.session_state["aih_res"] = {"game": game, "fmt": fmt, "topic": topic, "tags": tags, "kws": kws}
            else:
                st.warning("The model's answer could not be read. Please try again.")
                st.code(text, language=None)

res = st.session_state.get("aih_res")
if res:
    tag_text, kw_text = " ".join(res["tags"]), ", ".join(res["kws"])
    st.subheader("Hashtags")
    st.code(tag_text or "(none)", language=None)
    if tag_text:
        copy_button(tag_text, label="📋 Copy Hashtags")
    st.caption("YouTube shows the first 3 hashtags above your title and ignores all of them if you use more than 15.")
    st.subheader("Keyword tags")
    st.code(kw_text or "(none)", language=None)
    if kw_text:
        copy_button(kw_text, label="📋 Copy Keywords")
    st.caption(f"{len(kw_text)} of 500 characters used (YouTube's limit for keyword tags).")
    save_bar("AI Hashtags", res["game"], res["fmt"], res["topic"],
             f"Hashtags: {tag_text}\nKeywords: {kw_text}", "aih_save")
    ai_ui.footer(model)
