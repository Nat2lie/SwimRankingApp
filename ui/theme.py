from pathlib import Path

import streamlit as st

# Neumorphism: every surface shares the canvas colour and gets its shape from a
# dark shadow on one side and a light shadow on the other.
DARK_TOKENS = {
    "canvas": "#1c2631",
    "surface": "#1c2631",
    "surface_raised": "#212d39",
    "surface_soft": "#18212b",
    "text": "#eaf4f8",
    "muted": "#9db1bd",
    "accent": "#5fd0de",
    "accent_strong": "#8fe6ef",
    "accent_2": "#4f8dff",
    "on_accent": "#062029",
    "shadow_dark": "#10171e",
    "shadow_light": "#283644",
    "outline": "rgba(143, 222, 233, 0.08)",
    "glow": "rgba(95, 208, 222, 0.30)",
    "glass": "rgba(28, 38, 49, 0.92)",
    "blob": "rgba(95, 208, 222, 0.10)",
    "blob_2": "rgba(79, 141, 255, 0.09)",
    "pool_bg": "#0b1821",
    "grid_filter": "none",
    "gold": "#f2c14e",
    "silver": "#c6d1d9",
    "bronze": "#d9915f",
    "success": "#5fd99a",
    "warning": "#f5b85a",
    "danger": "#ff7f7f",
}

LIGHT_TOKENS = {
    "canvas": "#e4ebf0",
    "surface": "#e4ebf0",
    "surface_raised": "#ebf1f5",
    "surface_soft": "#dbe3e9",
    "text": "#172c38",
    "muted": "#5a7180",
    "accent": "#0f8ea3",
    "accent_strong": "#0a7486",
    "accent_2": "#2f6fe0",
    "on_accent": "#ffffff",
    "shadow_dark": "#bccad4",
    "shadow_light": "#ffffff",
    "outline": "rgba(15, 142, 163, 0.10)",
    "glow": "rgba(15, 142, 163, 0.24)",
    "glass": "rgba(228, 235, 240, 0.94)",
    "blob": "rgba(15, 142, 163, 0.10)",
    "blob_2": "rgba(47, 111, 224, 0.08)",
    "pool_bg": "#d7e4e9",
    # Data grids draw on a canvas with Streamlit's dark theme; flip them to match.
    "grid_filter": "invert(1) hue-rotate(180deg)",
    "gold": "#c9930f",
    "silver": "#7f8d98",
    "bronze": "#b0632f",
    "success": "#1f9d63",
    "warning": "#b87209",
    "danger": "#d64545",
}

MODES = {
    "light": (":material/light_mode:", "Light"),
    "system": (":material/contrast:", "Match device"),
    "dark": (":material/dark_mode:", "Dark"),
}


def _variables(tokens: dict[str, str]) -> str:
    return ";".join(f"--neo-{name.replace('_', '-')}: {value}" for name, value in tokens.items())


def current_mode() -> str:
    return st.session_state.get("appearance_mode") or "system"


def inject_theme(mode: str = "system") -> None:
    css = Path(__file__).with_name("theme.css").read_text(encoding="utf-8")
    active = LIGHT_TOKENS if mode == "light" else DARK_TOKENS
    media_override = ""
    if mode == "system":
        media_override = f"""
        @media (prefers-color-scheme: light) {{
          :root {{ {_variables(LIGHT_TOKENS)}; color-scheme: light; }}
        }}
        """
    st.markdown(
        f"<style>:root {{ {_variables(active)}; color-scheme: {mode if mode != 'system' else 'dark'}; }}"
        f"{media_override}{css}</style>",
        unsafe_allow_html=True,
    )


def render_appearance_menu() -> None:
    """One-tap light / device / dark switch floating in the top-right corner."""
    with st.container(key="appearance_menu"):
        st.segmented_control(
            "Color theme",
            options=list(MODES),
            format_func=lambda mode: MODES[mode][0],
            key="appearance_mode",
            required=True,
            label_visibility="collapsed",
        )
