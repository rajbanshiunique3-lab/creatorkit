import html
from collections import Counter

import pandas as pd
import streamlit as st

from components.styles import apply_styles, hero
from components.cards import feature_card, stat_card, empty_state
from components.sidebar import render_sidebar
from utils import storage

st.set_page_config(page_title="CreatorKit", page_icon="🎮", layout="wide")
apply_styles()
render_sidebar()

projects = storage.load_projects()
videos = storage.load_videos()
name = storage.load_settings()["creator"].strip()

hero(f"Welcome back, {html.escape(name)}" if name else "Welcome to CreatorKit",
     "Plan, create and track your gaming videos in one place: titles, descriptions, "
     "hashtags and thumbnail ideas for Minecraft, GTA V and Roblox.")

# ---------- Quick actions ----------
st.subheader("Quick actions")
actions = [
    ("✍️", "Title Generator", "Click-worthy titles in seconds.", "pages/1_Title_Generator.py"),
    ("📝", "Description Generator", "Full descriptions ready to paste.", "pages/2_Description_Generator.py"),
    ("#️⃣", "Hashtag Generator", "Hashtags for your niche.", "pages/3_Hashtag_Generator.py"),
    ("💡", "Thumbnail Ideas", "Composition, lighting and subjects.", "pages/4_Thumbnail_Ideas.py"),
]
for col, (icon, nm, desc, page) in zip(st.columns(4), actions):
    with col:
        feature_card(icon, nm, desc)
        st.page_link(page, label=f"Open {nm}", icon=":material/arrow_forward:")

# ---------- Usage statistics ----------
st.write("")
st.subheader("Usage statistics")
views = sum(v["views"] for v in videos)
engagement = (sum(v["likes"] + v["comments"] for v in videos) / views * 100) if views else 0
s1, s2, s3, s4 = st.columns(4)
with s1:
    stat_card("Saved projects", str(len(projects)), "In your library")
with s2:
    stat_card("Videos tracked", str(len(videos)), "Performance data")
with s3:
    stat_card("Total views", f"{views:,}", "Tracked videos")
with s4:
    stat_card("Engagement", f"{engagement:.1f}%", "Likes + comments / views")

# ---------- Recent projects + recently used tools ----------
st.write("")
left, right = st.columns([3, 2])
with left:
    st.subheader("Recent projects")
    if projects:
        for p in projects[:5]:
            st.markdown(
                f'<div class="list-row"><span><b>{html.escape(p["kind"])}</b> · '
                f'{html.escape(p["game"])} · {html.escape(p["topic"])}</span>'
                f'<span class="when">{p["created"]}</span></div>', unsafe_allow_html=True)
    else:
        empty_state("📁", "No projects yet", "Generate something and click Save to Projects.")
with right:
    st.subheader("Recently used tools")
    TOOL_PAGES = {
        "Titles": ("Title Generator", "pages/1_Title_Generator.py"),
        "Description": ("Description Generator", "pages/2_Description_Generator.py"),
        "Hashtags": ("Hashtag Generator", "pages/3_Hashtag_Generator.py"),
        "Thumbnail": ("Thumbnail Ideas", "pages/4_Thumbnail_Ideas.py"),
        "Thumbnail Set": ("Thumbnail Ideas", "pages/4_Thumbnail_Ideas.py"),
    }
    shown = []
    for p in projects:
        tool = TOOL_PAGES.get(p["kind"])
        if tool and tool not in shown:
            shown.append(tool)
    if shown:
        for label, page in shown[:4]:
            st.page_link(page, label=label, icon=":material/history:")
    else:
        empty_state("🕒", "Nothing yet", "Tools you save results from will appear here.")

# ---------- Video performance ----------
st.write("")
st.subheader("Video performance")
if videos:
    top = sorted(videos, key=lambda v: v["views"], reverse=True)[:8]
    st.bar_chart(pd.DataFrame({"Views": [v["views"] for v in top]},
                              index=[v["title"][:28] for v in top]), color="#7C3AED")
else:
    empty_state("📈", "No videos tracked", "Add a video in the Video Tracker to see performance here.")
    st.page_link("pages/6_Video_Tracker.py", label="Open Video Tracker", icon=":material/monitoring:")

# ---------- Featured tools ----------
st.write("")
st.subheader("Featured AI tools")
featured = [
    ("🎨", "AI Thumbnail Studio", "Design 1280 × 720 thumbnails.", "pages/10_Thumbnail_Studio.py"),
    ("✂️", "Background Remover", "Transparent PNGs in one click.", "pages/11_Background_Remover.py"),
    ("✨", "AI Image Generator", "Text to image.", "pages/9_AI_Image_Generator.py"),
    ("📐", "Image Resizer", "Presets for YouTube and Instagram.", "pages/13_Image_Resizer.py"),
]
for col, (icon, nm, desc, page) in zip(st.columns(4), featured):
    with col:
        feature_card(icon, nm, desc, badge="Coming soon")
        st.page_link(page, label="Preview", icon=":material/arrow_forward:")
