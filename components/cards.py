import streamlit as st


def feature_card(icon: str, title: str, description: str, badge: str = ""):
    """A feature card with an icon chip. `badge` adds a small label like 'Coming soon'."""
    tag = f'<span class="badge soon">{badge}</span>' if badge else ""
    st.markdown(
        f'<div class="ck-card"><div class="icon">{icon}</div>'
        f'<h3>{title}{tag}</h3><p>{description}</p></div>',
        unsafe_allow_html=True,
    )


def stat_card(label: str, value: str, hint: str = ""):
    """A small statistics box."""
    st.markdown(
        f'<div class="stat-card"><div class="label">{label}</div>'
        f'<div class="value">{value}</div><div class="hint">{hint}</div></div>',
        unsafe_allow_html=True,
    )


def empty_state(icon: str, title: str, text: str):
    """A friendly placeholder shown when there is no data yet."""
    st.markdown(
        f'<div class="empty-state"><div class="icon">{icon}</div>'
        f'<h3>{title}</h3><p>{text}</p></div>',
        unsafe_allow_html=True,
    )
