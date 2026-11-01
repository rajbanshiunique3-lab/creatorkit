import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import result_row
from components.results import generator_inputs, save_bar
from utils.generators import generate_titles

st.set_page_config(page_title="Title Generator · CreatorKit", page_icon="✍️", layout="wide")
apply_styles()
render_sidebar()
hero("✍️ Title Generator", "Catchy, click-worthy YouTube titles in one click.")

game, fmt, topic = generator_inputs("title")
st.write("")
if st.button("✨ Generate Titles", type="primary"):
    if not topic.strip():
        st.warning("Please type a topic or click one of the ideas above.")
    else:
        st.session_state["title_result"] = {
            "game": game, "fmt": fmt, "topic": topic,
            "items": generate_titles(game, topic, fmt)}

res = st.session_state.get("title_result")
if res:
    st.subheader("Your Titles")
    for t in res["items"]:
        result_row(t)
    save_bar("Titles", res["game"], res["fmt"], res["topic"],
             "\n".join(res["items"]), "save_titles")
