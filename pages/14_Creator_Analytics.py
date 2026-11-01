import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="Creator Analytics · CreatorKit", page_icon="📊", layout="wide")
apply_styles()
render_sidebar()
hero("Creator Analytics", "Usage charts built from your real CreatorKit data.")
empty_state("📊", "Coming in Stage 7", "This tool is being built next. Everything else works as usual.")
