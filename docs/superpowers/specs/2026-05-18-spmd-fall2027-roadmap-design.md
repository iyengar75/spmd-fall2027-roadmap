# SPMD Minor → Fall 2027 ADEK Roadmap — Design Spec

**Status:** approved by user 2026-05-18 (architecture · agent topology · persistence + verification)
**Author:** Claude Code session for Carlo Raj (iyengar75)
**Working dir:** `/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/`
**Target audience for deliverables:** ADEK reviewers (Abu Dhabi accreditor) — formal compliance voice
**Launch window:** Fall 2027 (≈ 16 months from today, 2026-05-18)

---

## 1. Purpose

Produce a complete, ADEK-aligned roadmap package for a two-track Sports Medicine offering inside the BSc Clinical Nutrition & Dietetics (BSCND) program at Khalifa University:

- **Track 1 · Sports Medicine Minor** — existing `SPMD 301–304` (4 consolidated syllabi already drafted; pending UGCC review)
- **Track 2 · Sports & Fitness Coaching Concentration** — proposed `SPMD 305–308` in response to Dr. Habiba Alsafar's licensure enquiry (REPs UAE / ADSC alignment)

The package must be defensible to ADEK reviewers and slot into the existing `FINAL_REVISED_ADEK_BSCND_Application.docx` workflow.

## 2. Scope (locked)

Five deliverable streams, all in scope (A + B + C + D + E):

