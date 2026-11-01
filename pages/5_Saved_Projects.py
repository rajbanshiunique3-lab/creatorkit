import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import copy_button
from utils import storage

st.set_page_config(page_title="Saved Projects · CreatorKit", page_icon="💾", layout="wide")
apply_styles()
render_sidebar()
hero("💾 Saved Projects", "Everything you saved, in one place.")

projects = storage.load_projects()
if not projects:
    st.info("Nothing saved yet. Generate something and click **Save to Projects**.")
else:
    games = ["All"] + sorted({p["game"] for p in projects})
    choice = st.selectbox("Filter by game", games)
    for p in projects:
        if choice != "All" and p["game"] != choice:
            continue
        title = f"{p['kind']} · {p['game']} · {p['format']} · {p['topic']}  ({p['created']})"
        with st.expander(title):
            st.code(p["content"], language=None)
            copy_button(p["content"])
            if st.button("🗑️ Delete", key=f"del_{p['id']}"):
                storage.delete_project(p["id"])
                st.rerun()
