import streamlit as st

from components import banner, empty_state, esc, icon, result_table, section, stat_tiles
from meet import finish_registration, register_athlete, roster_counts
from pageshell import open_screen
from sample_data import OLYMPIANS, SAMPLE_NOTE, SAMPLE_TEAM, age as age_of

open_screen(
    "Team registration",
    "material/groups",
    "Add a team and its athletes, then read the roster counts.",
    [
        ("Team", "Start with the team name, then add athletes one by one."),
        ("Athlete", "Each entry needs a full name, an age group, and a gender."),
        ("Result", "When registration is finished, the screen shows total, female, and male."),
    ],
)


def load_sample() -> None:
    st.session_state.team_name = SAMPLE_TEAM
    st.session_state.roster = [
        register_athlete(SAMPLE_TEAM, name, age_of(born), gender) for name, _, gender, born, _ in OLYMPIANS
    ]
    st.session_state.pop("heat", None)


def start_over() -> None:
    st.session_state.roster = []
    st.session_state.pop("team_name", None)


roster = st.session_state.setdefault("roster", [])
done = bool(roster) and all(athlete[4] for athlete in roster)

section("Team", "badge")
name_col, sample_col = st.columns([3, 1.3], vertical_alignment="bottom")
team = name_col.text_input("Team name", key="team_name", disabled=bool(roster), placeholder="e.g. Riverside Sharks")
if not roster:
    sample_col.button(
        f"Load {len(OLYMPIANS)} Olympians",
        icon=":material/playlist_add:",
        on_click=load_sample,
        help=SAMPLE_NOTE,
        width="stretch",
    )

with st.form("add_athlete", clear_on_submit=True, border=True):
    st.html(f'<p class="neo-form-title">{icon("person_add")}Add an athlete</p>')
    name_col, age_col, gender_col = st.columns([3, 1, 1.2])
    name = name_col.text_input("Full name", placeholder="First and last name")
    age = age_col.number_input("Age", min_value=8, max_value=99, value=10, step=1)
    gender = gender_col.segmented_control("Gender", ["F", "M"], default="F")
    added = st.form_submit_button("Add athlete", icon=":material/person_add:", disabled=done)

if added:
    if not team.strip():
        st.warning("Enter the team name first.", icon=":material/error:")
    elif not name.strip():
        st.warning("Enter the athlete's full name.", icon=":material/error:")
    elif not gender:
        st.warning("Choose F or M.", icon=":material/error:")
    else:
        roster.append(register_athlete(team.strip(), name.strip(), int(age), gender))
        st.toast(f"Added {name.strip()}", icon=":material/person_add:")
        st.rerun()

if roster:
    counts = roster_counts(roster)
    section("Roster", "groups", f"{counts['total']} athletes")
    stat_tiles([("Total", counts["total"], "groups"), ("Female", counts["female"], "female"), ("Male", counts["male"], "male")])
    result_table(
        ["#", "Athlete", "Age", "Gender", "Status"],
        [
            [
                str(i + 1),
                esc(n),
                str(a),
                f'<span class="neo-chip {"f" if g == "F" else "m"}">{esc(g)}</span>',
                f'<span class="neo-chip ok">{icon("check_circle")}Registered</span>'
                if r
                else f'<span class="neo-chip pending">{icon("schedule")}Pending</span>',
            ]
            for i, (_, n, a, g, r) in enumerate(roster)
        ],
    )

    finish_col, reset_col, _ = st.columns([1.3, 1, 2])
    if finish_col.button("Complete registration", type="primary", icon=":material/check_circle:", disabled=done):
        st.session_state.roster = finish_registration(roster)
        st.session_state.pop("heat", None)
        st.rerun()
    reset_col.button("Start over", icon=":material/restart_alt:", on_click=start_over)

    if done:
        banner(
            "success",
            f"{team} is registered",
            f"{counts['total']} athletes are ready. Their names now fill the Rankings heat.",
            "verified",
        )
else:
    empty_state("pool", "No athletes yet", "Add the first swimmer above, or load the Olympic sample team.")
