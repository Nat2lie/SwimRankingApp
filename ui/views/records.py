import streamlit as st

from components import banner, esc, icon, section
from meet import AGE_GROUPS, DEFAULT_RECORDS, age_group_index, check_record
from pageshell import open_screen
from sample_data import OLYMPIANS, SAMPLE_NOTE, age as age_of

open_screen(
    "Records",
    "material/timer",
    "Compare a swim with the record held by that age group.",
    [
        ("Age groups", "8–9, 10–11, 12–13, 14–15, and 16 and over."),
        ("Check", "A lower time than the record for that group is a new record."),
        ("Marks", "The current marks start at 45.30, 39.60, 32.90, 30.40, and 27.89."),
    ],
)

records = st.session_state.setdefault("records", list(DEFAULT_RECORDS))
holders = st.session_state.setdefault("record_holders", [None] * len(DEFAULT_RECORDS))

section("Check a swim", "timer")
picked = st.selectbox(
    "Fill from a sample swimmer",
    [None, *OLYMPIANS],
    format_func=lambda row: "Type your own" if row is None else f"{row[0]} ({row[1]})",
    help=SAMPLE_NOTE,
)
start_name, start_age, start_time = ("", 10, 40.0) if picked is None else (picked[0], age_of(picked[3]), picked[4])

with st.form("record_check", border=True):
    name_col, age_col, time_col = st.columns([3, 1, 1])
    name = name_col.text_input("Athlete name", value=start_name, placeholder="Full name")
    age = age_col.number_input("Age", min_value=8, max_value=99, value=start_age, step=1)
    time = time_col.number_input("Time (s)", min_value=0.01, value=start_time, step=0.01, format="%.2f")
    checked = st.form_submit_button("Check record", type="primary", icon=":material/timer:")

fresh = None
if checked:
    if not name.strip():
        st.warning("Enter the athlete's name.", icon=":material/error:")
    else:
        group = age_group_index(int(age))
        old_mark = records[group]
        updated, broken = check_record(name.strip(), int(age), float(time), records)
        st.session_state.records = records = updated
        if broken:
            holders[group] = name.strip()
            fresh = group
            banner(
                "record",
                "New record!",
                f"{name.strip()} swam {time:.2f} s in {AGE_GROUPS[group]}, beating {old_mark:.2f} s.",
                "military_tech",
            )
        else:
            banner("info", "No record this time", f"The {AGE_GROUPS[group]} mark stays at {old_mark:.2f} s.", "timer")

section("Current records", "military_tech")
cards = "".join(
    f"""
    <div class="neo-record{' fresh' if i == fresh else ''}{' changed' if mark != DEFAULT_RECORDS[i] else ''}" style="--i:{i}">
      <p class="neo-record-group">{esc(group)}</p>
      <p class="neo-record-mark">{mark:.2f}<small> s</small></p>
      <p class="neo-record-holder">{icon("person")}{esc(holders[i]) if holders[i] else "Meet record"}</p>
    </div>
    """
    for i, (group, mark) in enumerate(zip(AGE_GROUPS, records))
)
st.html(f'<div class="neo-records">{cards}</div>')

if records != DEFAULT_RECORDS and st.button("Reset records", icon=":material/restart_alt:"):
    st.session_state.records = list(DEFAULT_RECORDS)
    st.session_state.record_holders = [None] * len(DEFAULT_RECORDS)
    st.rerun()
