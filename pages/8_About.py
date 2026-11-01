import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import feature_card

st.set_page_config(page_title="About · CreatorKit", page_icon="ℹ️", layout="wide")
apply_styles()
render_sidebar()
hero("ℹ️ About CreatorKit", "A free toolkit for YouTube gaming creators.")

st.markdown("""
CreatorKit helps Minecraft, GTA V and Roblox creators plan videos faster. It generates
titles, descriptions, hashtags and thumbnail concepts, keeps your work organized, and
tracks how your videos perform. It runs entirely on your computer, needs no paid API,
and stores your data in simple files in the `data` folder.
""")

st.subheader("What you can do")
items = [
    ("✍️", "Generate", "Titles, descriptions and hashtags for Shorts and Long videos."),
    ("🖼️", "Design", "Thumbnail concepts with composition, background, lighting and subject."),
    ("💾", "Organize", "Save results, copy everything, and export as TXT, CSV or JSON."),
    ("📈", "Track", "Record views, likes and comments and see what works."),
]
for col, (icon, t, d) in zip(st.columns(4), items):
    with col:
        feature_card(icon, t, d)

st.write("")
l, r = st.columns(2)
with l:
    st.subheader("Quick start")
    st.markdown("""
1. Pick a game and video type.
2. Type a topic or click an idea.
3. Generate, then **Copy** or **Save**.
4. After publishing, add the video to the **Video Tracker**.
5. Set your channel name in **Settings**.
""")
with r:
    st.subheader("Good to know")
    st.markdown("""
- Generators use smart templates, not AI, so they work offline and are free.
- Your data never leaves your computer.
- Back up the `data` folder to keep your projects safe.
- Hashtags: YouTube shows the first 3 above the title.
""")

st.subheader("Built with")
st.caption("Python · Streamlit · pandas · Version 1.0")
