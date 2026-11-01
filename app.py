import streamlit as st

from components.styles import apply_styles, hero
from components.cards import feature_card, stat_card
from components.sidebar import render_sidebar
from utils import storage

st.set_page_config(page_title="CreatorKit", page_icon="🎮", layout="wide")
apply_styles()
render_sidebar()

hero("Welcome to CreatorKit 🎮",
     "Generate titles, descriptions, hashtags and thumbnail ideas for your "
     "Minecraft, GTA V and Roblox videos in seconds.")

s1, s2, s3, s4 = st.columns(4)
with s1:
    stat_card("Saved Projects", str(storage.count_projects()), "Your library")
with s2:
    stat_card("Games", "3", "Minecraft · GTA V · Roblox")
with s3:
    stat_card("Formats", "2", "Shorts · Long videos")
with s4:
    stat_card("Tools", "4", "All free")

st.write("")
st.subheader("Your Creator Tools")
tools = [
    ("✍️", "Title Generator", "Catchy, click-worthy YouTube titles.", "pages/1_Title_Generator.py"),
    ("📝", "Description Generator", "Full descriptions ready to paste.", "pages/2_Description_Generator.py"),
    ("#️⃣", "Hashtag Generator", "Trending hashtags for your niche.", "pages/3_Hashtag_Generator.py"),
    ("🖼️", "Thumbnail Ideas", "Eye-catching thumbnail concepts.", "pages/4_Thumbnail_Ideas.py"),
]
cols = st.columns(4)
for col, (icon, name, desc, page) in zip(cols, tools):
    with col:
        feature_card(icon, name, desc)
        st.page_link(page, label=f"Open {name}", icon="➡️")
