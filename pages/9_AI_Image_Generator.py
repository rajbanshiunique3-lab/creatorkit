import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="AI Image Generator · CreatorKit", page_icon="✨", layout="wide")
apply_styles()
render_sidebar()
hero("AI Image Generator", "Turn a text prompt into an image, preview it and download it.")
empty_state("✨", "Coming in Stage 6", "This tool is being built next. Everything else works as usual.")
