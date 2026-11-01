import streamlit as st


def feature_card(icon: str, title: str, description: str):
    """A clickable-looking feature card for the dashboard."""
    st.markdown(
        f'<div class="ck-card">'
        f'<div class="icon">{icon}</div>'
        f'<h3>{title}</h3>'
        f'<p>{description}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )


def stat_card(label: str, value: str, hint: str = ""):
    """A small statistics box."""
    st.markdown(
        f'<div class="stat-card">'
        f'<div class="label">{label}</div>'
        f'<div class="value">{value}</div>'
        f'<div class="hint">{hint}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )