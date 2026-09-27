from pathlib import Path

import streamlit as st

from components import esc, icon
from theme import inject_theme, render_appearance_menu

LOGO = Path(__file__).parent / "public" / "assets" / "main_logo.png"


def render_sidebar() -> None:
    state = st.session_state
    roster = state.get("roster", [])
    milestones = [
        ("Team registered", bool(roster) and all(a[4] for a in roster)),
        ("Heat ranked", bool(state.get("ranked"))),
        ("Points awarded", bool(state.get("points"))),
        ("Record checked", any(state.get("record_holders") or [])),
        ("Fouls settled", bool(state.get("fouls"))),
        ("Ties scored", bool(state.get("ties"))),
    ]
    done = sum(ok for _, ok in milestones)
    items = "".join(
        f'<li class="{"done" if ok else ""}" style="--i:{i}">{icon("check_circle" if ok else "radio_button_unchecked")}{esc(label)}</li>'
        for i, (label, ok) in enumerate(milestones)
    )
    with st.sidebar:
        st.html(
            f"""
            <div class="neo-progress">
              <div class="neo-progress-head"><span>Meet progress</span><b>{done}/{len(milestones)}</b></div>
              <div class="neo-progress-track"><i style="--w:{done / len(milestones) * 100:.0f}%"></i></div>
              <ul>{items}</ul>
            </div>
            """
        )
        with st.container(key="brand"):
            st.image(str(LOGO), width="stretch")

st.set_page_config(
    page_title="Swim Ranking",
    page_icon=":material/pool:",
    layout="wide",
    initial_sidebar_state="expanded",
)

appearance = st.session_state.setdefault("appearance_mode", "system")
inject_theme(appearance)
render_appearance_menu()

nav = st.navigation(
    {
        "Overview": [
            st.Page("views/home.py", title="Home", icon=":material/pool:", default=True),
        ],
        "Meet desk": [
            st.Page("views/team.py", title="Team registration", icon=":material/groups:", url_path="team"),
            st.Page("views/rankings.py", title="Rankings", icon=":material/leaderboard:", url_path="rankings"),
            st.Page("views/points.py", title="Points", icon=":material/scoreboard:", url_path="points"),
            st.Page("views/records.py", title="Records", icon=":material/timer:", url_path="records"),
            st.Page("views/fouls.py", title="Fouls", icon=":material/flag:", url_path="fouls"),
            st.Page("views/ties.py", title="Tied times", icon=":material/handshake:", url_path="ties"),
        ],
    }
)
nav.run()

# Drawn after the page runs so the checklist reflects what that page just did.
render_sidebar()
