import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import copy_button
from components.results import generator_inputs, save_bar
from utils.generators import generate_thumbnail_ideas, random_tip

st.set_page_config(page_title="Thumbnail Ideas · CreatorKit", page_icon="🖼️", layout="wide")
apply_styles()
render_sidebar()
hero("🖼️ Thumbnail Ideas", "Eye-catching thumbnail concepts.")

game, fmt, topic = generator_inputs("thumb")
st.write("")
if st.button("✨ Generate Thumbnail Ideas"):
    if not topic.strip():
        st.warning("Please type a topic or click one of the ideas above.")
    else:
        st.session_state["thumb_result"] = {
            "game": game, "fmt": fmt, "topic": topic,
            "items": generate_thumbnail_ideas(game, topic), "tip": random_tip()}

res = st.session_state.get("thumb_result")
if res:
    for i, item in enumerate(res["items"], 1):
        text = f"{item['idea']}\nSuggested text: {item['text']}"
        st.markdown(
            f'<div class="ck-card"><div class="icon">🖼️</div><h3>Idea {i}</h3>'
            f'<p>{item["idea"]}</p><p style="margin-top:.6rem;color:#60A5FA">'
            f'Text on thumbnail: <b>{item["text"]}</b></p></div>',
            unsafe_allow_html=True)
        copy_button(text)
        save_bar("Thumbnail", res["game"], res["fmt"], res["topic"], text, f"save_thumb_{i}")
        st.write("")
    st.info(f"💡 Tip: {res['tip']}")
