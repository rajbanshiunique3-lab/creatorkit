import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="AI Thumbnail Studio · CreatorKit", page_icon="🎨", layout="wide")
apply_styles()
render_sidebar()
hero("AI Thumbnail Studio", "Upload images, add text and shapes, pick templates and download a 1280 × 720 thumbnail.")
empty_state("🎨", "Coming in Stage 2", "This tool is being built next. Everything else works as usual.")
