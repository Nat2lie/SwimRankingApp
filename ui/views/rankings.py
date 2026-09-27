import streamlit as st

from components import esc, medal_chip, podium, result_table, section
from meet import rank_heat
from pageshell import heat_editor, open_screen, sample_note, starting_heat

open_screen(
    "Rankings",
    "material/leaderboard",
    "Enter each swimmer's time and sort the heat from fastest to slowest.",
    [
        ("Input", "A name and a time for every swimmer in the heat."),
        ("Order", "The lowest time ranks first."),
        ("Medals", "First is Gold, second is Silver, third is Bronze."),
    ],
)

section("Heat", "pool", "Edit any cell, or add a row at the bottom")
heat = starting_heat()
sample_note(heat)
swimmers, problems = heat_editor("rank_editor", heat)
for problem in problems:
    st.warning(problem, icon=":material/error:")

if st.button("Rank heat", type="primary", icon=":material/leaderboard:", disabled=bool(problems) or not swimmers):
    st.session_state.ranked = rank_heat(swimmers)
    st.session_state.heat = [(row["Athlete"], row["Time"]) for row in st.session_state.ranked]
    st.toast(f"Ranked {len(swimmers)} swimmers", icon=":material/emoji_events:")

ranked = st.session_state.get("ranked")
if ranked:
    section("Result", "emoji_events", "Carries over to Points and Fouls")
    podium(ranked, "Time", " s")
    result_table(
        ["Place", "Athlete", "Time (s)", "Medal"],
        [[f"<b>{r['Place']}</b>", esc(r["Athlete"]), f"{r['Time']:.2f}", medal_chip(r["Medal"])] for r in ranked],
        highlight={0},
    )