| ID | Deliverable | Format |
|----|---|---|
| **A** | NotebookLM corpus + 5 research artifacts | Notebook + briefing.pdf + study_guide.pdf + audio_overview.mp3 + mind_map.png + qa_pack.pdf |
| **B** | Two Excalidraw scenes → SVG + PNG | (1) Quarter × Track × Gate matrix, (2) Regulator alignment hub |
| **C** | Python pipeline → multi-format roadmap doc | `_data.json` → `.docx + .xlsx + .html` (KU Navy `#003D7A` / Gold `#C8A04A` brand) |
| **D** | React/TS + Vite + shadcn microsite | Deployed to Lovable; animated timeline + course cards + regulator matrix + downloads panel (offers .docx + .xlsx + .html + .pdf briefing + .svg diagrams + .mp3 audio overview as direct downloads, all served from the repo's `public/` dir) |
| **E** | Persistence | New public GitHub repo, mirror into BSCND-MSCR-ADEK, Obsidian note + Master Index entry, reusable skill, 3 memory updates |

## 3. Timeline structure

Hybrid **Quarter × Track × Gate matrix**, 5 quarters:

| Quarter | SPMD 301-304 (Minor) | SPMD 305-308 (Concentration) | Gate |
|---|---|---|---|
| Q3 2026 | UGCC packet | Authoring | UGCC review |
| Q4 2026 | ADEK draft | UGCC submit | ADEK Program Authorization |
| Q1 2027 | MoHESR / MoE | ADEK | MoE approval |
| Q2 2027 | Marketing | KU Senate | KU Senate / Board sign-off |
| Q3 2027 | **★ Fall 2027 Launch ★** | **★ Fall 2027 Launch ★** | Go-live + REPs UAE / ADSC alignment letter |

## 4. Architecture

**Single source of truth:** `_data.json` drives every downstream deliverable. Editing one field cascades through all 5 streams; no artifact drift.

### 4.1 `_data.json` schema

```jsonc
{
  "program": { "name": "BSc Clinical Nutrition & Dietetics", "launch": "Fall 2027" },
  "tracks": [
    { "id": "minor",         "name": "Sports Medicine Minor",
      "courses": ["SPMD301","SPMD302","SPMD303","SPMD304"] },
    { "id": "concentration", "name": "Sports & Fitness Coaching Concentration",
      "courses": ["SPMD305","SPMD306","SPMD307","SPMD308"] }
  ],
  "courses": {
    "SPMD301": { "title": "...", "credits": 3, "plos": [...], "clos": [...], "ku_gelo": [...] },
    /* ... 7 more ... */
  },
  "phases": [
    { "q": "Q3 2026", "deliverables_by_track": { "minor": "...", "concentration": "..." },
      "gate": "UGCC review", "owner": "..." },
    /* ... 4 more ... */
  ],
  "regulators": {
    "REPs UAE":  { "scope": "Fitness professional registration",
                   "alignment": { "SPMD305": "Tier 2 Personal Trainer match", /* ... */ } },
    "ADSC":      { "scope": "Abu Dhabi Sports Council", "alignment": { /* ... */ } },
    "DSC":       { "scope": "Dubai Sports Council", "alignment": { /* ... */ } },
    "GAS":       { "scope": "General Authority of Sport", "alignment": { /* ... */ } },
    "DoH":       { "scope": "Department of Health", "alignment": { /* ... */ } },
    "MoHRE":     { "scope": "Ministry of Human Resources & Emiratisation",
                   "alignment": { /* ... */ } }
  },
  "corpus": [
    { "id": "habiba_01", "type": "pdf", "path": "HabibaResponse_01.pdf", "extract": "..." },
    /* ... 11 more ... */
  ]
}
```

### 4.2 Data-flow diagram

```
_data.json ──┬──> A. NotebookLM (5 artifacts)
             ├──> B. Excalidraw × 2 (SVG + PNG)
             ├──> C. Python pipeline (.docx + .xlsx + .html)
             ├──> D. React/Vite/shadcn microsite (Lovable)
             └──> E. Persistence layer
```

## 5. Agent topology (7 agents, 3 waves)

```
WAVE 1 (parallel — 2 agents)
  A1 · Corpus + Data Author    → corpus_extracts.json + _data.json
  A2 · NotebookLM Setup        → notebook_id

WAVE 2 (parallel — 4 agents, all consume _data.json)
  A3 · Excalidraw scenes       → 2 × .excalidraw + .svg + .png
  A4 · Python pipeline         → .docx + .xlsx + .html
  A5 · React microsite         → /microsite source tree
  A6 · NotebookLM artifacts    → briefing + study_guide + audio + mind_map + qa_pack

WAVE 3 (sequential — 1 agent)
  A7 · Deploy + Persist        → Lovable URL + new repo + mirror + Obsidian + skill + memory
```

**Inter-agent contract:** `_data.json` is the only file Wave-2 agents read from Wave-1 output. No agent reads another agent's intermediate state.

## 6. Token-budget DNA

| Pattern | Rationale |
|---|---|
| `export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` before Wave 1 | Activates agent teams (per user's CLAUDE.md) |
| Agent prompts cap report length at 300 words; return paths, not contents | Keeps main context lean |
| PDFs > 10 pages read with `pages: "1-10"` then paginated | Avoids 200K-token reads |
| Subagents own all heavy Read/Bash/Edit/Write; main context only sees summaries | Context isolation |
| Artifacts written to disk, not returned in tool results | Main context receives paths only |
| Worktree isolation for microsite work (A5) | Prevents Vite scaffold polluting working dir |

## 7. Failure-mode handling

| Failure | Fallback |
|---|---|
| Lovable deploy fails (auth/credits) | A7 commits microsite source only; reports manual deploy command |
| NotebookLM auth rotated | A2 reports auth failure; A6 retries or reports "manual upload required" with prepared corpus URLs |
| GitHub MCP returns bad credentials (observed earlier 2026-05-18) | A7 uses `gh` CLI with OAuth token (`gho_*` scopes: repo, delete_repo, workflow) |
| Excalidraw MCP server not running | A3 falls back to fireworks-tech-graph skill (SVG/PNG) |
| Python pipeline syntax error | Each `_build_*.py` is independent; failure of one doesn't block the others |

## 8. Persistence map (locations of all deliverables)

```
GITHUB (public, NEW repo) — iyengar75/spmd-fall2027-roadmap
  README.md
  _data.json                                ← single source of truth
  corpus_extracts.json
  notebooklm/
    notebook_id.txt
    briefing.pdf
    study_guide.pdf
    audio_overview.mp3
    mind_map.png
    qa_pack.pdf
  diagrams/
    qtg_matrix.excalidraw + .svg + .png
    regulator_alignment.excalidraw + .svg + .png
  docs/
    SPMD_Fall2027_Roadmap.docx
    SPMD_Fall2027_Roadmap.xlsx
    SPMD_Fall2027_Roadmap.html
    _build_docx.py
    _build_xlsx.py
    _build_html.py
  microsite/                                ← React/Vite/shadcn source
    src/...
    package.json
    README.md (Lovable URL)
  skills/spmd-roadmap-pipeline/SKILL.md

GITHUB (existing, private) — iyengar75/BSCND-MSCR-ADEK
  spmd-fall2027-roadmap/                    ← full mirror of above (plain file copy committed
                                              in a single commit; NOT a submodule — avoids cross-
                                              repo dependency for ADEK reviewers reading offline)

OBSIDIAN VAULT
  GitHub/spmd-fall2027-roadmap.md           ← new note (frontmatter: tags, source, synced)
  GitHub/00-GitHub-Master-Index.md          ← appended 2026-05-18 section

LOCAL (this machine)
  ~/.claude/skills/spmd-roadmap-pipeline/SKILL.md   ← reusable skill, user-global

MEMORY (~/.claude/projects/.../memory/)
  project_spmd_minor_state.md               ← UPDATED: links roadmap repo + Fall 2027 state
  project_bscnd_fitness_coach.md            ← UPDATED: cross-link new repo + microsite URL
  project_spmd_fall2027_roadmap.md          ← NEW: links artifacts, agent topology, ADEK packet

LOVABLE
  https://<slug>.lovable.app                ← live microsite URL (slug captured in A7 report)
```

## 9. Verification gates

Final acceptance: A7's report ends with this table showing 11/11 ✅.

| # | Deliverable | "Done" means | Evidence command |
|---|---|---|---|
| 1 | `_data.json` | Valid JSON, all 8 courses + 5 quarters + 6 regulators populated | `jq '.tracks[].courses\|length, .phases\|length, .regulators\|keys\|length' _data.json` |
| 2 | NotebookLM artifacts | All 5 files present and non-empty | `ls -la notebooklm/*.{pdf,mp3,png}` |
| 3 | Excalidraw scenes | 2 `.excalidraw` files + `.svg` + `.png` exports each | `ls diagrams/*.{excalidraw,svg,png}` |
| 4 | Python pipeline | `.docx + .xlsx + .html` regenerate identically from `_data.json` (idempotent) | `python _build_docx.py && python _build_xlsx.py && python _build_html.py` exits 0 |
| 5 | React microsite | `npm run build` succeeds; build artifact loads; 4 sections render | `npm run build` exits 0; manual smoke-test of preview URL |
| 6 | Lovable deploy | Public URL returns HTTP 200; first paint shows Q×T×G matrix | `curl -sI <lovable-url> \| head -1` |
| 7 | GitHub repo | Repo exists, all paths above present, README has Lovable URL + diagram thumbnails | `gh repo view iyengar75/spmd-fall2027-roadmap --json url` |
| 8 | BSCND-MSCR-ADEK mirror | `spmd-fall2027-roadmap/` subdir matches | `git diff --no-index` empty |
| 9 | Obsidian note | Note exists; Master Index has 2026-05-18 entry | `mcp__mcp-obsidian__obsidian_get_file_contents` returns frontmatter |
| 10 | Skill | `~/.claude/skills/spmd-roadmap-pipeline/SKILL.md` exists with valid frontmatter | `head -10 ~/.claude/skills/.../SKILL.md` |
| 11 | Memory | 3 memory files updated; MEMORY.md index entries fresh | `grep spmd ~/.claude/projects/.../memory/MEMORY.md` |

## 10. Reusable skill

`spmd-roadmap-pipeline` (authored as part of E) captures the 7-agent workflow so future runs (MSCR roadmap, BSCND Y2 update, other KU programs) require only swapping `_data.json` content and the audience field. Installed user-global at `~/.claude/skills/spmd-roadmap-pipeline/`.

## 11. Out of scope (deferred)

- HyperFrames animated walkthrough video (Approach 3 declined)
- HeyGen avatar video for stakeholder briefing (Approach 3 declined)
- Faculty CV / hiring plan section of ADEK packet (separate workstream)
- Resource-allocation budget for SPMD lab equipment (separate workstream)
- 200-level prerequisite re-mapping for SPMD entry (separate workstream)

## 12. Next step

Per the brainstorming skill protocol: user reviews this spec, then I invoke `superpowers:writing-plans` to produce a step-by-step implementation plan before any agents are dispatched.
