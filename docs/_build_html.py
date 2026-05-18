"""
Build the SPMD Minor → Fall 2027 ADEK Roadmap self-contained HTML page.

Reads  ../_data.json
Writes docs/SPMD_Fall2027_Roadmap.html

Self-contained: all CSS inline, no external assets, Arial/sans-serif fonts.
Prints cleanly from browser. No CDN dependencies.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_PATH = HERE.parent / "_data.json"
OUT_PATH = HERE / "SPMD_Fall2027_Roadmap.html"

GEN_DATE = "2026-05-18"
FOOTER_TEXT = "BSCND Sports Medicine Roadmap · Fall 2027 · Generated 2026-05-18 · ADEK-aligned"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def esc(val) -> str:
    if val is None:
        return ""
    return html.escape(str(val), quote=True)


def proposed_badge() -> str:
    return '<span style="background:#D97706;color:#fff;padding:2px 10px;border-radius:4px;font-size:12px;font-weight:700;letter-spacing:0.04em;">PROPOSED — pending faculty validation</span>'


# ---------------------------------------------------------------------------
# CSS (inline, no external fonts)
# ---------------------------------------------------------------------------

CSS = """
:root {
  --navy: #003D7A;
  --navy-dark: #002551;
  --gold: #C8A04A;
  --gold-light: #E8D08A;
  --amber: #D97706;
  --amber-bg: #FFF7ED;
  --green: #1B8A4E;
  --ink: #1F2937;
  --grey-50: #F9FAFB;
  --grey-100: #F3F4F6;
  --grey-200: #E5E7EB;
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0;
  font-family: Arial, sans-serif;
  color: var(--ink);
  background: #fff;
  line-height: 1.5;
}
a { color: var(--navy); text-decoration: none; }
a:hover { text-decoration: underline; }

/* Header */
.header-band {
  background: var(--navy);
  border-bottom: 3px solid var(--gold);
}
.header-eyebrow {
  padding: 8px 32px;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  color: #fff;
  border-bottom: 2px solid var(--gold);
}
.header-titles { padding: 16px 32px 20px; }
.header-title { font-size: 24px; font-weight: 700; margin: 0; color: #fff; }
.header-subtitle { font-size: 14px; color: var(--gold-light); margin: 4px 0 0; }

/* Nav */
.site-nav {
  background: var(--navy-dark);
  border-bottom: 1px solid rgba(255,255,255,0.1);
  position: sticky; top: 0; z-index: 40;
}
.site-nav ul {
  list-style: none; margin: 0; padding: 0 24px;
  display: flex; gap: 2px; overflow-x: auto;
}
.site-nav li { flex: 0 0 auto; }
.site-nav a {
  display: inline-block; padding: 11px 14px;
  color: #fff; font-size: 12px; font-weight: 700;
  letter-spacing: 0.05em; text-transform: uppercase;
  border-bottom: 3px solid transparent;
}
.site-nav a:hover { color: var(--gold-light); text-decoration: none; }
.site-nav a.active { border-bottom-color: var(--gold); color: var(--gold-light); }

/* Main */
main { max-width: 1200px; margin: 0 auto; padding: 32px 28px 80px; }
section { margin-bottom: 52px; scroll-margin-top: 130px; }

h2.sec { color: var(--navy); border-left: 3px solid var(--gold);
  padding: 4px 0 4px 14px; font-size: 22px; font-weight: 700; margin: 0 0 18px; }
h3.sub { color: var(--navy); font-size: 16px; font-weight: 700; margin: 24px 0 10px; }

/* Cards */
.card { background: #fff; border: 1px solid var(--grey-200);
  border-radius: 8px; padding: 22px; margin-bottom: 14px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06); }

/* Banners */
.banner { border-radius: 6px; padding: 12px 16px; margin: 10px 0;
  font-size: 13px; border-left: 4px solid; }
