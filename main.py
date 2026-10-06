"""
mkdocs-macros-plugin hook file.
Save as main.py at your repo root (same level as mkdocs.yml), unless your
mkdocs.yml specifies a different `module_name` under the macros plugin config --
see the mkdocs.yml snippet for where this gets referenced.

Defines two macros, both reading from the same docs/_data/release_status.yml:
  {{ release_status_widget() }}   -- compact, unused on homepage currently but kept
                                      in case a future page wants the small version
  {{ release_status_table() }}    -- full detail, used on the homepage and release notes

Editing docs/_data/release_status.yml is the ONLY thing that should change
each release. Nothing in this file should need to change release-to-release.

Styling note: all HTML output uses plain hardcoded colors, NOT theme CSS variables
(e.g. NOT var(--md-default-fg-color--lightest)), so this renders identically
regardless of which mkdocs theme is active.
"""

import yaml
from datetime import date, datetime
from pathlib import Path

DATA_PATH = Path(__file__).parent / "docs" / "_data" / "release_status.yml"

FRESH_DAYS = 30
STALE_DAYS = 120


def _load_sources():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)["sources"]


def _status_for(src):
    release = str(src.get("release", "")).lower()
    if release in ("unassigned", "unknown", ""):
        return "unknown", "Unassigned"

    try:
        extracted = datetime.strptime(src["extracted"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        return "unknown", "Unknown"

    age_days = (date.today() - extracted).days
    if age_days <= FRESH_DAYS:
        return "fresh", "Recently extracted"
    else:
        return "stale", f"{age_days}d since extraction"


def define_env(env):
    """Required entry point for mkdocs-macros-plugin."""

    @env.macro
    def release_status_widget():
        sources = _load_sources()
        rows = []
        for src in sources:
            status_class, status_label = _status_for(src)
            dot_color = {"fresh": "#1a7f37", "stale": "#9a6700", "unknown": "#cf222e"}[status_class]
            rows.append(
                f'<span title="{src["name"]}: {status_label}" style="display:inline-flex;align-items:center;gap:4px;margin-right:14px;font-size:0.85rem;">'
                f'<span style="width:8px;height:8px;border-radius:50%;background:{dot_color};display:inline-block;"></span>'
                f'<strong>{src["name"]}</strong></span>'
            )
        return (
            '<div style="padding:10px 14px;border:1px solid #d0d0d0;'
            'border-radius:8px;margin:16px 0;">'
            '<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;'
            'color:#777777;margin-bottom:6px;">Data currency</div>'
            + "".join(rows)
            + ' <a href="/release_notes/data_updates/" style="font-size:0.85rem;">Full details →</a>'
            "</div>"
        )

    @env.macro
    def release_status_table():
        sources = _load_sources()
        status_colors = {
            "fresh":   {"bg": "rgba(52,211,153,0.15)",  "text": "#1a7f37", "dot": "#1a7f37"},
            "stale":   {"bg": "rgba(251,191,36,0.18)",  "text": "#9a6700", "dot": "#9a6700"},
            "unknown": {"bg": "rgba(248,113,113,0.18)", "text": "#cf222e", "dot": "#cf222e"},
        }
        header = (
            '<table style="width:100%;border-collapse:collapse;font-size:0.9rem;">'
            "<thead><tr>"
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Source</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Data release</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">API version</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Extracted</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Status</th>'
            "</tr></thead><tbody>"
        )
        rows = []
        for src in sources:
            status_class, status_label = _status_for(src)
            colors = status_colors[status_class]
            release_cell = (
                f'<a href="{src["link"]}" target="_blank" rel="noopener">{src["release"]}</a>'
                if src.get("link") else src["release"]
            )
            rows.append(
                '<tr style="border-bottom:1px solid #e5e5e5;">'
                f'<td style="padding:10px 12px;"><span style="display:inline-block;width:8px;height:8px;'
                f'border-radius:50%;background:{colors["dot"]};margin-right:8px;"></span><strong>{src["name"]}</strong></td>'
                f'<td style="padding:10px 12px;">{release_cell}</td>'
                f'<td style="padding:10px 12px;">{src["api"]}</td>'
                f'<td style="padding:10px 12px;">{src["extracted"]}</td>'
                f'<td style="padding:10px 12px;"><span style="display:inline-block;padding:3px 12px;'
                f'border-radius:999px;font-size:0.78rem;font-weight:700;background:{colors["bg"]};'
                f'color:{colors["text"]};">{status_label}</span></td>'
                "</tr>"
            )
        return (
            '<div style="border:1px solid #d0d0d0;border-radius:12px;'
            'padding:20px 24px;margin:16px 0;">'
            '<h3 style="margin-top:0;">📅 Data currency</h3>'
            '<p style="color:#555555;font-size:0.85rem;margin-bottom:16px;">'
            "How recently each underlying source was refreshed — updated with each CDA release.</p>"
            + header + "".join(rows) + "</tbody></table></div>"
        )
