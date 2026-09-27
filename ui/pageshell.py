import pandas as pd
import streamlit as st

from components import hero, steps
from sample_data import SAMPLE_HEAT, SAMPLE_NOTE, SAMPLE_TIMES


def starting_heat() -> list[tuple[str, float]]:
    """The last ranked heat, else the registered roster, else the Olympic sample heat."""
    if st.session_state.get("heat"):
        return st.session_state.heat
    roster = st.session_state.get("roster", [])
    if roster:
        # Sample athletes bring their mock time; anyone else starts blank.
        return [(athlete[1], SAMPLE_TIMES.get(athlete[1], 0.0)) for athlete in roster]
    return SAMPLE_HEAT


def sample_note(rows: list[tuple[str, float]]) -> None:
    if any(name in SAMPLE_TIMES for name, _ in rows):
        st.html(f'<p class="neo-note"><span class="msr" aria-hidden="true">info</span>{SAMPLE_NOTE}</p>')


def heat_editor(key: str, rows: list[tuple[str, float]], fixed: bool = False) -> tuple[list[tuple[str, float]], list[str]]:
    """Editable name/time table. Returns the complete rows and any problems to show."""
    frame = pd.DataFrame(rows, columns=["Athlete", "Time"])
    edited = st.data_editor(
        frame,
        key=key,
        num_rows="fixed" if fixed else "dynamic",
        hide_index=True,
        width="stretch",
        column_config={
            "Athlete": st.column_config.TextColumn("Athlete", required=True),
            "Time": st.column_config.NumberColumn("Time (s)", min_value=0.0, step=0.01, format="%.2f", required=True),
        },
    )
    swimmers, problems = [], []
    for _, row in edited.iterrows():
        name = str(row["Athlete"]).strip() if pd.notna(row["Athlete"]) else ""
        time = row["Time"]
        if not name and pd.isna(time):
            continue
        if not name:
            problems.append("Every row needs an athlete name.")
            continue
        if pd.isna(time) or time <= 0:
            problems.append(f"Enter a time for {name}.")
            continue
        swimmers.append((name, float(time)))
    names = [name for name, _ in swimmers]
    if len(set(names)) != len(names):
        problems.append("Each athlete name must be unique in the heat.")
    return swimmers, problems


def open_screen(title: str, icon: str, summary: str, details: list[tuple[str, str]]) -> None:
    """Page header: icon badge, title, summary, then the rule explained in numbered steps."""
    hero(title, icon.removeprefix("material/"), summary)
    steps(details)
