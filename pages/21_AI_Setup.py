import time

import streamlit as st

from ai import config
from ai.ollama_client import DEFAULT_MODEL, INSTALL_URL
from ai.provider import AIError, get_provider
from components import ai_ui
from components.cards import stat_card
from components.sidebar import render_sidebar
from components.styles import apply_styles, hero

st.set_page_config(page_title="AI Setup · CreatorKit", page_icon="🧠", layout="wide")
apply_styles()
render_sidebar()
hero("🧠 AI Setup", "Connect CreatorKit to Ollama, the free AI engine that runs on your PC.")

cfg = config.load()
url = st.text_input("Ollama address", cfg["ollama_url"], help="Leave as is unless you changed Ollama's port.")
provider = get_provider("ollama", url=url, timeout=cfg["timeout"])
status = provider.status(cfg["model"])

c1, c2, c3 = st.columns(3)
with c1:
    stat_card("Installed", "Yes" if status.installed else "No", "ollama.com/download")
with c2:
    stat_card("Running", "Yes" if status.running else "No", url)
with c3:
    stat_card("Model ready", "Yes" if status.model_ready else "No", cfg["model"])
st.write("")
(st.success if status.ok else st.error)(status.message)

st.subheader("Settings")
model = cfg["model"]
if status.models:
    idx = status.models.index(model) if model in status.models else 0
    model = st.selectbox("Model", status.models, index=idx)
else:
    model = st.text_input("Model name", model)
s1, s2 = st.columns(2)
temp = s1.slider("Creativity", 0.0, 1.2, float(cfg["temperature"]), 0.1)
timeout = s2.slider("Timeout (seconds)", 30, 600, int(cfg["timeout"]), 30)
if st.button("💾 Save AI Settings", type="primary"):
    config.save({"model": model, "ollama_url": url, "temperature": temp, "timeout": timeout})
    ai_ui.cached_status.clear()
    st.success("Saved.")

st.subheader("Test the AI")
if st.button("Run a test"):
    if not status.ok:
        st.error("Fix the problem above first.")
    else:
        start = time.time()
        with st.spinner("Asking the model…"):
            try:
                out = get_provider("ollama", url=url, timeout=timeout).generate(
                    "Write one short YouTube title for a Minecraft video.", model=model)
                st.success(f"Worked in {time.time() - start:.1f} seconds")
                st.code(out, language=None)
            except AIError as exc:
                st.error(str(exc))

st.subheader("Download models")
st.markdown(f"Run these in a terminal. `{DEFAULT_MODEL}` is the recommended start for a 6 GB graphics card.")
st.code(f"ollama pull {DEFAULT_MODEL}      # about 2 GB, fast, fits fully on your GPU\n"
        "ollama pull llama3.1:8b         # about 5 GB, better writing, slower on 6 GB cards\n"
        "ollama list                     # show downloaded models\n"
        "ollama ps                       # show what is loaded and whether it uses the GPU", language=None)

with st.expander("Installing Ollama"):
    st.markdown(f"1. Download from {INSTALL_URL}\n2. Run the installer\n"
                "3. Open a **new** terminal and run `ollama --version`\n4. Pull a model with the commands above")
with st.expander("About deploying CreatorKit online"):
    st.markdown("Ollama runs on your own computer. If you put CreatorKit on Streamlit Community Cloud, "
                "the AI pages cannot reach your PC and will show \"AI offline\". The template tools keep working. "
                "To use AI online later, a hosted AI provider can be added as one new file in the `ai` folder.")
