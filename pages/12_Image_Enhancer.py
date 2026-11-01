import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="AI Image Enhancer · CreatorKit", page_icon="🔍", layout="wide")
apply_styles()
render_sidebar()
hero("AI Image Enhancer", "Sharpen and improve image quality with before and after previews.")
empty_state("🔍", "Coming in Stage 4", "This tool is being built next. Everything else works as usual.")
