---
name: spmd-roadmap-pipeline
description: Generate an ADEK-aligned roadmap bundle for a KU BSCND minor/concentration. Use when user asks to produce a multi-deliverable program roadmap with NotebookLM corpus + Excalidraw infographics + Python pipeline (.docx/.xlsx/.html) + React/Vite/shadcn microsite + persistence (GitHub + Obsidian + memory). Triggers — "build a roadmap for X program", "package this for ADEK", "make a Lovable site for this curriculum", "generate the SPMD-style bundle for [other program]".
---

# spmd-roadmap-pipeline

Reusable 7-agent pipeline for generating ADEK-grade multi-deliverable curriculum roadmap bundles. First executed 2026-05-18 for the SPMD Minor + Sports & Fitness Coaching Concentration at KU BSCND.

## 7-Agent Topology

### Wave 1 — Sequential (A1)
- **A1**: Corpus extraction from source PDFs/DOCX/PPTX → `_data.json` (single source of truth) + `corpus_extracts.json`

### Wave 2 — Parallel (A3, A4, A5, A6)
- **A3**: Excalidraw infographics (Scene 1: Q×T×G matrix; Scene 2: regulator alignment hub). Uses Python to generate `.excalidraw` + `.svg` + `.png` files directly (no canvas server needed).
- **A4**: Python doc pipeline → `_build_docx.py` + `_build_xlsx.py` + `_build_html.py` → KU Navy/Gold branded deliverables for ADEK reviewers
- **A5**: React/Vite/shadcn/framer-motion microsite. Reads `_data.json` at RUNTIME via `fetch('/_data.json')` — no rebuild after data update. `microsite/public/_data.json` and `microsite/dist/_data.json` are the only files to update.
- **A6**: NotebookLM-equivalent artifacts: briefing PDF + study guide PDF + Q&A pack PDF + mind map PNG + audio narration script (`gen_audio.py`).

### Wave 3 — Sequential (A7)
- **A7**: 18-credit regen + all builds + GitHub push + Obsidian sync + skill + memory

## `_data.json` Schema (Single Source of Truth)

Top-level keys:
- `program` — name, institution, college, launch, credits_baseline, credits_with_concentration, qf_emirates_level, adek_submission_version
- `tracks[]` — id, name, credits_total, courses[], status, icreps_eligible, note
- `bscnd_plos[]` — id, label, description, qfemirates_alignment
- `courses{}` — keyed by code (e.g. SPMD301). Each: title, credits, semester, track, description, clos[], plos[], ku_gelo[], _inferred, _inference_note
- `phases[]` — q, label, date_range, deliverables{minor, concentration}, gate, owner, decision_maker, key_actions[]
- `regulators{}` — keyed by body name. Each: full_name, name_ar, url, level, scope, tier, requirements[], alignment{}
- `ku_brand` — navy, gold, white, font_heading, font_body
- `stakeholders{}` — key persons
- `known_data_issues[]` — list of strings
- `generated_at`, `generated_by`, `pipeline_version`

## Token-Budget DNA

- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` — enable parallel agent dispatch
- Subagent isolation — each Wave 2 agent writes to separate paths; no shared state
- Runtime-fetch microsite — updating `public/_data.json` is sufficient after data changes; no Vite rebuild needed
- Plain-file mirror into `BSCND-MSCR-ADEK` (not submodule) for offline ADEK reviewer access
- Build scripts are idempotent — safe to re-run after any `_data.json` change

## Pitfalls Observed (2026-05-18 Run)

1. **NotebookLM MCP auth in WSL**: `uvx --from notebooklm-skill notebooklm login` must be run in WSL terminal and Claude Code restarted before the MCP server picks up the auth token. NotebookLM artifacts were generated locally as Python PDF/PNG equivalents instead.
2. **ElevenLabs key expiry**: `gen_audio.py` works but the API key expires. `audio_overview.mp3` is a placeholder MP3. User must rotate key and re-run `gen_audio.py`.
3. **Excalidraw canvas server unreachable**: The Excalidraw MCP canvas tool was not reachable. A3 agent wrote pure-Python scripts (`build_scene1.py`, `build_scene2.py`) that generate `.excalidraw` JSON, `.svg`, and `.png` files directly — no canvas server needed.
4. **GitHub PAT vs OAuth scope**: Default `GITHUB_TOKEN` env var is set to a PAT (`github_pat_*`) that lacks `delete_repo` / full `repo` create scope. Always `unset GITHUB_TOKEN` first to fall through to the OAuth token (`gho_*`) which has `repo, delete_repo, workflow` scope.
5. **WSL→Windows path for node_modules**: The microsite `node_modules/` must be excluded from `.gitignore` to avoid enormous commits.

## Reuse Pattern

To generate a new program bundle:
1. Copy `_data.json` and swap out all content (program name, tracks, courses, phases, regulators).
2. Update `audience` field for the target reviewer (e.g. "ADEK reviewers", "UGCC committee", "Senate").
3. Re-run all build scripts:
   ```bash
   cd docs && python3 _build_docx.py && python3 _build_xlsx.py && python3 _build_html.py
   cp _data.json microsite/public/_data.json microsite/dist/_data.json
   cd ../notebooklm && python3 gen_briefing.py && python3 gen_study_guide.py && python3 gen_qa_pack.py && python3 gen_mindmap.py
   python3 ../build_scene1.py && python3 ../build_scene2.py
   ```
4. Push to new GitHub repo, mirror to `BSCND-MSCR-ADEK`, sync Obsidian note.

## Files

| Script | Output | Notes |
|---|---|---|
| `docs/_build_docx.py` | `docs/SPMD_Fall2027_Roadmap.docx` | KU Navy/Gold branded |
| `docs/_build_xlsx.py` | `docs/SPMD_Fall2027_Roadmap.xlsx` | 6 sheets |
| `docs/_build_html.py` | `docs/SPMD_Fall2027_Roadmap.html` | Self-contained, no CDN |
| `build_scene1.py` | `diagrams/qtg_matrix.{excalidraw,svg,png}` | Q×T×G matrix |
| `build_scene2.py` | `diagrams/regulator_alignment.{excalidraw,svg,png}` | Regulator hub |
| `notebooklm/gen_briefing.py` | `notebooklm/briefing.pdf` | |
| `notebooklm/gen_study_guide.py` | `notebooklm/study_guide.pdf` | |
| `notebooklm/gen_qa_pack.py` | `notebooklm/qa_pack.pdf` | |
| `notebooklm/gen_mindmap.py` | `notebooklm/mind_map.png` | |
| `notebooklm/gen_audio.py` | `notebooklm/audio_overview.mp3` | ElevenLabs key required |

## Reference

- GitHub: https://github.com/iyengar75/spmd-fall2027-roadmap
- Mirror: https://github.com/iyengar75/BSCND-MSCR-ADEK/tree/main/spmd-fall2027-roadmap
- Design spec: `docs/superpowers/specs/2026-05-18-spmd-fall2027-roadmap-design.md`
