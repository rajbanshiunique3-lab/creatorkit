import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from utils import storage
from utils.templates import GAME_NAMES, VIDEO_FORMATS

st.set_page_config(page_title="Settings · CreatorKit", page_icon="⚙️", layout="wide")
apply_styles()
render_sidebar()
hero("⚙️ Settings", "Make CreatorKit work the way you do.")

s = storage.load_settings()
with st.form("settings"):
    st.subheader("Profile")
    creator = st.text_input("Your name", value=s["creator"])
    channel = st.text_input("Channel name (used in descriptions)", value=s["channel"])
    st.subheader("Defaults")
    c1, c2 = st.columns(2)
    game = c1.selectbox("Default game", GAME_NAMES, index=GAME_NAMES.index(s["default_game"]))
    fmt = c2.selectbox("Default video type", VIDEO_FORMATS, index=VIDEO_FORMATS.index(s["default_format"]))
    tags = st.slider("Default hashtag count", 5, 15, int(s["hashtag_count"]))
    if st.form_submit_button("💾 Save Settings", type="primary"):
        storage.save_settings({"creator": creator, "channel": channel, "default_game": game,
                               "default_format": fmt, "hashtag_count": tags})
        st.success("Settings saved. Reopen a generator page to see your defaults.")

st.write("")
st.subheader("⚠️ Danger zone")
sure = st.checkbox("I understand this cannot be undone")
d1, d2, _ = st.columns([1.3, 1.3, 3])
if d1.button("Clear saved projects", disabled=not sure):
    storage.clear_projects()
    st.success("Saved projects cleared.")
if d2.button("Clear tracked videos", disabled=not sure):
    storage.clear_videos()
    st.success("Tracked videos cleared.")
