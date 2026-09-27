# Swim Ranking

A small app for a swim meet: register a team, rank race times, assign points, check records, mark fouls, and split tied times.

The screens run in [Streamlit](https://streamlit.io/). The home page includes a Three.js lane with a freestyle swimmer. The meet rules live in `backend/` as plain Python scripts. Every screen calls those functions through `ui/meet.py`, and each script still runs on its own from the command line.

## Features

| Screen | What it does |
| --- | --- |
| Team registration | Add a team and its athletes, then count female and male swimmers |
| Rankings | Sort swimmers by time and assign Gold, Silver, and Bronze |
| Points | Award points by place: 15, 7, 5, 3, 2, 1 |
| Records | Compare a time with the record for that age group |
| Fouls | Move a fouled athlete to last and mark them DQ |
| Tied times | Split points when two athletes finish with the same time |

## Project structure

```text
SwimRankingApp/
├── backend/                  # meet rules (Python scripts)
│   ├── home.py               # team registration, command line
│   ├── func1teaminput.py
│   ├── func2sort.py
│   ├── func3pointdistri.py
│   ├── func4recordbrk.py
│   ├── func5fouls.py
│   └── func6idenTime.py
├── ui/                       # Streamlit app
│   ├── app.py                # navigation
│   ├── meet.py               # calls the backend functions
│   ├── pool.html             # Three.js lane
│   └── views/                # one file per screen
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or newer
- A terminal opened in this folder

Check Python:

```powershell
python --version
```

## First-time setup

Do this once, before the first run.

**1. Create a virtual environment**

```powershell
python -m venv .venv
```

**2. Activate it**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**3. Install dependencies**

```powershell
python -m pip install -r requirements.txt
```

That installs Streamlit `1.64.0` from `requirements.txt`. The `backend/` scripts use only the Python standard library.

macOS and Linux use the same three steps, with a different activate command:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the app

From this folder, with the virtual environment activated:

```powershell
python -m streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501). The home page lists every screen. Use the sidebar to switch between them.

Stop the app with `Ctrl+C` in the terminal.

## Run a command-line script

The original scripts still run on their own. Start them from `backend/`, because `home.py` imports `func1teaminput.py` from that same folder.

```powershell
cd backend
python home.py
```

| Script | Run it for |
| --- | --- |
| `home.py` | Team registration |
| `func2sort.py` | Rankings and medals |
| `func3pointdistri.py` | Point distribution |
| `func4recordbrk.py` | Record check |
| `func5fouls.py` | Fouls |
| `func6idenTime.py` | Tied times |

Return to the project folder before starting Streamlit again:

```powershell
cd ..
python -m streamlit run ui/app.py
```
