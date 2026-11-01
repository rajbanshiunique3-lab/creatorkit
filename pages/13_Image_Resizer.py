import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="Image Resizer · CreatorKit", page_icon="📐", layout="wide")
apply_styles()
render_sidebar()
hero("Image Resizer", "Resize for YouTube, Shorts and Instagram with crop and fit controls.")
empty_state("📐", "Coming in Stage 5", "This tool is being built next. Everything else works as usual.")
