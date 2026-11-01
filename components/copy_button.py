import html
import json

import streamlit.components.v1 as components

_TEMPLATE = """
<style>
  body { margin: 0; background: transparent; }
  button {
    width: 100%; height: 40px; cursor: pointer;
    background: linear-gradient(90deg, #8B5CF6, #3B82F6);
    color: white; border: none; border-radius: 10px;
    font-family: Inter, Arial, sans-serif; font-weight: 600; font-size: 14px;
    transition: all 0.2s ease;
  }
  button:hover { box-shadow: 0 6px 18px rgba(139, 92, 246, 0.5); }
</style>
<button id="btn">📋 Copy</button>
<script>
  const text = __TEXT__;
  const btn = document.getElementById("btn");

  function fallbackCopy() {
    const area = document.createElement("textarea");
    area.value = text;
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    document.body.removeChild(area);
  }

  btn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(text);
    } catch (err) {
      fallbackCopy();
    }
    btn.textContent = "✅ Copied!";
    setTimeout(() => { btn.textContent = "📋 Copy"; }, 1500);
  });
</script>
"""


def copy_button(text: str, height: int = 44):
    """Show a Copy button that puts `text` on the clipboard."""
    safe_text = json.dumps(text).replace("</", "<\\/")
    components.html(_TEMPLATE.replace("__TEXT__", safe_text), height=height)


def result_row(text: str):
    """Show one result line with a Copy button beside it."""
    import streamlit as st

    left, right = st.columns([5, 1], vertical_alignment="center")
    with left:
        st.markdown(
            f'<div class="result-row">{html.escape(text)}'
            f'<span class="chars">{len(text)} characters</span></div>',
            unsafe_allow_html=True,
        )
    with right:
        copy_button(text)