.banner-navy { background: #EFF6FF; border-color: var(--navy); color: var(--navy-dark); }
.banner-amber { background: var(--amber-bg); border-color: var(--amber); color: #92400E; }
.banner-green { background: #ECFDF5; border-color: var(--green); color: #065F46; }

/* Tables */
.tbl-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
thead th { background: var(--navy); color: #fff; font-weight: 700;
  text-align: left; padding: 10px 12px; border: 1px solid var(--navy);
  font-size: 12px; letter-spacing: 0.03em; }
tbody td { padding: 10px 12px; border: 1px solid var(--grey-200); vertical-align: top; }
tbody tr:nth-child(even) td { background: var(--grey-50); }
tbody tr.proposed td { background: var(--amber-bg); }
tbody tr.proposed:nth-child(even) td { background: #FFE8C8; }
.col-code { font-weight: 700; color: var(--navy); white-space: nowrap; }
.col-center { text-align: center; }

/* Pill / badge */
.pill { display: inline-block; padding: 2px 9px; border-radius: 999px;
  font-size: 11px; font-weight: 700; white-space: nowrap; }
.pill-amber { background: #FFEDD5; color: #9A3412; }
.pill-navy { background: #DBEAFE; color: #1E3A8A; }
.pill-green { background: #DCFCE7; color: #065F46; }

/* Heatmap */
.hm td { text-align: center; min-width: 48px; font-weight: 700; }
.hm .dot { background: var(--navy); color: #fff; }
.hm .empty { background: var(--grey-100); color: #9CA3AF; }

/* Roadmap grid */
.roadmap-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0;
  border: 1px solid var(--grey-200); border-radius: 8px; overflow: hidden; }
.rg-header { background: var(--navy); color: #fff; font-weight: 700;
  font-size: 12px; padding: 10px 12px; text-align: center;
  letter-spacing: 0.04em; text-transform: uppercase; }
.rg-cell { padding: 10px 12px; border-right: 1px solid var(--grey-200);
  border-bottom: 1px solid var(--grey-200); font-size: 12px; }
.rg-cell:nth-child(5n) { border-right: none; }
.rg-q { font-weight: 700; color: var(--navy); font-size: 13px; }
.rg-minor { border-left: 3px solid var(--navy); padding-left: 9px; }
.rg-conc { border-left: 3px solid var(--gold); padding-left: 9px; }
.rg-gate { font-style: italic; color: #374151; font-size: 11px; }
.rg-launch { background: var(--amber-bg); }
.rg-launch .rg-q { color: var(--amber); }

/* Course cards */
.course-card { border: 1px solid var(--grey-200); border-radius: 8px;
  margin-bottom: 20px; overflow: hidden; }
.course-card-head { background: var(--navy); color: #fff; padding: 12px 18px; }
.course-card-head.proposed { background: var(--amber); }
.course-card-title { font-size: 16px; font-weight: 700; margin: 0; }
.course-card-meta { font-size: 12px; opacity: 0.85; margin: 4px 0 0; }
.course-card-body { padding: 16px 18px; }
.course-meta-grid { display: grid; grid-template-columns: 140px 1fr; gap: 4px 12px;
  font-size: 13px; margin-bottom: 14px; }
.course-meta-label { font-weight: 700; color: var(--navy); }
.clo-list { padding-left: 18px; margin: 0; font-size: 13px; }
.clo-list li { margin-bottom: 4px; }

/* Footer */
.site-footer { background: var(--navy); color: #fff; text-align: center;
  padding: 16px 24px; font-size: 12px; border-top: 3px solid var(--gold); }
.site-footer .dot { color: var(--gold-light); margin: 0 6px; }

/* Print */
@media print {
  .site-nav { display: none !important; }
  .header-band { position: static; }
  section { page-break-after: always; }
  table { font-size: 11px; }
  thead th { background: var(--navy) !important; -webkit-print-color-adjust: exact;
    print-color-adjust: exact; color: #fff !important; }
  .hm .dot { background: var(--navy) !important; -webkit-print-color-adjust: exact;
    print-color-adjust: exact; }
  body { font-size: 12px; }
  .card { box-shadow: none; }
}
@media (max-width: 800px) {
  .roadmap-grid { grid-template-columns: 1fr 1fr; }
  main { padding: 20px 14px 60px; }
  .header-titles { padding: 12px 18px 16px; }
  .header-title { font-size: 20px; }
}
"""

# ---------------------------------------------------------------------------
# JS (minimal — nav active-section, no external deps)
# ---------------------------------------------------------------------------

JS = r"""
(function() {
  var links = document.querySelectorAll('.site-nav a[data-anchor]');
  if (!links.length) return;
  var byAnchor = {};
  links.forEach(function(a) { byAnchor[a.dataset.anchor] = a; });
  var secs = Array.prototype.slice.call(links).map(function(a) {
    return document.getElementById(a.dataset.anchor);
  }).filter(Boolean);
  function setActive(id) {
    links.forEach(function(a) { a.classList.remove('active'); });
    if (byAnchor[id]) byAnchor[id].classList.add('active');
  }
  var io = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) { if (e.isIntersecting) setActive(e.target.id); });
  }, { rootMargin: '-120px 0px -55% 0px', threshold: 0 });
  secs.forEach(function(s) { io.observe(s); });
  if (secs.length) setActive(secs[0].id);
})();
"""


# ---------------------------------------------------------------------------
# Render helpers
# ---------------------------------------------------------------------------

def render_header() -> str:
    return """
<header class="header-band">
  <div class="header-eyebrow">Khalifa University &middot; College of Medicine and Health Sciences &middot; ADEK Submission</div>
  <div class="header-titles">
    <h1 class="header-title">SPMD Minor &rarr; Fall 2027 ADEK Roadmap</h1>
    <div class="header-subtitle">BSc Clinical Nutrition &amp; Dietetics &mdash; QF Emirates Level 6 &mdash; Prepared by Dr. Carlo Raj</div>
  </div>
</header>
"""


def render_nav() -> str:
    items = [
        ("cover", "Cover"),
        ("exec-summary", "Executive Summary"),
        ("tracks", "Track Structure"),
        ("courses", "Course Catalogue"),
        ("roadmap", "Roadmap Matrix"),
        ("regulators", "Regulators"),
        ("plo-clo", "PLO×CLO"),
        ("data-issues", "Data Issues"),
        ("appendix", "Appendix A"),
    ]
    lis = "\n".join(
        f'    <li><a href="#{a}" data-anchor="{a}">{esc(label)}</a></li>'
        for a, label in items
    )
    return f'<nav class="site-nav" aria-label="Section navigation"><ul>\n{lis}\n</ul></nav>'


def render_cover(data: dict) -> str:
    prog = data["program"]
    meta = [
        ("Programme", prog["full_name"]),
        ("Institution", prog["institution"]),
        ("College", prog["college"]),
        ("Target Launch", prog["launch"]),
        ("QF Emirates Level", str(data["qfemirates_level"])),
        ("Baseline Credits", str(prog["total_credits_baseline"])),
        ("Credits with Concentration", str(prog["total_credits_with_concentration"])),
        ("Date", GEN_DATE),
        ("Prepared by", "Dr. Carlo Raj"),
        ("Audience", "ADEK Reviewers"),
    ]
    rows = "\n".join(
        f'<tr><td style="font-weight:700;color:var(--navy);padding:8px 12px;border:1px solid var(--grey-200);background:var(--grey-50);white-space:nowrap;">{esc(k)}</td>'
        f'<td style="padding:8px 12px;border:1px solid var(--grey-200);">{esc(v)}</td></tr>'
        for k, v in meta
    )
    return f"""
<section id="cover">
  <h2 class="sec">Programme Cover Sheet</h2>
  <div class="card">
    <div class="tbl-wrap">
      <table style="width:auto;min-width:400px;">
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
  <div class="banner banner-navy">
    <strong>Document purpose:</strong> ADEK Programme Authorization submission supporting the Sports Medicine Minor (SPMD 301&ndash;304) and Sports &amp; Fitness Coaching Concentration (SPMD 305&ndash;308) within the BSCND at Khalifa University CMHS.
  </div>
  <div class="banner banner-amber">
    <strong>Note:</strong> SPMD 305&ndash;308 courses are PROPOSED &mdash; syllabi not yet authored. Data is inferred from the ICREPs Level 3 PT gap analysis and is pending faculty validation before UGCC submission.
  </div>
</section>
"""


def render_exec_summary(data: dict) -> str:
    return f"""
<section id="exec-summary">
  <h2 class="sec">Executive Summary</h2>
  <div class="card">
    <h3 class="sub" style="margin-top:0;">Two-Track Approach</h3>
    <p style="font-size:14px;margin:0 0 12px;">
      This roadmap presents a dual-track strategy for delivering sports medicine content within the
      BSCND. <strong>Track 1</strong> (SPMD 301&ndash;304: Sports Medicine Minor, 12 credits) consolidates
      four existing syllabi awaiting UGCC review. <strong>Track 2</strong> (SPMD 305&ndash;308: Sports &amp;
      Fitness Coaching Concentration, 12 credits) introduces four new courses proposed in May 2026 in
      response to CMHS Dean Dr. Habiba Alsafar&rsquo;s inquiry, closing all ICREPs Level 3 PT
      competency gaps and enabling REPs UAE Personal Trainer registration for graduates.
    </p>
    <h3 class="sub">Fall 2027 Launch Window</h3>
    <p style="font-size:14px;margin:0 0 12px;">
      Five-quarter implementation plan (Q3 2026 &ndash; Q3 2027). First classes offered September 2027.
      Key governance gates: UGCC bundled submission (Q3 2026), ADEK Program Authorization for the minor
      (Q4 2026), MoHESR filing (Q1 2027), KU Senate/Board approval (Q2 2027), Go-Live (Q3 2027).
    </p>
    <h3 class="sub">Regulator Alignment</h3>
    <p style="font-size:14px;margin:0;">
      Aligned to six UAE regulatory bodies: REPs UAE (primary professional registration, mandatory UAE
      gym employment), ADSC and DSC (emirate-level enforcement), GAS (federal strategic framework),
      DoH Abu Dhabi (parallel Dietitian licence pathway), and MoHRE (commercial employment compliance).
      REPs UAE / ADSC alignment letters targeted for Q3 2027 Go-Live gate.
    </p>
  </div>
</section>
"""


def render_tracks(data: dict) -> str:
    tracks = sorted(data["tracks"], key=lambda t: t["id"])
    cards = []
    for track in tracks:
        is_conc = track["id"] == "concentration"
        border_color = "var(--gold)" if is_conc else "var(--navy)"
        label = "Track 2 — Sports &amp; Fitness Coaching Concentration (SPMD 305&ndash;308)" if is_conc \
            else "Track 1 — Sports Medicine Minor (SPMD 301&ndash;304)"
        icreps = ('<span class="pill pill-green">ICREPs Level 3 PT eligible</span>'
                  if track.get("icreps_eligible")
                  else '<span class="pill pill-navy">Didactic — no fitness-coach credential</span>')
        cards.append(f"""
  <div class="card" style="border-left:4px solid {border_color};">
    <h3 class="sub" style="margin-top:0;">{label}</h3>
    <div class="course-meta-grid">
      <span class="course-meta-label">Courses</span><span>{esc(", ".join(track["courses"]))}</span>
      <span class="course-meta-label">Credits</span><span>{esc(str(track["credits_total"]))}</span>
      <span class="course-meta-label">Status</span><span><span class="pill pill-amber">{esc(track["status"])}</span></span>
      <span class="course-meta-label">REPs eligibility</span><span>{icreps}</span>
    </div>
    <p style="font-size:13px;color:#4B5563;margin:0;">{esc(track["note"])}</p>
  </div>
""")

    # Side-by-side comparison table
    cmp_rows = [
        ("Course codes", "SPMD 301, 302, 303, 304", "SPMD 305, 306, 307, 308"),
        ("Credits", "12", "12"),
        ("Level", "300-level", "300–400 level"),
        ("Target student", "Nutrition students — sports science depth; athlete-centred",
         "Nutrition students targeting REPs UAE PT / GFI registration"),
        ("ICREPs Level 3 PT pathway", "No", "Yes"),
        ("Governance status", "Pending UGCC review", "Proposed — syllabi not yet authored"),
    ]
    cmp_html = "".join(
        f"<tr><td style='font-weight:700;color:var(--navy);'>{esc(r[0])}</td>"
        f"<td>{esc(r[1])}</td><td>{esc(r[2])}</td></tr>"
        for r in cmp_rows
    )

    return f"""
<section id="tracks">
  <h2 class="sec">Two-Track Programme Structure</h2>
  {"".join(cards)}
  <h3 class="sub">Side-by-Side Comparison</h3>
  <div class="card" style="padding:0;overflow:hidden;">
    <div class="tbl-wrap">
      <table>
        <thead><tr><th>Attribute</th><th>Minor (SPMD 301&ndash;304)</th><th>Concentration (SPMD 305&ndash;308)</th></tr></thead>
        <tbody>{cmp_html}</tbody>
      </table>
    </div>
  </div>
</section>
"""


def render_courses(data: dict) -> str:
    courses = data["courses"]
    plos_map = {p["id"]: p["label"] for p in data["bscnd_plos"]}
    blocks = []

    for code in sorted(courses.keys()):
        c = courses[code]
        is_inferred = c.get("_inferred", False)
        head_class = "course-card-head proposed" if is_inferred else "course-card-head"
        prereqs = "; ".join(c.get("prerequisites", [])) or "None"
        if c.get("prerequisite_note"):
            prereqs += f" [{c['prerequisite_note']}]"
        track_label = "Concentration" if c["track"] == "concentration" else "Minor"
        icreps = f'<div class="course-meta-label">ICREPs alignment</div><div>{esc(c["icreps_alignment"])}</div>' \
            if c.get("icreps_alignment") else ""
        embedded = f'<div class="course-meta-label">Embedded certs</div><div>{esc(", ".join(c["embedded_certifications"]))}</div>' \
            if c.get("embedded_certifications") else ""

        plo_pills = " ".join(
            f'<span class="pill pill-navy">{esc(pid)}</span>' for pid in sorted(c.get("plos", []))
        )
        gelo_pills = " ".join(
            f'<span class="pill" style="background:var(--grey-100);color:var(--ink);">{esc(g)}</span>'
            for g in c.get("ku_gelo", [])
        )
        clo_items = "\n".join(f"<li>{esc(clo)}</li>" for clo in c.get("clos", []))
        proposed_tag = proposed_badge() if is_inferred else ""
        inference_note = (f'<p style="font-size:11px;color:var(--amber);margin:8px 0 0;">'
                          f'<strong>Inference note:</strong> {esc(c["_inference_note"])}</p>'
                          if is_inferred and c.get("_inference_note") else "")

        blocks.append(f"""
  <div class="course-card">
    <div class="{head_class}">
      <p class="course-card-title">{esc(code)}: {esc(c["title"])}</p>
      <p class="course-card-meta">{esc(track_label)} &middot; {esc(c.get("semester",""))} &middot; {esc(str(c["credits"]))} credits &middot; Level {esc(str(c.get("level","")))} {proposed_tag}</p>
    </div>
    <div class="course-card-body">
      <div class="course-meta-grid">
        <div class="course-meta-label">Prerequisites</div><div style="font-size:12px;">{esc(prereqs)}</div>
        <div class="course-meta-label">Status</div><div>{esc(c.get("status",""))}</div>
        {icreps}
        {embedded}
        <div class="course-meta-label">PLOs</div><div>{plo_pills}</div>
        <div class="course-meta-label">KU GELOs</div><div>{gelo_pills}</div>
      </div>
      <p style="font-size:13px;margin:0 0 12px;">{esc(c.get("description",""))}</p>
      <strong style="font-size:13px;color:var(--navy);">Course Learning Outcomes (CLOs)</strong>
      <ol class="clo-list">{clo_items}</ol>
      {inference_note}
    </div>
  </div>
""")

    return f"""
<section id="courses">
  <h2 class="sec">Course Catalogue &mdash; SPMD 301&ndash;308</h2>
  <div class="banner banner-amber" style="margin-bottom:18px;">
    <strong>PROPOSED courses (SPMD 305&ndash;308):</strong> Header shown in amber. CLOs and PLO mappings are inferred and require faculty validation before UGCC submission.
  </div>
  {"".join(blocks)}
</section>
"""


def render_roadmap(data: dict) -> str:
    phases = data["phases"]
    cells = []
    # Headers
    for h in ["Quarter", "Minor Track Deliverable", "Concentration Track Deliverable",
               "Governance Gate", "Owner / Decision-Maker"]:
        cells.append(f'<div class="rg-header">{esc(h)}</div>')

    for phase in phases:
        is_launch = phase["q"] == "Q3 2027"
        cls = "rg-cell rg-launch" if is_launch else "rg-cell"
        cells.append(f'<div class="{cls} rg-q">{esc(phase["q"])}<br><small style="font-weight:400;font-size:11px;">{esc(phase["date_range"])}</small></div>')
        cells.append(f'<div class="{cls} rg-minor">{esc(phase["deliverables"]["minor"])}</div>')
        cells.append(f'<div class="{cls} rg-conc">{esc(phase["deliverables"]["concentration"])}</div>')
        cells.append(f'<div class="{cls} rg-gate">{esc(phase["gate"])}</div>')
        cells.append(f'<div class="{cls}" style="font-size:11px;"><strong>{esc(phase["owner"])}</strong><br>Decision: {esc(phase["decision_maker"])}</div>')

    grid_html = "\n".join(cells)

    # Key actions
    ka_rows = []
    for phase in phases:
        for action in phase.get("key_actions", []):
            ka_rows.append(
                f'<tr><td class="col-code">{esc(phase["q"])}</td>'
                f'<td style="font-size:12px;">{esc(action)}</td></tr>'
            )
    ka_table = f"""
<div class="tbl-wrap" style="margin-top:20px;">
  <table>
    <thead><tr><th>Quarter</th><th>Key Action</th></tr></thead>
    <tbody>{"".join(ka_rows)}</tbody>
  </table>
</div>
"""

    return f"""
<section id="roadmap">
  <h2 class="sec">Quarter &times; Track &times; Gate Roadmap Matrix</h2>
  <p style="font-size:13px;color:#4B5563;margin:-8px 0 16px;">Five-quarter implementation plan Q3 2026 &ndash; Q3 2027. Q3 2027 (Go-Live) is highlighted in amber.</p>
  <div class="roadmap-grid">
{grid_html}
  </div>
  <h3 class="sub">Key Actions by Quarter</h3>
  {ka_table}
</section>
"""


def render_regulators(data: dict) -> str:
    regulators = data["regulators"]
    conc_codes = sorted(["SPMD305", "SPMD306", "SPMD307", "SPMD308"])

    th_codes = "".join(f"<th>{esc(c)}</th>" for c in conc_codes)
    rows = []
    for reg_key in sorted(regulators.keys()):
        reg = regulators[reg_key]
        alignment = reg.get("alignment", {})
        tier = reg.get("tier", "")
        tier_pill = ""
        if "Tier 1" in tier:
            tier_pill = '<span class="pill pill-green">Tier 1</span>'
        elif "Tier 2" in tier:
            tier_pill = '<span class="pill pill-navy">Tier 2</span>'
        else:
            tier_pill = '<span class="pill" style="background:var(--grey-100);">Tier 3</span>'

        align_cells = ""
        for code in conc_codes:
            align_text = alignment.get(code, "")
            if align_text:
                align_cells += f'<td style="font-size:11px;">{esc(align_text)}</td>'
            else:
                align_cells += '<td style="text-align:center;color:#9CA3AF;">—</td>'

        rows.append(
            f'<tr><td class="col-code">{esc(reg_key)}</td>'
            f'<td style="font-size:12px;"><strong>{esc(reg.get("full_name",""))}</strong><br>'
            f'<span style="font-size:11px;color:#4B5563;">{esc(reg.get("name_ar",""))}</span></td>'
            f'<td>{tier_pill}</td>'
            f'{align_cells}</tr>'
        )

    return f"""
<section id="regulators">
  <h2 class="sec">Regulator Alignment Matrix</h2>
  <p style="font-size:13px;color:#4B5563;margin:-8px 0 14px;">
    The concentration courses (SPMD 305&ndash;308) carry direct UAE professional-registration relevance.
    The Sports Medicine Minor (SPMD 301&ndash;304) provides foundational knowledge but does not confer
    fitness-coach credentials.
  </p>
  <div class="card" style="padding:0;overflow:hidden;">
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Regulator</th>
            <th>Full Name / Arabic</th>
            <th>Tier</th>
            {th_codes}
          </tr>
        </thead>
        <tbody>{"".join(rows)}</tbody>
      </table>
    </div>
  </div>
</section>
"""


def render_plo_clo(data: dict) -> str:
    courses = data["courses"]
    plos = data["bscnd_plos"]
    plo_ids = [p["id"] for p in plos]

    # PLO definitions card
    plo_cards = "\n".join(
        f'<div style="background:var(--grey-50);border-left:4px solid var(--gold);padding:12px 14px;border-radius:6px;">'
        f'<strong style="color:var(--navy);">{esc(p["id"])}</strong> &mdash; {esc(p["label"])}'
        f'<br><span style="font-size:12px;color:#374151;">{esc(p["description"])}</span>'
        f'<br><span style="font-size:11px;background:var(--navy);color:#fff;padding:1px 8px;border-radius:999px;">QF: {esc(p.get("qf_emirates_alignment",""))}</span>'
        f'</div>'
        for p in plos
    )

    tables = []
    for code in sorted(courses.keys()):
        c = courses[code]
        is_inferred = c.get("_inferred", False)
        course_plos = set(c.get("plos", []))
        clos = c.get("clos", [])

        head_style = (
            "background:var(--amber);color:#fff;" if is_inferred
            else "background:var(--navy);color:#fff;"
        )
        proposed_tag = " [PROPOSED — pending faculty validation]" if is_inferred else ""

        th_plo = "".join(f"<th style='min-width:48px;text-align:center;'>{esc(pid)}</th>" for pid in plo_ids)
        trs = []
        for clo in clos:
            dots = "".join(
                '<td class="dot" style="text-align:center;font-size:14px;">&#9679;</td>'
                if pid in course_plos else
                '<td class="empty" style="text-align:center;color:#9CA3AF;background:var(--grey-100);">&mdash;</td>'
                for pid in plo_ids
            )
            trs.append(f'<tr><td style="font-size:11px;">{esc(clo)}</td>{dots}</tr>')

        tables.append(f"""
  <div style="margin-bottom:24px;">
    <div style="{head_style}padding:10px 16px;border-radius:8px 8px 0 0;font-weight:700;font-size:14px;">
      {esc(code)}: {esc(c["title"])}{esc(proposed_tag)}
    </div>
    <div style="border:1px solid var(--grey-200);border-top:none;border-radius:0 0 8px 8px;overflow:hidden;">
      <div class="tbl-wrap">
        <table class="hm">
          <thead><tr><th style="text-align:left;min-width:300px;">CLO</th>{th_plo}</tr></thead>
          <tbody>{"".join(trs)}</tbody>
        </table>
      </div>
      <div style="padding:8px 14px;font-size:11px;color:#4B5563;border-top:1px solid var(--grey-200);">
        PLOs addressed: <strong>{esc(", ".join(sorted(course_plos)))}</strong>
        &nbsp;&middot;&nbsp; KU GELOs: {esc(", ".join(c.get("ku_gelo", [])))}
      </div>
    </div>
  </div>
""")

    return f"""
<section id="plo-clo">
  <h2 class="sec">PLO &times; CLO Matrix</h2>
  <p style="font-size:13px;color:#4B5563;margin:-8px 0 14px;">Filled circle (&#9679;) indicates the CLO maps to that PLO. PROPOSED courses shown with amber header.</p>
  <h3 class="sub">Programme Learning Outcomes</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px;margin-bottom:20px;">
    {plo_cards}
  </div>
  {"".join(tables)}
</section>
"""


def render_data_issues(data: dict) -> str:
    issues = data.get("known_data_issues", [])
    items = "\n".join(
        f'<li style="margin-bottom:8px;"><strong>Decision needed:</strong> {esc(issue)}</li>'
        for issue in issues
    )
    if not items:
        items = "<li>(No data issues recorded)</li>"
    return f"""
<section id="data-issues">
  <h2 class="sec">Known Data Issues</h2>
  <div class="banner banner-amber" style="margin-bottom:14px;">
    <strong>Action required:</strong> The following issues must be resolved before UGCC submission.
  </div>
  <div class="card">
    <ol style="font-size:13px;color:#4B5563;line-height:1.7;padding-left:20px;margin:0;">
{items}
    </ol>
  </div>
</section>
"""


def render_appendix(data: dict) -> str:
    corpus = data.get("corpus_extracts", [])
    if not corpus:
        body = '<p style="font-size:13px;color:#4B5563;">(Corpus extract data not present in this data file.)</p>'
    else:
        rows = []
        for i, item in enumerate(corpus, start=1):
            title = item.get("title", item.get("source", str(item)))
            rows.append(
                f'<tr><td class="col-center">{i}</td>'
                f'<td>{esc(title)}</td>'
                f'<td>{esc(item.get("type",""))}</td>'
                f'<td style="font-size:12px;">{esc(item.get("relevance",""))}</td></tr>'
            )
        body = f"""
<div class="card" style="padding:0;overflow:hidden;">
  <div class="tbl-wrap">
    <table>
      <thead><tr><th>#</th><th>Title / Source</th><th>Type</th><th>Relevance</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
  </div>
</div>
"""
    return f"""
<section id="appendix">
  <h2 class="sec">Appendix A &mdash; Source Corpus Index</h2>
  {body}
</section>
"""


def render_footer() -> str:
    return f"""
<footer class="site-footer">
  {esc(FOOTER_TEXT)}
  <span class="dot">&middot;</span>
  Prepared by Dr. Carlo Raj
  <span class="dot">&middot;</span>
  Khalifa University CMHS
</footer>
"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build() -> None:
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SPMD Minor &rarr; Fall 2027 ADEK Roadmap &mdash; Khalifa University CMHS</title>
  <meta name="description" content="SPMD Minor and Sports Fitness Coaching Concentration Fall 2027 ADEK roadmap, Khalifa University CMHS.">
  <style>
{CSS}
  </style>
</head>
<body>
{render_header()}
{render_nav()}
<main>
{render_cover(data)}
{render_exec_summary(data)}
{render_tracks(data)}
{render_courses(data)}
{render_roadmap(data)}
{render_regulators(data)}
{render_plo_clo(data)}
{render_data_issues(data)}
{render_appendix(data)}
</main>
{render_footer()}
<script>
{JS}
</script>
</body>
</html>
"""

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(page)
    size = OUT_PATH.stat().st_size
    print(f"[OK] Wrote: {OUT_PATH}  ({size:,} bytes)")


if __name__ == "__main__":
    build()
