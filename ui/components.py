"""Small HTML building blocks styled by theme.css (classes start with neo-).

Everything a user typed goes through esc() before it reaches the page.
"""

from html import escape

import streamlit as st

MEDAL_CLASS = {"Gold": "gold", "Silver": "silver", "Bronze": "bronze"}


def esc(value) -> str:
    return escape(str(value))


def icon(name: str) -> str:
    return f'<span class="msr" aria-hidden="true">{esc(name)}</span>'


def hero(title: str, icon_name: str, summary: str, eyebrow: str = "Meet desk") -> None:
    st.html(
        f"""
        <section class="neo-hero">
          <div class="neo-badge">{icon(icon_name)}</div>
          <div class="neo-hero-text">
            <p class="eyebrow">{esc(eyebrow)}</p>
            <h1 class="neo-title">{esc(title)}</h1>
            <p class="lede">{esc(summary)}</p>
          </div>
        </section>
        """
    )


def steps(items: list[tuple[str, str]]) -> None:
    cards = "".join(
        f"""
        <div class="neo-step" style="--i:{i}">
          <span class="neo-step-n">{i + 1}</span>
          <div><p class="neo-step-title">{esc(label)}</p><p class="neo-step-text">{esc(text)}</p></div>
        </div>
        """
        for i, (label, text) in enumerate(items)
    )
    st.html(f'<div class="neo-steps">{cards}</div>')


def section(title: str, icon_name: str, note: str | None = None) -> None:
    extra = f'<span class="neo-section-note">{esc(note)}</span>' if note else ""
    st.html(f'<div class="neo-section">{icon(icon_name)}<h3>{esc(title)}</h3>{extra}</div>')


def stat_tiles(stats: list[tuple[str, int, str]]) -> None:
    """Raised tiles whose numbers count up from zero. stats = (label, value, icon)."""
    tiles = "".join(
        f"""
        <div class="neo-stat" style="--i:{i}">
          <div class="neo-stat-icon">{icon(icon_name)}</div>
          <div>
            <p class="neo-stat-label">{esc(label)}</p>
            <p class="neo-stat-value"><span class="neo-count" style="--to:{int(value)}" aria-label="{int(value)}"></span></p>
          </div>
        </div>
        """
        for i, (label, value, icon_name) in enumerate(stats)
    )
    st.html(f'<div class="neo-stats">{tiles}</div>')


def medal_chip(medal: str) -> str:
    if not medal:
        return '<span class="neo-muted">—</span>'
    return f'<span class="neo-chip {MEDAL_CLASS.get(medal, "")}">{icon("workspace_premium")}{esc(medal)}</span>'


def podium(rows: list[dict], value_key: str, unit: str = "") -> None:
    """Gold in the middle, silver left, bronze right. rows are in finishing order."""
    top = rows[:3]
    if not top:
        return
    order = [(1, "silver", 108), (0, "gold", 150), (2, "bronze", 80)]
    blocks = []
    for delay, (index, tone, height) in enumerate(order):
        if index >= len(top):
            blocks.append('<div class="neo-pod empty"></div>')
            continue
        row = top[index]
        value = row[value_key]
        shown = f"{value:.2f}" if isinstance(value, float) else esc(value)
        blocks.append(
            f"""
            <div class="neo-pod {tone}" style="--h:{height}px;--d:{delay * 0.12:.2f}s">
              <div class="neo-pod-medal">{index + 1}</div>
              <p class="neo-pod-name">{esc(row["Athlete"])}</p>
              <p class="neo-pod-meta">{shown}{esc(unit)}</p>
              <div class="neo-pod-bar"><span></span></div>
            </div>
            """
        )
    st.html(f'<div class="neo-podium">{"".join(blocks)}</div>')


def result_table(columns: list[str], rows: list[list[str]], highlight: set[int] | None = None) -> None:
    """Rows slide in one after another. Cells are pre-built HTML, so escape text with esc()."""
    highlight = highlight or set()
    head = "".join(f"<span>{esc(c)}</span>" for c in columns)
    body = "".join(
        f'<div class="neo-row{" hot" if i in highlight else ""}" style="--i:{min(i, 14)}">'
        + "".join(f"<span>{cell}</span>" for cell in row)
        + "</div>"
        for i, row in enumerate(rows)
    )
    # First column is sized in CSS; the name column gets the most room.
    template = " ".join(["minmax(0, 2.2fr)"] + ["minmax(0, 1fr)"] * (len(columns) - 2))
    st.html(
        f'<div class="neo-table" style="--tpl:{template}">'
        f'<div class="neo-row head">{head}</div>{body}</div>'
    )


def banner(kind: str, title: str, text: str, icon_name: str) -> None:
    """kind: record, success, info, warning."""
    st.html(
        f"""
        <div class="neo-banner {esc(kind)}">
          <div class="neo-banner-icon">{icon(icon_name)}</div>
          <div><p class="neo-banner-title">{esc(title)}</p><p class="neo-banner-text">{esc(text)}</p></div>
        </div>
        """
    )


def empty_state(icon_name: str, title: str, text: str) -> None:
    st.html(
        f"""
        <div class="neo-empty">
          <div class="neo-empty-icon">{icon(icon_name)}</div>
          <p class="neo-empty-title">{esc(title)}</p>
          <p class="neo-empty-text">{esc(text)}</p>
        </div>
        """
    )
