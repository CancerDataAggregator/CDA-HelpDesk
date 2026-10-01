"""
mkdocs-macros-plugin hook file.
Save as main.py at your repo root (same level as mkdocs.yml), unless your
mkdocs.yml specifies a different `module_name` under the macros plugin config --
see the mkdocs.yml snippet for where this gets referenced.

Defines two macros, both reading from the same docs/_data/release_status.yml:
  {{ release_status_widget() }}   -- compact, for the homepage
  {{ release_status_table() }}    -- full detail, for the release notes page

Editing docs/_data/release_status.yml is the ONLY thing that should change
each release. Nothing in this file should need to change release-to-release.
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
            '<div style="padding:10px 14px;border:1px solid var(--md-default-fg-color--lightest);'
            'border-radius:8px;margin:16px 0;">'
            '<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;'
            'color:var(--md-default-fg-color--light);margin-bottom:6px;">Data currency</div>'
            + "".join(rows)
            + ' <a href="/release_notes/data_updates/" style="font-size:0.85rem;">Full details →</a>'
            "</div>"
        )

    @env.macro
    def release_status_table():
        sources = _load_sources()
        header = (
            "<table><thead><tr>"
            "<th>Source</th><th>Data release</th><th>API version</th>"
            "<th>Extracted</th><th>Status</th></tr></thead><tbody>"
        )
        rows = []
        for src in sources:
            status_class, status_label = _status_for(src)
            dot_color = {"fresh": "#1a7f37", "stale": "#9a6700", "unknown": "#cf222e"}[status_class]
            release_cell = (
                f'<a href="{src["link"]}" target="_blank" rel="noopener">{src["release"]}</a>'
                if src.get("link") else src["release"]
            )
            rows.append(
                "<tr>"
                f'<td><span style="display:inline-block;width:8px;height:8px;border-radius:50%;'
                f'background:{dot_color};margin-right:6px;"></span><strong>{src["name"]}</strong></td>'
                f"<td>{release_cell}</td>"
                f'<td>{src["api"]}</td>'
                f'<td>{src["extracted"]}</td>'
                f"<td>{status_label}</td>"
                "</tr>"
            )
        return header + "".join(rows) + "</tbody></table>"
