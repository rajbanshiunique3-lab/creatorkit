import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import empty_state

st.set_page_config(page_title="Background Remover · CreatorKit", page_icon="✂️", layout="wide")
apply_styles()
render_sidebar()
hero("Background Remover", "Remove image backgrounds and download a transparent PNG.")
empty_state("✂️", "Coming in Stage 3", "This tool is being built next. Everything else works as usual.")
