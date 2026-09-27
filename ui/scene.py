from pathlib import Path

import streamlit as st

def render_pool(height: int = 460, compact: bool = False) -> None:
    html = Path(__file__).with_name("pool.html").read_text(encoding="utf-8")
    html = html.replace("__COMPACT__", "1" if compact else "0")
    html = html.replace("__THEME__", st.session_state.get("appearance_mode", "system"))
    st.iframe(html, height=height)
