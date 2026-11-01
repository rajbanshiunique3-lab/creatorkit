import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ---------- Layout ---------- */
.stApp { background: #FFFFFF; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px; }

h1, h2, h3 { font-weight: 700 !important; letter-spacing: -0.3px; color: #111827 !important; }
h3 { font-size: 1.15rem !important; }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] { background: #F8F9FC; border-right: 1px solid #E5E7EB; }
.brand { display: flex; align-items: center; gap: .6rem; margin: .2rem 0 1rem 0; }
.brand .logo {
    width: 34px; height: 34px; border-radius: 10px; background: #7C3AED; color: #fff;
    display: flex; align-items: center; justify-content: center; font-weight: 700;
}
.brand .name { font-weight: 700; font-size: 1.05rem; color: #111827; letter-spacing: .5px; }
.nav-label {
    font-size: .68rem; font-weight: 600; letter-spacing: 1.2px; color: #9CA3AF;
    margin: 1.1rem 0 .25rem .4rem;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    border-radius: 10px; padding: .45rem .75rem; color: #374151; font-weight: 500;
    transition: background .15s ease;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover { background: #EEF2FF; }
[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
    background: #EDE9FE; color: #6D28D9; font-weight: 600;
}

/* ---------- Hero ---------- */
.hero {
    padding: 2rem 2rem; border-radius: 20px; margin-bottom: 1.5rem;
    background: #F5F3FF; border: 1px solid #E4DCFB;
}
.hero h1 { margin: 0; font-size: 2rem; color: #111827; }
.hero p { margin: .5rem 0 0 0; color: #4B5563; font-size: 1.02rem; }

/* ---------- Cards ---------- */
.ck-card {
    background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 16px; padding: 1.25rem;
    box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 4px 12px rgba(16,24,40,.04);
    height: 100%; transition: all .2s ease;
}
.ck-card:hover { border-color: #C4B5FD; box-shadow: 0 8px 24px rgba(124,58,237,.10); transform: translateY(-2px); }
.ck-card .icon {
    width: 42px; height: 42px; border-radius: 12px; background: #F5F3FF; font-size: 1.3rem;
    display: flex; align-items: center; justify-content: center; margin-bottom: .7rem;
}
.ck-card h3 { margin: 0 0 .3rem 0; font-size: 1.02rem !important; }
.ck-card p { margin: 0; color: #6B7280; font-size: .88rem; line-height: 1.5; }

.stat-card {
    background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 16px; padding: 1.1rem 1.3rem;
    box-shadow: 0 1px 2px rgba(16,24,40,.04);
}
.stat-card .label { color: #6B7280; font-size: .75rem; font-weight: 600; text-transform: uppercase; letter-spacing: .8px; }
.stat-card .value { font-size: 1.8rem; font-weight: 700; color: #111827; }
.stat-card .hint { color: #7C3AED; font-size: .8rem; }

.badge { display: inline-block; font-size: .68rem; font-weight: 600; padding: .15rem .55rem;
    border-radius: 999px; background: #EDE9FE; color: #6D28D9; margin-left: .4rem; vertical-align: middle; }
.badge.soon { background: #F3F4F6; color: #6B7280; }

.empty-state {
    text-align: center; padding: 2.2rem 1rem; border: 1px dashed #D1D5DB;
    border-radius: 16px; background: #F9FAFB;
}
.empty-state .icon { font-size: 2rem; }
.empty-state h3 { margin: .4rem 0 .2rem 0; font-size: 1.05rem !important; }
.empty-state p { margin: 0; color: #6B7280; font-size: .9rem; }

.list-row {
    display: flex; justify-content: space-between; gap: 1rem; background: #FFFFFF;
    border: 1px solid #E5E7EB; border-radius: 12px; padding: .65rem 1rem; margin-bottom: .45rem;
    color: #111827; font-size: .9rem;
}
.list-row .when { color: #9CA3AF; font-size: .75rem; white-space: nowrap; }

/* ---------- Result rows ---------- */
.result-row {
    background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 12px;
    padding: .8rem 1.1rem; color: #111827; font-weight: 500;
}
.result-row .chars { display: block; margin-top: .2rem; color: #7C3AED; font-size: .72rem; font-weight: 400; }

/* ---------- Buttons & inputs ---------- */
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button {
    border-radius: 10px; font-weight: 600; transition: all .15s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-1px); box-shadow: 0 4px 12px rgba(124,58,237,.18);
}
.stTextInput input, .stTextArea textarea, .stNumberInput input { border-radius: 10px !important; }
[data-testid="stExpander"] { border-radius: 12px; border-color: #E5E7EB; }

/* ---------- Responsive ---------- */
@media (max-width: 768px) {
    .hero { padding: 1.3rem 1.1rem; }
    .hero h1 { font-size: 1.5rem; }
    .block-container { padding-left: 1rem; padding-right: 1rem; }
}
</style>
"""


def apply_styles():
    """Inject the CreatorKit light theme into the current page."""
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str):
    """Show the header panel at the top of a page."""
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>',
                unsafe_allow_html=True)
