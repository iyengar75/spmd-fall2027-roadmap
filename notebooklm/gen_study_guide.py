#!/usr/bin/env python3
"""Generate study_guide.pdf via weasyprint."""
import json
from pathlib import Path

OUT = "/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/notebooklm/study_guide.pdf"

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>
  @page { size: A4; margin: 2.5cm 2.5cm 2.5cm 2.5cm; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; color: #222; line-height: 1.6; }
  h1 { font-size: 18pt; color: #003D7A; margin-bottom: 4px; }
  h2 { font-size: 13pt; color: #003D7A; margin-top: 20px; margin-bottom: 6px; border-left: 5px solid #C8A04A; padding-left: 10px; }
  h3 { font-size: 11pt; color: #003D7A; margin-top: 14px; margin-bottom: 4px; }
  .header-block { background: #003D7A; color: #fff; padding: 16px 20px; margin-bottom: 20px; }
  .header-block h1 { color: #C8A04A; font-size: 16pt; margin: 0; }
  .header-block .sub { color: #ddd; font-size: 9pt; margin-top: 5px; }
  .disclaimer { background: #fff3cd; border: 2px solid #C8A04A; padding: 12px 15px; margin: 16px 0; font-size: 9.5pt; }
  table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 9.5pt; }
  th { background: #003D7A; color: #fff; padding: 7px 9px; text-align: left; }
  td { border: 1px solid #bbb; padding: 6px 9px; vertical-align: top; }
  tr:nth-child(even) td { background: #f0f4fa; }
  .faq-q { font-weight: bold; color: #003D7A; margin-top: 12px; }
  .faq-a { margin-left: 16px; margin-bottom: 8px; }
  .pill { display: inline; background: #003D7A; color: #fff; padding: 2px 7px; border-radius: 4px; font-size: 9pt; }
  .pill-gold { display: inline; background: #C8A04A; color: #fff; padding: 2px 7px; border-radius: 4px; font-size: 9pt; }
  .pill-inferred { background: #e74c3c; }
  ul { margin: 6px 0; padding-left: 18px; }
  li { margin-bottom: 3px; }
  .footer { margin-top: 24px; border-top: 2px solid #C8A04A; padding-top: 8px; font-size: 8.5pt; color: #666; }
</style>
</head>
<body>

<div class="header-block">
  <h1>Internal Study Guide — Faculty &amp; UGCC Reviewer Reference</h1>
  <div class="sub">BSCND Sports Medicine Minor (SPMD 301–304) &amp; Sports &amp; Fitness Coaching Concentration (SPMD 305–308)<br/>
  Khalifa University · College of Medicine and Health Sciences · May 2026 · Restricted Circulation</div>
</div>

<div class="disclaimer">
  <strong>Inferred Content Disclosure:</strong>
  SPMD 305–308 syllabi have <em>not been formally authored</em>. Course structures, CLOs, PLO mappings,
  and ICREPs alignments are inferred from Dr. Habiba Alsafar's correspondence (May 2026),
  the proposed course table (Kartik Rangaraj/Sara Almessabi), published ICREPs Level 3 PT competency
  units, and REPs UAE registration requirements. All SPMD 305–308 content marked
  <span class="pill pill-inferred">INFERRED</span> must be reviewed and validated by SPMD faculty
  before any UGCC or ADEK submission. SPMD 301–304 are based on approved/consolidated syllabi
  <span class="pill">REVIEWED</span>.
</div>

<h2>1. KU Undergraduate Framework Placement — SPMD Courses</h2>

<p>The KU undergraduate framework places courses in Year 3 (300-level) and Year 4 (400-level).
All eight SPMD courses are correctly classified within this framework:</p>

<table>
  <tr><th>Code</th><th>Title</th><th>Credits</th><th>YR/Sem</th><th>Track</th><th>Status</th><th>Format</th></tr>
  <tr><td>SPMD 301</td><td>Foundations of Sports Medicine</td><td>3</td><td>Y3 Fall</td><td>Minor</td><td><span class="pill">REVIEWED</span></td><td>3L / 0Lab</td></tr>
  <tr><td>SPMD 302</td><td>Exercise Physiology</td><td>3</td><td>Y3 Spring</td><td>Minor</td><td><span class="pill">REVIEWED</span></td><td>3L / 0Lab</td></tr>
  <tr><td>SPMD 303</td><td>Injury Prevention &amp; Rehabilitation</td><td>3</td><td>Y3 Spring</td><td>Minor</td><td><span class="pill">REVIEWED</span></td><td>3L / 0Lab</td></tr>
  <tr><td>SPMD 304</td><td>Performance Assessment &amp; Technology</td><td>3</td><td>Y4 Fall</td><td>Minor</td><td><span class="pill">REVIEWED</span></td><td>2L / 1Lab</td></tr>
  <tr><td>SPMD 305</td><td>Personal Training &amp; Exercise Programme Design</td><td>3</td><td>Y3 Fall</td><td>Concentration</td><td><span class="pill pill-inferred">INFERRED</span></td><td>2L / 1Lab</td></tr>
  <tr><td>SPMD 306</td><td>Group Fitness, Stretching &amp; Conditioning Instruction</td><td>3</td><td>Y3 Spring</td><td>Concentration</td><td><span class="pill pill-inferred">INFERRED</span></td><td>1L / 2Lab</td></tr>
  <tr><td>SPMD 307</td><td>Fitness Coaching, Behaviour Change &amp; Business of Fitness</td><td>3</td><td>Y4 Fall</td><td>Concentration</td><td><span class="pill pill-inferred">INFERRED</span></td><td>3L / 0Lab</td></tr>
  <tr><td>SPMD 308</td><td>Fitness Coaching Practicum &amp; REPs UAE Certification Capstone</td><td>3</td><td>Y4 Spring</td><td>Concentration</td><td><span class="pill pill-inferred">INFERRED</span></td><td>1L / 200 supervised hrs</td></tr>
</table>

<p><strong>Credit note:</strong> A known data-entry error in <code>BSCND_KU_Mapping/_data.json</code>
lists SPMD 304 credits as 0. The correct value is 3 credits, confirmed from the SPMD 304 syllabus header.
This error must be corrected in all program documentation before UGCC submission.</p>

<h2>2. Prerequisite Logic and Sequencing</h2>

<p>The prerequisite chain enforces progressive skill-building from foundational science through applied coaching practice:</p>

<table>
  <tr><th>Course</th><th>Prerequisite</th><th>Rationale</th></tr>
  <tr><td>SPMD 301</td><td>BIOL 207: Human Physiology</td><td>Human physiology provides the anatomical and systems basis for sports medicine concepts</td></tr>
  <tr><td>SPMD 302</td><td>BIOL 207: Human Physiology</td><td>Cellular and systems physiology underpins exercise bioenergetics and cardiorespiratory adaptation</td></tr>
  <tr><td>SPMD 303</td><td>SPMD 301: Foundations of Sports Medicine</td><td>Injury prevention/rehab requires prior grounding in anatomy of movement, injury mechanisms, and tissue healing. <em>Note: source docx typo BMED301 corrected to SPMD301.</em></td></tr>
  <tr><td>SPMD 304</td><td>SPMD 302: Exercise Physiology</td><td>Performance assessment technology requires understanding physiological parameters being measured (VO2, lactate, HRV). <em>Note: source docx typo BMED302 corrected to SPMD302.</em></td></tr>
  <tr><td>SPMD 305</td><td>SPMD 301: Foundations of Sports Medicine</td><td>Exercise programme design requires anatomical and biomechanical understanding from SPMD 301</td></tr>
  <tr><td>SPMD 306</td><td>SPMD 302: Exercise Physiology</td><td>Group instruction requires physiological understanding of training adaptations and individual variation</td></tr>
  <tr><td>SPMD 307</td><td>SPMD 305: Personal Training &amp; Exercise Programme Design</td><td>Behaviour change and business modules build on applied exercise prescription experience from SPMD 305</td></tr>
  <tr><td>SPMD 308</td><td>SPMD 306 + SPMD 307 (both)</td><td>Capstone practicum requires mastery of group instruction (SPMD 306) and professional practice/behaviour change (SPMD 307) before supervised placement hours begin</td></tr>
</table>

<h2>3. PLO–CLO Derivation Rationale</h2>

<p>BSCND Program Learning Outcomes (PLOs) were mapped to SPMD courses to ensure coherence with the parent program's QFEmirates Level 6 learning outcomes:</p>

<table>
  <tr><th>PLO</th><th>Label</th><th>SPMD Courses</th><th>Derivation Logic</th></tr>
  <tr><td>PLO1</td><td>Problem-Solving with Science</td><td>301, 302, 303, 304, 305, 307</td><td>Applied scientific analysis of movement, physiology, and evidence-based intervention — core to all sports science courses</td></tr>
  <tr><td>PLO2</td><td>System / Program Design</td><td>301, 302, 303, 304, 305, 306, 308</td><td>Programme, prevention, and performance system design; directly realized in SPMD 305 and SPMD 308 applied outputs</td></tr>
  <tr><td>PLO3</td><td>Experimentation &amp; Data Analysis</td><td>302, 304, 305</td><td>Quantitative assessment (VO2max, force platforms, fitness metrics) forms the scientific substrate of coaching decisions</td></tr>
  <tr><td>PLO4</td><td>Communication &amp; Collaborative Practice</td><td>301, 303, 306, 307, 308</td><td>Interprofessional collaboration, client communication, instructional delivery, and reflective practice</td></tr>
  <tr><td>PLO5</td><td>Ethics &amp; Professional Responsibility</td><td>306, 307, 308</td><td>UAE regulatory compliance, scope of practice, professional ethics, and MoHRE/DED/REPs UAE requirements</td></tr>
</table>

<h2>4. ICREPs Level 3 PT Competency Alignment (SPMD 305–308) <span class="pill pill-inferred">INFERRED</span></h2>

<p>The four Concentration courses were designed to collectively address all ICREPs Level 3 Personal Trainer
competency units required for REPs UAE registration:</p>

<table>
  <tr><th>ICREPs L3 PT Unit</th><th>SPMD Course</th><th>CLO Mapping</th></tr>
  <tr><td>Apply Principles of Training</td><td>SPMD 305</td><td>CLO1 (FITT-VP, periodization), CLO4 (programme adjustment)</td></tr>
  <tr><td>Programme Design for General Population</td><td>SPMD 305</td><td>CLO1, CLO2 (needs analysis), CLO5 (nutrition integration)</td></tr>
  <tr><td>Group Fitness Instructor Competencies (ICREPs L2/3 GFI)</td><td>SPMD 306</td><td>CLO1, CLO2, CLO3, CLO5 (REPs UAE GFI competencies)</td></tr>
  <tr><td>Client Consultation &amp; Behaviour Change</td><td>SPMD 307</td><td>CLO1 (TTM, MI, SDT), CLO2 (UAE regulatory environment)</td></tr>
  <tr><td>Professional Practice (Scope + Ethics + Business)</td><td>SPMD 307</td><td>CLO3 (ethics/liability), CLO4 (business model), CLO5 (dual scope)</td></tr>
  <tr><td>Practical Coaching Hours (200 hrs supervised)</td><td>SPMD 308</td><td>CLO1 (200 hrs delivery), CLO3 (REPs UAE portfolio)</td></tr>
  <tr><td>First Aid / CPR / AED Certification</td><td>SPMD 308</td><td>CLO2 (embedded external certification)</td></tr>
</table>

<h2>5. SPMD 305–308 Inferred-Content Disclaimer (Full)</h2>

<p>UGCC reviewers must understand the provenance of SPMD 305–308 content before deliberation:</p>
<ul>
  <li><strong>Source of course titles and structures:</strong> Dr. Habiba Alsafar's May 14, 2026 email
  forwarding a proposed table from Dr. Carlo Raj, confirmed in follow-up from Kartik Rangaraj
  (Period Director, Medical Education). These courses were described as "newly proposed additions under
  Dr. Kinda's guidance" — not formally reviewed by any committee as of May 2026.</li>
  <li><strong>Source of CLOs:</strong> Inferred by pipeline agents from (a) ICREPs Level 3 PT published
  competency units, (b) REPs UAE registration requirements at repsuae.com, (c) Physical Manager Program
  Plan PPTX (Cseh 2018) module mapping, and (d) the gap analysis in Integration_Deliverables/_analysis.json.</li>
  <li><strong>Source of PLO and KU ILO mappings:</strong> Derived by applying standard KU UGCC alignment
  methodology to inferred CLOs. Not validated by BSCND program faculty or CMHS College Council.</li>
  <li><strong>What faculty must do before UGCC submission:</strong> Author full syllabi using KU Course
  Syllabus Template (December 2025 version); validate CLOs against actual course content; confirm
  ICREPs alignment with a REPs UAE liaison contact; obtain CMHS College Council endorsement.</li>
</ul>

<h2>6. FAQ for UGCC Committee Deliberation</h2>

<div class="faq-q">Q1: Why are SPMD 301–304 and SPMD 305–308 submitted together as a bundled UGCC packet?</div>
<div class="faq-a">The Concentration (305–308) builds directly on the Minor (301–304) through the prerequisite chain. Separating the submissions creates risk of orphaned prerequisites and forces a second UGCC review cycle. Bundling also allows the committee to evaluate the complete dual-credential pathway in a single deliberation, reducing administrative overhead for the Q4 2026 ADEK submission deadline.</div>

<div class="faq-q">Q2: SPMD 303 and SPMD 304 source syllabi contain "BMED 301/302" as prerequisite codes. Is this an error?</div>
<div class="faq-a">Yes — confirmed data-entry errors. The prerequisites should read SPMD 301 (for SPMD 303) and SPMD 302 (for SPMD 304). These typos are documented in the pipeline's known_data_issues log and must be corrected in the UGCC submission packet before filing.</div>

<div class="faq-q">Q3: Kinda Khalaf mentioned approximately 18 credits for a "strengthened minor." How does this relate to the current 12-credit proposal?</div>
<div class="faq-a">This discrepancy is unresolved as of May 2026 and requires a decision by Dr. Carlo Raj before UGCC submission. The current pipeline uses Option A (12-credit Concentration, total 124→136 credits). If the 18-credit option is preferred, an alternative track design must be developed. UGCC reviewers should note this as a pending design decision.</div>

<div class="faq-q">Q4: Does completion of SPMD 305–308 guarantee REPs UAE registration for graduates?</div>
<div class="faq-a">Not automatically. REPs UAE registration requires (1) an ICREPs-accredited Level 3 PT qualification — which the SPMD Concentration must formally obtain through ICREPs accreditation, (2) a current First Aid/CPR certificate (embedded in SPMD 308), and (3) documented practical hours (200 hrs in SPMD 308). KU must obtain a formal alignment/accreditation letter from REPs UAE confirming SPMD 305–308 meets ICREPs Level 3 PT standards. This is scheduled as a Q3 2027 gate.</div>

<div class="faq-q">Q5: How does SPMD 304 differ from SPMD 305 for the purposes of QFEmirates Level 6 skills?</div>
<div class="faq-a">SPMD 304 (Performance Assessment &amp; Technology) is framed around measuring and monitoring athlete performance using laboratory and wearable technology — it is assessment-oriented and athlete-facing. SPMD 305 (Personal Training &amp; Exercise Programme Design) is prescription-oriented and general-population/client-facing. SPMD 304 belongs to the Minor; SPMD 305 belongs to the Concentration. They are complementary but non-redundant.</div>

<div class="faq-q">Q6: What are the lab facility requirements for SPMD 305, 306, and 308?</div>
<div class="faq-a">SPMD 305 (1 lab/wk, 150 min): requires resistance training equipment, cardiovascular machines, functional training tools. SPMD 306 (2 lab/wk, 300 min): requires group exercise studio with sound system, stretching area, conditioning equipment. SPMD 308 (200 supervised hours): requires practicum placement MoUs with REPs-affiliated Abu Dhabi health clubs (Fitness First, Gold's Gym, NAS Sports Complex Abu Dhabi). Current KU CMHS facilities and practicum placement capacity must be confirmed before UGCC submission.</div>

<h2>7. KU ILO Coverage Across SPMD Courses</h2>

<p>KU's fifteen Institutional Learning Outcomes (ILOs) provide the institutional framework for quality
assurance. The table below maps SPMD courses to the KU ILOs they address, supporting UGCC reviewers
in validating that the SPMD tracks contribute meaningfully to KU's graduate profile:</p>

<table>
  <tr><th>KU ILO</th><th>Description (summary)</th><th>SPMD Courses</th></tr>
  <tr><td>ILO1</td><td>Breadth of knowledge across disciplines</td><td>SPMD 301</td></tr>
  <tr><td>ILO2</td><td>Apply scientific method</td><td>SPMD 302, 304, 305</td></tr>
  <tr><td>ILO3</td><td>Critical thinking and problem analysis</td><td>SPMD 301, 302, 303, 305</td></tr>
  <tr><td>ILO5</td><td>Understanding of sustainability / societal impact</td><td>SPMD 307</td></tr>
  <tr><td>ILO6</td><td>Effective communication (written/oral)</td><td>SPMD 301, 306, 307, 308</td></tr>
  <tr><td>ILO7</td><td>Digital literacy and technology use</td><td>SPMD 304</td></tr>
  <tr><td>ILO8</td><td>Quantitative reasoning and data interpretation</td><td>SPMD 302, 304</td></tr>
  <tr><td>ILO9</td><td>Lifelong learning and professional development</td><td>SPMD 302, 303, 305, 306, 307</td></tr>
  <tr><td>ILO10</td><td>Innovation and creative problem solving</td><td>SPMD 304, 305</td></tr>
  <tr><td>ILO11</td><td>Research skills</td><td>SPMD 308</td></tr>
  <tr><td>ILO12</td><td>Teamwork and collaboration</td><td>SPMD 303, 306, 308</td></tr>
  <tr><td>ILO14</td><td>Ethics, professionalism, and social responsibility</td><td>SPMD 306, 307, 308</td></tr>
  <tr><td>ILO15</td><td>Self-management and leadership</td><td>SPMD 308</td></tr>
</table>

<h2>8. Course-Level Learning Environment Requirements</h2>

<p>Faculty and the UGCC must confirm that the following physical learning environment requirements
can be met before the SPMD courses go live in Fall 2027:</p>

<table>
  <tr><th>Course</th><th>Room Type</th><th>Equipment Required</th><th>Status</th></tr>
  <tr><td>SPMD 301</td><td>Lecture theatre / seminar room</td><td>Standard AV; anatomical models optional</td><td>Standard KU provision — no special requirements</td></tr>
  <tr><td>SPMD 302</td><td>Lecture theatre</td><td>Standard AV; access to spirometry/VO2max equipment desirable but not mandatory for 3L/0Lab format</td><td>Lecture-only — standard provision</td></tr>
  <tr><td>SPMD 303</td><td>Lecture theatre</td><td>Standard AV; movement assessment tools (goniometers, FMS kit) desirable</td><td>Lecture-only — standard provision</td></tr>
  <tr><td>SPMD 304</td><td>Sports science laboratory</td><td>Force platforms, motion capture system or equivalent, heart rate monitors, GPS trackers, body composition analyser</td><td>REQUIRES CONFIRMATION: laboratory availability and equipment procurement must be verified before UGCC submission</td></tr>
  <tr><td>SPMD 305</td><td>Fitness laboratory / gym</td><td>Resistance training equipment (barbells, dumbbells, cable machines), cardiovascular machines (treadmills, bikes, rowers), functional training tools</td><td>REQUIRES CONFIRMATION: KU CMHS fitness facility capacity for class instruction use</td></tr>
  <tr><td>SPMD 306</td><td>Group exercise studio</td><td>Sound system, open floor space, mats, resistance bands, steps, group exercise props</td><td>REQUIRES CONFIRMATION: dedicated group exercise studio required; 300 min/week lab time is substantial</td></tr>
  <tr><td>SPMD 307</td><td>Lecture theatre / seminar room</td><td>Standard AV; case study materials; guest speaker capacity for UAE industry practitioners</td><td>Standard provision — no special requirements</td></tr>
  <tr><td>SPMD 308</td><td>External placement + weekly seminar room</td><td>200 supervised hours at REPs-affiliated health clubs; KU seminar room for weekly reflection sessions; CPR/AED manikins for embedded certification</td><td>CRITICAL: MoUs with Fitness First UAE, Gold's Gym, NAS Sports Complex Abu Dhabi must be executed by Q1 2027</td></tr>
</table>

<h2>9. Textbook and Resource Recommendations for SPMD 305–308</h2>

<p>The following textbooks are recommended for the as-yet-unAuthored SPMD 305–308 syllabi,
based on ICREPs Level 3 PT standard reading lists and the BSCND programme's existing textbook
selection criteria (current editions, peer-reviewed, QFEmirates Level 6 appropriate):</p>

<table>
  <tr><th>Course</th><th>Recommended Primary Textbook</th><th>Rationale</th></tr>
  <tr><td>SPMD 305</td><td>Baechle, T. R., &amp; Earle, R. W. (Eds.). (2008). <em>Essentials of Strength Training and Conditioning</em> (3rd or 4th ed.). Human Kinetics. <em>AND</em> American College of Sports Medicine. (2022). <em>ACSM's Guidelines for Exercise Testing and Prescription</em> (11th ed.). Wolters Kluwer.</td><td>NSCA CSCS text provides periodization and programme design; ACSM Guidelines provides general-population prescription standards aligned with ICREPs L3 PT</td></tr>
  <tr><td>SPMD 306</td><td>Francis, L. (2020). <em>Group Fitness Instructor Manual</em>. American Council on Exercise (ACE).</td><td>Industry-standard group fitness instruction text; maps to REPs UAE GFI competencies and ACE GFI certification requirements</td></tr>
  <tr><td>SPMD 307</td><td>Rollnick, S., Miller, W. R., &amp; Butler, C. C. (2008). <em>Motivational Interviewing in Health Care</em>. Guilford Press. <em>AND</em> Prochaska, J. O., &amp; Norcross, J. C. (2018). <em>Systems of Psychotherapy: A Transtheoretical Analysis</em> (9th ed.). Oxford University Press.</td><td>MI and TTM primary source texts for CLO1's behaviour-change theory module; both standard in coaching psychology curricula at QFEmirates L6</td></tr>
  <tr><td>SPMD 308</td><td>No single primary text — practicum-based course. Portfolio assessment documentation: REPs UAE Practical Hours Log template; KU Reflective Practice Framework; CPR/AED certification materials from Heart &amp; Stroke Foundation or UAE Red Crescent.</td><td>Practicum capstone assessed via portfolio, supervision logs, and external certification — not textbook-based</td></tr>
</table>

<h2>10. Assessment Strategy Overview (SPMD 305–308)</h2>

<p>Pending formal syllabus authoring, the following assessment strategy is proposed based on
ICREPs Level 3 PT competency requirements and UGCC standard assessment design principles:</p>

<table>
  <tr><th>Course</th><th>Proposed Assessment Mix</th><th>ICREPs Competency Evidence</th></tr>
  <tr><td>SPMD 305</td><td>60% practical (in-lab programme delivery demonstration + client assessment simulation); 40% written (exercise prescription report with scientific justification)</td><td>Satisfies ICREPs L3 PT "Apply Principles of Training" practical evidence requirement</td></tr>
  <tr><td>SPMD 306</td><td>80% practical (group fitness class delivery — observed and peer-assessed); 20% written (class design documentation)</td><td>Satisfies ICREPs L2/3 GFI observed teaching requirement</td></tr>
  <tr><td>SPMD 307</td><td>50% case study report (client coaching plan); 30% role-play assessment (motivational interviewing); 20% business plan submission</td><td>Satisfies ICREPs L3 PT "Client Consultation" and "Professional Practice" evidence requirements</td></tr>
  <tr><td>SPMD 308</td><td>Portfolio (60%): supervised hours log + supervisor evaluation forms + reflective journal; External certification (30%): CPR/AED pass/fail from accredited provider; Final presentation (10%): professional development goals</td><td>Directly assembles REPs UAE PT registration portfolio — the portfolio IS the assessment artefact</td></tr>
</table>

<div class="footer">
  Document prepared May 2026 · Pipeline Agent A6 · Restricted — Faculty and UGCC use only ·
  SPMD 305–308 content is inferred and requires faculty validation before any formal submission.
</div>

</body>
</html>"""

from weasyprint import HTML
HTML(string=html).write_pdf(OUT)
print(f"Written: {OUT}")
