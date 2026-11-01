import html

import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.results import generator_inputs, save_bar
from utils.generators import generate_thumbnail_ideas, random_tip

st.set_page_config(page_title="Thumbnail Ideas · CreatorKit", page_icon="🖼️", layout="wide")
apply_styles()
render_sidebar()
hero("🖼️ Thumbnail Ideas", "Composition, background, lighting and subject suggestions.")

game, fmt, topic = generator_inputs("thumb")
st.write("")
if st.button("✨ Generate Thumbnail Ideas", type="primary"):
    if not topic.strip():
        st.warning("Please type a topic or click one of the ideas above.")
    else:
        st.session_state["thumb_result"] = {
            "game": game, "fmt": fmt, "topic": topic,
            "items": generate_thumbnail_ideas(game, topic), "tip": random_tip()}

FIELDS = [("🎬 Concept", "idea"), ("📐 Composition", "composition"), ("🧍 Subject", "subject"),
          ("🌄 Background", "background"), ("💡 Lighting", "lighting"),
          ("🎨 Colors", "palette"), ("🔤 Text", "text")]


def as_text(item):
    return "\n".join(f"{label.split(' ', 1)[1]}: {item[key]}" for label, key in FIELDS)


res = st.session_state.get("thumb_result")
if res:
    all_text = []
    for i, item in enumerate(res["items"], 1):
        rows = "".join(
            f'<p style="margin:.35rem 0"><b style="color:#6D28D9">{label}</b><br>'
            f'{html.escape(item[key])}</p>' for label, key in FIELDS)
        st.markdown(f'<div class="ck-card"><h3>Idea {i}</h3>{rows}</div>', unsafe_allow_html=True)
        save_bar("Thumbnail", res["game"], res["fmt"], res["topic"], as_text(item), f"save_thumb_{i}")
        all_text.append(f"--- Idea {i} ---\n{as_text(item)}")
        st.write("")
    st.subheader("All ideas")
    save_bar("Thumbnail Set", res["game"], res["fmt"], res["topic"],
             "\n\n".join(all_text), "save_thumb_all")
    st.info(f"💡 Tip: {res['tip']}")
