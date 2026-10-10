"""
mkdocs-macros-plugin hook file.

Macros, all reading from docs/_data/release_status.yml:
  data_available_widget()  -- compact per-source strip, unused currently but kept
  data_available_table()   -- full per-source detail table (GDC, PDC, IDC, GC, ICDC,
                               CTDC individually)
  latest_releases()        -- homepage summary box with two halves: the CDA data
                               release (the versioned, bundled dataset CDA publishes
                               once its ETL pipeline has pulled and harmonized ALL
                               individual data commons together) and the cdapython
                               code release (the Python package, on its own
                               independent schedule). Carries the "Full data release
                               history" link.

FRAMING NOTE: within a single CDA data release, extraction timing across sources is
uniform -- CDA pulls all of them together for that release. What varies, and what the
per-source table communicates, is how recently each upstream source itself last
published new data as of that pull. The 'extracted' field in release_status.yml means
the date a source's data was last updated upstream, as best CDA can tell -- not the
date CDA last pulled it.

Styling note: all HTML output uses plain hardcoded colors, not theme CSS variables, so
this renders identically regardless of which mkdocs theme is active.

Both cda_data_release and cdapython_release are read from release_status.yml as plain
manually-maintained entries (no live fetch) -- see the project's release PR checklist
for the manual-update steps this depends on.
"""

import yaml
from datetime import date, datetime
from pathlib import Path

DATA_PATH = Path(__file__).parent / "docs" / "_data" / "release_status.yml"

FRESH_DAYS = 30
STALE_DAYS = 120


def _load_data():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)


def _load_sources():
    return _load_data()["sources"]


def _load_cda_data_release():
    return _load_data().get("cda_data_release")


def _load_cdapython_release():
    return _load_data().get("cdapython_release")


def _update_status_for(src):
    release = str(src.get("release", "")).lower()
    if release in ("unassigned", "unknown", ""):
        return "unknown", "No release assigned yet"

    try:
        updated = datetime.strptime(src["extracted"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        return "unknown", "Unknown"

    age_days = (date.today() - updated).days
    if age_days <= FRESH_DAYS:
        return "fresh", "Recently updated by source"
    else:
        return "stale", f"{age_days}d since source update"


def define_env(env):
    """Required entry point for mkdocs-macros-plugin."""

    @env.macro
    def data_available_widget():
        sources = _load_sources()
        rows = []
        for src in sources:
            status_class, status_label = _update_status_for(src)
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
            'color:#777777;margin-bottom:6px;">Data available at CDA</div>'
            + "".join(rows)
            + ' <a href="/release_notes/data_updates/" style="font-size:0.85rem;">Full details →</a>'
            "</div>"
        )

    @env.macro
    def data_available_table():
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
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Source last updated</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Status</th>'
            "</tr></thead><tbody>"
        )
        rows = []
        for src in sources:
            status_class, status_label = _update_status_for(src)
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
            '<h3 style="margin-top:0;">📅 Data available at CDA, by source</h3>'
            '<p style="color:#555555;font-size:0.85rem;margin-bottom:16px;">'
            "These dates show how recently each <em>upstream source itself</em> last "
            "published new data as of CDA's most recent pull — not how recently CDA "
            "last checked.</p>"
            + header + "".join(rows) + "</tbody></table></div>"
        )

    @env.macro
    def latest_releases():
        cda_rel = _load_cda_data_release()
        code_rel = _load_cdapython_release()

        def half(emoji, title, rel, link, link_text):
            if not rel:
                return '<div style="flex:1;min-width:240px;"></div>'
            highlight_html = (
                f'<p style="color:#555555;font-size:0.9rem;margin-bottom:12px;">{rel["highlight"]}</p>'
                if rel.get("highlight") else ""
            )
            return (
                '<div style="flex:1;min-width:240px;">'
                f'<h3 style="margin-top:0;">{emoji} {title}</h3>'
                f'<p style="margin:0 0 4px;"><strong>Available {rel["date_display"]}</strong></p>'
                + highlight_html +
                f'<p style="margin:0;font-size:0.85rem;"><a href="{link}">{link_text}</a></p>'
                "</div>"
            )

        cda_half = half(
            "📦", "Latest CDA data release", cda_rel,
            "release_notes/data_updates/", "Full data release history →"
        )
        code_half = half(
            "🐍", "Latest cdapython release", code_rel,
            "release_notes/cdapython/", "Full code release history →"
        )

        return (
            '<div style="border:1px solid #d0d0d0;border-radius:12px;'
            'padding:20px 24px;margin:16px 0;display:flex;gap:32px;flex-wrap:wrap;">'
            + cda_half + code_half +
            "</div>"
        )
