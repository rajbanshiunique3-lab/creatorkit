import html
import json

import streamlit as st
import streamlit.components.v1 as components

_TEMPLATE = """
<style>
  body { margin: 0; background: transparent; }
  button {
    width: 100%; height: 40px; cursor: pointer;
    background: #7C3AED;
    color: white; border: none; border-radius: 10px;
    font-family: Inter, Arial, sans-serif; font-weight: 600; font-size: 14px;
    transition: all 0.2s ease;
  }
  button:hover { background: #6D28D9; box-shadow: 0 4px 12px rgba(124, 58, 237, 0.25); }
</style>
<button id="btn"></button>
<script>
  const text = __TEXT__;
  const label = __LABEL__;
  const btn = document.getElementById("btn");
  btn.textContent = label;

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
    setTimeout(() => { btn.textContent = label; }, 1500);
  });
</script>
"""


def copy_button(text: str, label: str = "📋 Copy", height: int = 44):
    """Show a button that puts `text` on the clipboard."""
    safe_text = json.dumps(text).replace("</", "<\\/")
    safe_label = json.dumps(label)
    page = _TEMPLATE.replace("__TEXT__", safe_text).replace("__LABEL__", safe_label)
    components.html(page, height=height)


def result_row(text: str):
    """Show one result line with a Copy button beside it."""
    left, right = st.columns([5, 1], vertical_alignment="center")
    with left:
        st.markdown(
            f'<div class="result-row">{html.escape(text)}'
            f'<span class="chars">{len(text)} characters</span></div>',
            unsafe_allow_html=True,
        )
    with right:
        copy_button(text)
