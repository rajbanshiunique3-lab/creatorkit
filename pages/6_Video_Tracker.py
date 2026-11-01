from datetime import date

import pandas as pd
import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.cards import stat_card
from utils import storage
from utils.templates import GAME_NAMES, VIDEO_FORMATS

st.set_page_config(page_title="Video Tracker · CreatorKit", page_icon="📈", layout="wide")
apply_styles()
render_sidebar()
hero("📈 Video Tracker", "Track views, likes and comments for every video you publish.")

with st.form("add_video", clear_on_submit=True):
    st.subheader("Add a video")
    title = st.text_input("Video title")
    c1, c2, c3 = st.columns(3)
    game = c1.selectbox("Game", GAME_NAMES)
    fmt = c2.selectbox("Video type", VIDEO_FORMATS)
    published = c3.date_input("Published on", value=date.today())
    c4, c5, c6 = st.columns(3)
    views = c4.number_input("Views", min_value=0, step=100)
    likes = c5.number_input("Likes", min_value=0, step=10)
    comments = c6.number_input("Comments", min_value=0, step=5)
    if st.form_submit_button("➕ Add Video", type="primary"):
        if title.strip():
            storage.add_video(title.strip(), game, fmt, str(published),
                              int(views), int(likes), int(comments))
            st.success("Video added!")
        else:
            st.warning("Please enter a video title.")

videos = storage.load_videos()
if not videos:
    st.info("No videos yet. Add your first one above.")
    st.stop()

total_views = sum(v["views"] for v in videos)
total_likes = sum(v["likes"] for v in videos)
total_comments = sum(v["comments"] for v in videos)
m1, m2, m3, m4 = st.columns(4)
with m1:
    stat_card("Videos", str(len(videos)), "Tracked")
with m2:
    stat_card("Views", f"{total_views:,}", f"Avg {total_views // len(videos):,} per video")
with m3:
    stat_card("Likes", f"{total_likes:,}", "Total")
with m4:
    stat_card("Comments", f"{total_comments:,}", "Total")

df = pd.DataFrame([{
    "Title": v["title"], "Game": v["game"], "Type": v["format"], "Published": v["published"],
    "Views": v["views"], "Likes": v["likes"], "Comments": v["comments"],
    "Engagement %": round((v["likes"] + v["comments"]) / v["views"] * 100, 2) if v["views"] else 0,
} for v in videos])

st.write("")
st.subheader("All videos")
st.dataframe(df, use_container_width=True, hide_index=True)
st.download_button("⬇️ Export CSV", df.to_csv(index=False), "creatorkit_videos.csv", "text/csv")

g1, g2 = st.columns(2)
with g1:
    st.subheader("Views by game")
    st.bar_chart(df.groupby("Game")["Views"].sum(), color="#8B5CF6")
with g2:
    st.subheader("Views over time")
    st.line_chart(df.sort_values("Published").set_index("Published")["Views"], color="#3B82F6")

st.subheader("✏️ Update or delete")
chosen = st.selectbox("Choose a video", videos, format_func=lambda v: v["title"])
u1, u2, u3 = st.columns(3)
nv = u1.number_input("Views", min_value=0, value=chosen["views"], key=f"v_{chosen['id']}")
nl = u2.number_input("Likes", min_value=0, value=chosen["likes"], key=f"l_{chosen['id']}")
nc = u3.number_input("Comments", min_value=0, value=chosen["comments"], key=f"c_{chosen['id']}")
b1, b2, _ = st.columns([1, 1, 4])
if b1.button("💾 Update"):
    storage.update_video(chosen["id"], int(nv), int(nl), int(nc))
    st.rerun()
if b2.button("🗑️ Delete"):
    storage.delete_video(chosen["id"])
    st.rerun()
