import csv
import io
import json

import streamlit as st

from components.styles import apply_styles, hero
from components.sidebar import render_sidebar
from components.copy_button import copy_button
from utils import storage

st.set_page_config(page_title="Saved Projects · CreatorKit", page_icon="💾", layout="wide")
apply_styles()
render_sidebar()
hero("💾 Saved Projects", "Browse, copy and export everything you saved.")

projects = storage.load_projects()
if not projects:
    st.info("Nothing saved yet. Generate something and click **Save to Projects**.")
    st.stop()

f1, f2 = st.columns(2)
game_f = f1.selectbox("Filter by game", ["All"] + sorted({p["game"] for p in projects}))
kind_f = f2.selectbox("Filter by tool", ["All"] + sorted({p["kind"] for p in projects}))
shown = [p for p in projects
         if (game_f == "All" or p["game"] == game_f) and (kind_f == "All" or p["kind"] == kind_f)]
st.caption(f"Showing {len(shown)} of {len(projects)} projects")


def as_txt(items):
    return "\n\n".join(
        f"=== {p['kind']} | {p['game']} | {p['format']} | {p['topic']} | {p['created']} ===\n{p['content']}"
        for p in items)


def as_csv(items):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["created", "kind", "game", "format", "topic", "content"],
                       extrasaction="ignore")
    w.writeheader()
    w.writerows(items)
    return buf.getvalue()


st.subheader("📤 Export")
e1, e2, e3, e4 = st.columns(4)
with e1:
    st.download_button("⬇️ Text (.txt)", as_txt(shown), "creatorkit_projects.txt", "text/plain",
                       use_container_width=True)
with e2:
    st.download_button("⬇️ CSV (.csv)", as_csv(shown), "creatorkit_projects.csv", "text/csv",
                       use_container_width=True)
with e3:
    st.download_button("⬇️ JSON (.json)", json.dumps(shown, indent=2, ensure_ascii=False),
                       "creatorkit_projects.json", "application/json", use_container_width=True)
with e4:
    copy_button(as_txt(shown), label="📋 Copy Everything")

st.write("")
for p in shown:
    with st.expander(f"{p['kind']} · {p['game']} · {p['format']} · {p['topic']}  ({p['created']})"):
        st.code(p["content"], language=None)
        c1, c2, c3, _ = st.columns([1.2, 1.4, 1.2, 3], vertical_alignment="center")
        with c1:
            copy_button(p["content"], label="📋 Copy")
        with c2:
            st.download_button("⬇️ Download", p["content"], f"{p['kind']}_{p['id']}.txt",
                               key=f"dl_{p['id']}")
        with c3:
            if st.button("🗑️ Delete", key=f"del_{p['id']}"):
                storage.delete_project(p["id"])
                st.rerun()
