import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import copy_button
from components.results import generator_inputs, save_bar
from utils.generators import generate_hashtags

st.set_page_config(page_title="Hashtag Generator · CreatorKit", page_icon="#️⃣", layout="wide")
apply_styles()
render_sidebar()
hero("#️⃣ Hashtag Generator", "Trending hashtags for your niche.")

game, fmt, topic = generator_inputs("tags")
count = st.slider("How many hashtags?", 5, 15, 12)
st.write("")
if st.button("✨ Generate Hashtags"):
    if not topic.strip():
        st.warning("Please type a topic or click one of the ideas above.")
    else:
        st.session_state["tags_result"] = {
            "game": game, "fmt": fmt, "topic": topic,
            "items": generate_hashtags(game, topic, fmt, count)}

res = st.session_state.get("tags_result")
if res:
    text = " ".join(res["items"])
    st.subheader("Your Hashtags")
    st.code(text, language=None)
    copy_button(text)
    st.caption("YouTube only shows the first 3 hashtags above your title, and ignores all if you use more than 15.")
    save_bar("Hashtags", res["game"], res["fmt"], res["topic"], text, "save_tags")
