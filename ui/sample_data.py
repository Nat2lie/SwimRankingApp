"""Mock meet data for trying the screens.

The names, countries, genders, and birth years belong to real Olympic swimmers.
The 50 m freestyle times are made up for testing and are not official results.
"""

from datetime import date

SAMPLE_TEAM = "Olympic All-Stars"
SAMPLE_NOTE = "Names are real Olympic swimmers. Times are made up for testing, not official results."

# (name, country, gender, birth year, mock 50 m freestyle time in seconds)
OLYMPIANS = [
    ("Caeleb Dressel", "USA", "M", 1996, 21.41),
    ("Pan Zhanle", "CHN", "M", 2004, 21.62),
    ("Kyle Chalmers", "AUS", "M", 1998, 21.70),
    ("David Popovici", "ROU", "M", 2004, 21.88),
    ("Michael Phelps", "USA", "M", 1985, 22.05),
    ("Thomas Ceccon", "ITA", "M", 2001, 22.20),
    ("Léon Marchand", "FRA", "M", 2002, 22.31),
    ("Duncan Scott", "GBR", "M", 1997, 22.35),
    ("Ryan Murphy", "USA", "M", 1995, 22.48),
    ("Adam Peaty", "GBR", "M", 1994, 22.60),
    ("Sarah Sjöström", "SWE", "F", 1993, 23.71),
    ("Emma McKeon", "AUS", "F", 1994, 23.95),
    ("Mollie O'Callaghan", "AUS", "F", 2004, 24.10),
    ("Siobhán Haughey", "HKG", "F", 1997, 24.18),
    ("Torri Huske", "USA", "F", 2002, 24.22),
    ("Kaylee McKeown", "AUS", "F", 2001, 24.50),
    ("Regan Smith", "USA", "F", 2002, 24.62),
    ("Summer McIntosh", "CAN", "F", 2006, 24.75),
    ("Ariarne Titmus", "AUS", "F", 2000, 24.90),
    ("Katie Ledecky", "USA", "F", 1997, 25.30),
]


def age(birth_year: int) -> int:
    return date.today().year - birth_year


SAMPLE_HEAT = [(name, time) for name, _, _, _, time in OLYMPIANS]
SAMPLE_TIMES = dict(SAMPLE_HEAT)
