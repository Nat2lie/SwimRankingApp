import streamlit as st

from components import esc, podium, result_table, section
from meet import award_points, rank_heat
from pageshell import heat_editor, open_screen, sample_note, starting_heat

open_screen(
    "Points",
    "material/scoreboard",
    "Award meet points from the finishing order.",
    [
        ("Places", "1st through 6th receive points. Later places stay on the list."),
        ("Scale", "The points are 15, 7, 5, 3, 2, then 1."),
        ("Result", "Each athlete keeps the points added for that place."),
    ],
)

section("Heat", "pool", "Times set the finishing order")
heat = starting_heat()
sample_note(heat)
swimmers, problems = heat_editor("points_editor", heat)
for problem in problems:
    st.warning(problem, icon=":material/error:")

if st.button("Award points", type="primary", icon=":material/scoreboard:", disabled=bool(problems) or not swimmers):
    order = [row["Athlete"] for row in rank_heat(swimmers)]
    st.session_state.points = award_points(order)
    st.toast("Points awarded", icon=":material/scoreboard:")

scored = st.session_state.get("points")
if scored:
    section("Points", "scoreboard")
    podium(scored, "Points", " pts")
    top = max(r["Points"] for r in scored) or 1
    result_table(
        ["Place", "Athlete", "Points"],
        [
            [
                f"<b>{r['Place']}</b>",
                esc(r["Athlete"]),
                f'<span class="neo-meter" style="--w:{r["Points"] / top * 100:.0f}%"><i></i></span><b>{r["Points"]}</b>',
            ]
            for r in scored
        ],
        highlight={0},
    )
