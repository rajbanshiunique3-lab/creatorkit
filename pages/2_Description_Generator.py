import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import copy_button
from components.results import generator_inputs, save_bar
from utils.generators import generate_descriptions

st.set_page_config(page_title="Description Generator · CreatorKit", page_icon="📝", layout="wide")
apply_styles()
render_sidebar()
hero("📝 Description Generator", "Full descriptions ready to paste.")

game, fmt, topic = generator_inputs("desc")
st.write("")
if st.button("✨ Generate Descriptions"):
    if not topic.strip():
        st.warning("Please type a topic or click one of the ideas above.")
    else:
        st.session_state["desc_result"] = {
            "game": game, "fmt": fmt, "topic": topic,
            "items": generate_descriptions(game, topic, fmt)}

res = st.session_state.get("desc_result")
if res:
    for i, d in enumerate(res["items"], 1):
        st.subheader(f"Option {i}")
        st.code(d, language=None)
        copy_button(d)
        save_bar("Description", res["game"], res["fmt"], res["topic"], d, f"save_desc_{i}")
