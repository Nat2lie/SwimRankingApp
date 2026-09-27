import streamlit as st

from components import esc, icon, result_table, section
from meet import apply_foul, rank_heat
from pageshell import heat_editor, open_screen, sample_note, starting_heat

open_screen(
    "Fouls",
    "material/flag",
    "A foul sends that athlete to the back of the heat.",
    [
        ("Pick", "Choose the athlete who committed the foul."),
        ("Order", "Everyone behind them moves up one place."),
        ("Mark", "The fouled athlete finishes last and is shown as DQ."),
    ],
)

section("Heat", "pool")
heat = starting_heat()
sample_note(heat)
swimmers, problems = heat_editor("fouls_editor", heat)
for problem in problems:
    st.warning(problem, icon=":material/error:")

if swimmers and not problems:
    results = [(row["Athlete"], row["Time"]) for row in rank_heat(swimmers)]
    pick_col, button_col = st.columns([3, 1], vertical_alignment="bottom")
    fouled = pick_col.selectbox("Athlete who committed the foul", [name for name, _ in results])
    if button_col.button("Apply foul", type="primary", icon=":material/flag:", width="stretch"):
        st.session_state.fouls = apply_foul(results, fouled)
        st.toast(f"{fouled} disqualified", icon=":material/flag:")

outcome = st.session_state.get("fouls")
if outcome:
    section("Result", "flag")
    result_table(
        ["Place", "Athlete", "Result"],
        [
            [
                f"<b>{r['Place']}</b>",
                esc(r["Athlete"]),
                f'<span class="neo-chip dq">{icon("block")}DQ</span>' if r["Result"] == "DQ" else r["Result"],
            ]
            for r in outcome
        ],
        highlight={len(outcome) - 1},
    )
