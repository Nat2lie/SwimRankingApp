import streamlit as st

from components import esc, icon, medal_chip, result_table, section
from meet import split_ties
from pageshell import heat_editor, open_screen, sample_note, starting_heat
from sample_data import SAMPLE_HEAT

open_screen(
    "Tied times",
    "material/handshake",
    "When two athletes touch together, they share the points for those places.",
    [
        ("First and second", "They split 15 and 7. Third receives 7, fourth receives 3."),
        ("Second and third", "They split 7 and 5. First keeps 15, fourth receives 3."),
        ("Third and fourth", "They split 5 and 3. First keeps 15, second keeps 7."),
    ],
)

section("Four-swimmer heat", "pool", "Give two swimmers the same time to see the split")

heat = list(starting_heat())[:4]
heat += [row for row in SAMPLE_HEAT if row[0] not in {name for name, _ in heat}][: 4 - len(heat)]
sample_note(heat)
swimmers, problems = heat_editor("ties_editor", heat, fixed=True)
if len(swimmers) != 4 and not problems:
    problems.append("Fill in all four swimmers.")
for problem in problems:
    st.warning(problem, icon=":material/error:")

if st.button("Score heat", type="primary", icon=":material/handshake:", disabled=bool(problems)):
    st.session_state.ties = split_ties(swimmers)
    st.toast("Heat scored", icon=":material/handshake:")

scored = st.session_state.get("ties")
if scored:
    times = [r["Time"] for r in scored]
    tied = {i for i, t in enumerate(times) if times.count(t) > 1}
    section("Result", "handshake", "Tied swimmers are highlighted" if tied else "No tied times in this heat")
    result_table(
        ["Place", "Athlete", "Time (s)", "Points", "Medal"],
        [
            [
                f"<b>{r['Place']}</b>",
                esc(r["Athlete"]) + (f' <span class="neo-chip tie">{icon("handshake")}Tie</span>' if i in tied else ""),
                f"{r['Time']:.2f}",
                f"<b>{r['Points']:g}</b>",
                medal_chip(r["Medal"]),
            ]
            for i, r in enumerate(scored)
        ],
        highlight=tied,
    )
