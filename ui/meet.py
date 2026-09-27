"""Bridge between the Streamlit screens and the meet rules in backend/.

The backend functions work on plain lists and change them in place, so every
wrapper here hands them a fresh copy and turns the result into rows for a table.
"""

import contextlib
import io
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parent.parent / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from func1teaminput import complete_registration, count_memperteam, team_detail  # noqa: E402
from func2sort import Medals, ranking  # noqa: E402
from func3pointdistri import point  # noqa: E402
from func4recordbrk import newrecord, record as DEFAULT_RECORDS  # noqa: E402
from func5fouls import fouls  # noqa: E402
from func6idenTime import identical_times  # noqa: E402

AGE_GROUPS = ["8–9", "10–11", "12–13", "14–15", "16 and over"]


def register_athlete(team: str, name: str, age: int, gender: str) -> tuple:
    return team_detail(team, name, age, gender, False)


def roster_counts(athletes: list[tuple]) -> dict[str, int]:
    total, female, male = count_memperteam(athletes)
    return {"total": total, "female": female, "male": male}


def finish_registration(athletes: list[tuple]) -> list[tuple]:
    done = complete_registration("y", False)
    return [team_detail(*athlete[:4], done) for athlete in athletes]


def rank_heat(swimmers: list[tuple[str, float]]) -> list[dict]:
    ordered = ranking([[name, time] for name, time in swimmers])
    return [
        {"Place": place, "Athlete": name, "Time": time, "Medal": Medals[place - 1] if place <= len(Medals) else ""}
        for place, (name, time) in enumerate(ordered, start=1)
    ]


def award_points(names_in_order: list[str]) -> list[dict]:
    scored = point([[name, 0] for name in names_in_order])
    return [{"Place": place, "Athlete": name, "Points": pts} for place, (name, pts) in enumerate(scored, start=1)]


def age_group_index(age: int) -> int | None:
    if age < 8:
        return None
    return min((age - 8) // 2, len(AGE_GROUPS) - 1)


def check_record(name: str, age: int, time: float, records: list[float]) -> tuple[list[float], bool]:
    # newrecord() announces a break with print(); capture it instead of writing to the server log.
    with contextlib.redirect_stdout(io.StringIO()) as announced:
        updated = newrecord([[name, age, time]], list(records))
    return updated, "New Record!" in announced.getvalue()


def apply_foul(results: list[tuple[str, float]], fouled: str) -> list[dict]:
    reordered = fouls(list(results), fouled)
    return [
        {"Place": place, "Athlete": name, "Result": "DQ" if name == fouled else f"{time:.2f}"}
        for place, (name, time) in enumerate(reordered, start=1)
    ]


def split_ties(swimmers: list[tuple[str, float]]) -> list[dict]:
    """Score a four-swimmer heat, sharing points between tied times (sorted first, as the backend expects)."""
    ordered = ranking([[name, time] for name, time in swimmers])
    results = identical_times([[name, time, 0] for name, time in ordered])

    # Same medal rule as the command-line version of func6idenTime.py.
    gold, silver, bronze = results[0][1], None, None
    rows = []
    for place, (name, time, pts) in enumerate(results, start=1):
        if time == gold:
            medal = "Gold"
        elif silver is None or time == silver:
            silver = time
            medal = "Silver"
        elif bronze is None or time == bronze:
            bronze = time
            medal = "Bronze"
        else:
            medal = ""
        rows.append({"Place": place, "Athlete": name, "Time": time, "Points": pts, "Medal": medal})
    return rows
