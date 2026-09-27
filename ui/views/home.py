import streamlit as st

from components import section
from scene import render_pool

st.html(
    """
    <section class="neo-home-hero">
      <p class="eyebrow">Meet desk</p>
      <h1 class="neo-title neo-title-xl">Swim <span class="neo-gradient-text">Ranking</span></h1>
      <p class="lede">Register a team, rank the heat, and settle points, records, fouls, and ties.</p>
    </section>
    """
)

render_pool(height=460)

section("Tools", "apps", "Work top to bottom, or jump to any screen")

tools = [
    ("views/team.py", "Team registration", ":material/groups:", "Add the roster and count female and male athletes."),
    ("views/rankings.py", "Rankings", ":material/leaderboard:", "Sort the heat by time. Fastest swim takes Gold."),
    ("views/points.py", "Points", ":material/scoreboard:", "Award 15, 7, 5, 3, 2, and 1 by finishing place."),
    ("views/records.py", "Records", ":material/timer:", "Check a time against the record for that age group."),
    ("views/fouls.py", "Fouls", ":material/flag:", "Move a fouled athlete to last and mark them DQ."),
    ("views/ties.py", "Tied times", ":material/handshake:", "Split the points when two athletes share a time."),
]

for start in range(0, len(tools), 3):
    columns = st.columns(3)
    for offset, (column, (path, label, icon, blurb)) in enumerate(zip(columns, tools[start : start + 3])):
        with column:
            with st.container(border=True, key=f"tool_{start + offset}"):
                st.page_link(path, label=label, icon=icon)
                st.caption(blurb)
