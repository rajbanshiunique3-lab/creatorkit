import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ---------- Background ---------- */
.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(139, 92, 246, 0.12), transparent 40%),
        radial-gradient(circle at 90% 10%, rgba(59, 130, 246, 0.10), transparent 40%),
        #000000;
}

/* Hide default Streamlit chrome */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B0B16 0%, #07070D 100%);
    border-right: 1px solid rgba(139, 92, 246, 0.2);
}

/* ---------- Headings ---------- */
/* ---------- Hide Streamlit's default page list (we use our own) ---------- */
[data-testid="stSidebarNav"] { display: none; }

/* ---------- Sidebar navigation links ---------- */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: 10px !important;
    padding: 0.55rem 0.9rem !important;
    justify-content: flex-start !important;
    transition: all 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: rgba(139, 92, 246, 0.15) !important;
    border-color: rgba(139, 92, 246, 0.4) !important;
    transform: none;
    box-shadow: none;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(139,92,246,0.3), rgba(59,130,246,0.2)) !important;
    border-color: rgba(139, 92, 246, 0.6) !important;
}
h1, h2, h3 {
    font-weight: 800 !important;
    letter-spacing: -0.5px;
    color: #F5F5FA !important;
}

/* ---------- Sidebar text ---------- */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #F5F5FA !important;
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #B8B8D0 !important;
}
/* ---------- Hero ---------- */
.hero {
    padding: 2.2rem 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(139,92,246,0.25), rgba(59,130,246,0.18));
    border: 1px solid rgba(139, 92, 246, 0.35);
    margin-bottom: 1.5rem;
}
.hero h1 {
    margin: 0;
    font-size: 2.4rem;
    background: linear-gradient(90deg, #A78BFA, #60A5FA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    margin: 0.5rem 0 0 0;
    color: #B8B8D0;
    font-size: 1.05rem;
}

/* ---------- Cards ---------- */
.ck-card {
    background: linear-gradient(145deg, #11111F, #0A0A14);
    border: 1px solid rgba(139, 92, 246, 0.22);
    border-radius: 16px;
    padding: 1.3rem;
    height: 100%;
    transition: all 0.25s ease;
}
.ck-card:hover {
    transform: translateY(-4px);
    border-color: rgba(139, 92, 246, 0.7);
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.18);
}
.ck-card .icon { font-size: 2rem; margin-bottom: 0.4rem; }
.ck-card h3 { margin: 0 0 0.3rem 0; font-size: 1.1rem; color: #F5F5FA; }
.ck-card p { margin: 0; color: #9A9AB5; font-size: 0.9rem; line-height: 1.5; }

.stat-card {
    background: linear-gradient(145deg, #11111F, #0A0A14);
    border: 1px solid rgba(59, 130, 246, 0.25);
    border-radius: 16px;
    padding: 1.1rem 1.3rem;
}
.stat-card .label { color: #9A9AB5; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
.stat-card .value { font-size: 1.9rem; font-weight: 800; color: #F5F5FA; }
.stat-card .hint { color: #60A5FA; font-size: 0.8rem; }

/* ---------- Buttons ---------- */
/* ---------- Result rows ---------- */
.result-row {
    background: linear-gradient(145deg, #11111F, #0A0A14);
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 12px;
    padding: 0.8rem 1.1rem;
    color: #F5F5FA;
    font-weight: 500;
}
.result-row .chars {
    display: block;
    margin-top: 0.2rem;
    color: #60A5FA;
    font-size: 0.72rem;
    font-weight: 400;
}
.stButton > button, .stDownloadButton > button, [data-testid="stPageLink"] a {
    background: linear-gradient(90deg, #8B5CF6, #3B82F6);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1.4rem;
    font-weight: 600;
    transition: all 0.2s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(139, 92, 246, 0.45);
    color: white;
    border: none;
}

/* ---------- Inputs ---------- */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
    background-color: #0F0F1A !important;
    border: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-radius: 10px !important;
    color: #F5F5FA !important;
}

/* ---------- Responsive ---------- */
@media (max-width: 768px) {
    .hero { padding: 1.4rem 1.1rem; }
    .hero h1 { font-size: 1.7rem; }
    .block-container { padding-left: 1rem; padding-right: 1rem; }
}
</style>
"""


def apply_styles():
    """Inject the CreatorKit dark theme into the current page."""
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str):
    """Show the big gradient header at the top of a page."""
    st.markdown(
        f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )