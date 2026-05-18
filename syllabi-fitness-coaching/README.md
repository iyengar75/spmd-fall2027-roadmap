# Sports & Fitness Coaching Track — Course Syllabi

UGCC-formatted course syllabi for the **Sports & Fitness Coaching specialization track** of the BSc Clinical Nutrition & Dietetics with Minor in Sports Medicine. These four courses operationalize Sara Almessabi's recommendation (email **2026-05-18**, ref: *Bachelor of Science (B.Sc.) in Clinical Nutrition and Dietetics with a Minor in Sports Medicine*) and supply the practical/coaching depth required for graduates to sit for **REPs UAE Level 3, NASM-CPT, ACE-CPT, ISSA-CPT, ACSM-CPT, and NSCA-CSCS** certifications.

## Stakeholder chain

| Date | From → To | Decision |
|------|-----------|----------|
| 2026-05-13 | Dr. Habiba Alsafar (Dean, CMHS) → Khalaf / Rangaraj / Almessabi | Inquiry from senior management: does current BSCND+Sports Medicine Minor qualify graduates as licensed fitness coaches? |
| 2026-05-14 | Sara Almessabi → Habiba | Current minor partially supports eligibility for NASM/ACE/ISSA/ACSM/NSCA-CSCS/REPs UAE but lacks dedicated practical coaching, exercise prescription, fitness training. |
| 2026-05-18 | Sara Almessabi → Kartik Rangaraj | **Recommended Track 2 combination: SPMD 305 + SPMD 306 + SPMD 308 + SPMD 302a** — strongest alignment with foundational fitness-coaching competencies. |

## Courses in this folder

| Code | Title | Credits | L:Lab | Type |
|---|---|---|---|---|
| SPMD 305 | Exercise Programme Design | 3 | 3:0 | Lecture |
| SPMD 306 | Group Fitness Instruction | 3 | 2:2 | Lecture + Studio |
| SPMD 308 | Supervised Coaching Practicum | 3 | 0:120 | Practicum (capstone) |
| SPMD 302a | Exercise Physiology Laboratory | 1 | 0:2 | Lab (coreq SPMD 302) |
| **Track Total** | | **10 cr** | | |

All four are stacked on top of the existing **Sports Medicine Minor core** (SPMD 301 + 302 + 303 + 304 + 301a + 302a) — total fitness-coaching pathway = 18 minor cr + 10 specialization cr = **28 credits** beyond the BSCND major.

## Structure (each syllabus)

All 17 KU UGCC sections present per *Course Syllabus Template Updated Dec 2025*:

1. Header (code, title, credit line)
2. Prerequisites + Corequisites
3. Course Catalog Description (80–150 words)
4. Textbook (1, IEEE format)
5. Reference Materials (3–4, IEEE format)
6. Course Structure & Learning Methodology
7. Weekly Course Topics table (14–15 wk)
8. Lab/Studio Tutorials table *(if applicable)*
9. Laboratory / Computing / Digital Resources
10. CLO ↔ PLO matrix (5 CLOs, mapped to BSCND PLOs 1-5, with H/M/L emphasis)
11. Assessment table (instruments summing to 100%)
12. UG Grading Scheme (11-row letter-grade table)
13. Academic Integrity Statement
14. Copyright and Plagiarism (incl. generative-AI clause)
15. Syllabus-supplement closing

## BSCND PLO mapping (program-level)

| PLO | Label |
|---|---|
| PLO1 | Problem-Solving with Science |
| PLO2 | System / Program Design |
| PLO3 | Experimentation & Data Analysis |
| PLO4 | Communication & Collaborative Practice |
| PLO5 | Ethics & Professional Responsibility |

| Course | Primary PLOs | Secondary PLOs |
|---|---|---|
| SPMD 305 | PLO2 (Design) | PLO1, PLO3, PLO4 |
| SPMD 306 | PLO4 (Communication) | PLO2, PLO5 |
| SPMD 308 | PLO4 + PLO5 | PLO2 |
| SPMD 302a | PLO3 (Data Analysis) | PLO1, PLO5, PLO4 |

## Certification crosswalk

| Course | NASM-CPT | ACE-CPT/GFI | ACSM | NSCA-CSCS | REPs UAE L3 |
|---|---|---|---|---|---|
| SPMD 305 | Programming & OPT model | Exercise programming | GETP 11 prescription | Programme design | Programme design competency |
| SPMD 306 | — | **ACE-GFI core** | ACSM-GEI core | — | Group exercise leadership |
| SPMD 308 | **120-hr practicum** | **120-hr practicum** | Practical assessment | Practicum hrs toward CSCS | **L3 practical assessment** |
| SPMD 302a | Assessments domain | Assessments domain | **Lab skills (VO₂max, lactate, BIA)** | Performance testing | Fitness-test skills (L2-L3) |

## Regenerating the .docx files

Each syllabus has a paired Python builder. To regenerate (e.g., to amend a CLO or a textbook):

```bash
cd <local clone>/syllabi-fitness-coaching
pip install python-docx
python build_spmd305_syllabus.py   # writes SPMD305_Syllabus_Consolidated.docx
python build_spmd306.py            # writes SPMD306_Syllabus_Consolidated.docx
python build_spmd308.py            # writes SPMD308_Syllabus_Consolidated.docx
# SPMD302a was built directly via python-docx by patching the KU template; see note below.
```

Builder scripts include assertions enforcing: 5 CLOs all PLO-mapped, assessment weights sum to 100%, SPMD 308 practicum hours = 120.

## Quality bar / QA checklist

Each file verified against the approved-reference quality bar set by `SPMD301_Syllabus_Consolidated.docx`:

- [x] All 17 UGCC sections present
- [x] Credit line matches header
- [x] 5 CLOs, each Bloom-aligned + PLO-mapped + emphasis (H/M/L)
- [x] Assessment weights sum to **exactly 100%**
- [x] 11-row UG grading scheme (A → F)
- [x] IEEE-formatted textbook + references
- [x] Weekly schedule = 14 weeks
- [x] Academic Integrity + Copyright (incl. AI clause) present
- [x] File size > approved-reference floor (41–63 KB)

## Pending / next steps

1. **Faculty validation** — assign SPMD-track faculty owner per course (currently authored by Claude Code pipeline against the Sara recommendation; no human faculty has reviewed). Required before UGCC submission.
2. **CPR/AED + First Aid corequisite for SPMD 308** — confirm institutional partner (AHA-BLS, EFR, or Red Crescent UAE) and add to KU registration prerequisite blocks.
3. **Site MoUs for SPMD 308** — solicit through KU Office of Industry Engagement: Fitness First UAE, Gold's Gym Abu Dhabi, KU Sports Center, Cleveland Clinic AD Wellness, corporate-wellness partners.
4. **REPs UAE / ADSC alignment letter** — Q3 2027 gate per [[project-spmd-fall2027-roadmap]].
5. **Update `_data.json`** — flip `_inferred: true` → `_inferred: false, _validated_by: "Sara Almessabi 2026-05-18"` for SPMD 305/306/308/302a once faculty validation lands.

## Provenance

- Authored: 2026-05-18 by Claude Code 4-agent parallel-syllabus pipeline (skill `ku-syllabus-author`)
- Template source: `Syllabi_BSCND/Course Syllabus Template Updated Dec 2025.docx` (KU-mandated, Dec 2025 revision)
- Quality reference: `Syllabi_BSCND/SPMD_Syllabi/SPMD301_Syllabus_Consolidated.docx` (UGCC-approved, Apr 2025)
- Stakeholder: Sara Almessabi (Health Educator, Falcon & Balsam, KU CMHS) — email 2026-05-18
- Decision authority: Dr. Habiba Alsafar (Dean, CMHS); Dr. Kinda Khalaf (Associate Dean, UG Studies); Dr. Kartik Rangaraj (Period Director, Medical Education)
