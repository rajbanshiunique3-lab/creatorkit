import streamlit as st

NAV = [
    ("DASHBOARD", [("app.py", "Home", "home")]),
    ("LOCAL AI STUDIO", [
        ("pages/15_AI_Titles.py", "AI Titles", "title"),
        ("pages/16_AI_Descriptions.py", "AI Descriptions", "article"),
        ("pages/17_AI_Hashtags.py", "AI Hashtags", "tag"),
        ("pages/18_AI_Video_Ideas.py", "AI Video Ideas", "tips_and_updates"),
        ("pages/19_AI_Thumbnails.py", "AI Thumbnail Concepts", "image"),
        ("pages/20_AI_Shorts.py", "AI Shorts", "smartphone"),
        ("pages/21_AI_Setup.py", "AI Setup", "memory"),
    ]),
    ("INSTANT TEMPLATES", [
        ("pages/1_Title_Generator.py", "Title Generator", "edit_note"),
        ("pages/2_Description_Generator.py", "Description Generator", "description"),
        ("pages/3_Hashtag_Generator.py", "Hashtag Generator", "tag"),
        ("pages/4_Thumbnail_Ideas.py", "Thumbnail Ideas", "lightbulb"),
    ]),
    ("IMAGE STUDIO", [
        ("pages/9_AI_Image_Generator.py", "AI Image Generator", "auto_awesome"),
        ("pages/10_Thumbnail_Studio.py", "AI Thumbnail Studio", "palette"),
        ("pages/11_Background_Remover.py", "Background Remover", "content_cut"),
        ("pages/12_Image_Enhancer.py", "AI Image Enhancer", "hd"),
        ("pages/13_Image_Resizer.py", "Image Resizer", "aspect_ratio"),
    ]),
    ("WORKSPACE", [
        ("pages/5_Saved_Projects.py", "Saved Projects", "folder"),
        ("pages/6_Video_Tracker.py", "Video Tracker", "monitoring"),
        ("pages/14_Creator_Analytics.py", "Creator Analytics", "analytics"),
    ]),
    ("SETTINGS", [
        ("pages/7_Settings.py", "Settings", "settings"),
        ("pages/8_About.py", "About", "info"),
    ]),
]


def render_sidebar():
    """Draw the CreatorKit sidebar with grouped navigation."""
    from components.ai_ui import status_chip

    with st.sidebar:
        st.markdown('<div class="brand"><div class="logo">C</div>'
                    '<div class="name">CREATORKIT</div></div>', unsafe_allow_html=True)
        status_chip()
        for label, links in NAV:
            st.markdown(f'<div class="nav-label">{label}</div>', unsafe_allow_html=True)
            for path, name, icon in links:
                st.page_link(path, label=name, icon=f":material/{icon}:")
        st.divider()
        st.caption("CreatorKit v1.2")
