import streamlit as st


def render_sidebar():
    """Draw the CreatorKit sidebar with navigation links."""
    with st.sidebar:
        st.markdown("## 🎮 CreatorKit")
        st.caption("Tools for gaming creators")
        st.write("")

        st.page_link("app.py", label="Dashboard", icon="🏠")
        st.page_link("pages/1_Title_Generator.py", label="Title Generator", icon="✍️")
        st.page_link("pages/2_Description_Generator.py", label="Description Generator", icon="📝")
        st.page_link("pages/3_Hashtag_Generator.py", label="Hashtag Generator", icon="#️⃣")
        st.page_link("pages/4_Thumbnail_Ideas.py", label="Thumbnail Ideas", icon="🖼️")
        st.page_link("pages/5_Saved_Projects.py", label="Saved Projects", icon="💾")

        st.divider()
        st.caption("CreatorKit v0.1 · Free forever")