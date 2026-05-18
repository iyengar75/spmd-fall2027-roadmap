#!/usr/bin/env python3
"""Generate briefing.pdf via weasyprint from HTML source."""
import json, sys
from pathlib import Path

DATA = json.loads(Path("/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/_data.json").read_text())
OUT = "/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/notebooklm/briefing.pdf"

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>
  @page { size: A4; margin: 2.5cm 2.5cm 2.5cm 2.5cm; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 11pt; color: #222; line-height: 1.6; }
  h1 { font-size: 20pt; color: #003D7A; border-bottom: 3px solid #C8A04A; padding-bottom: 8px; margin-bottom: 6px; }
  h2 { font-size: 14pt; color: #003D7A; margin-top: 22px; margin-bottom: 6px; border-left: 5px solid #C8A04A; padding-left: 10px; }
  h3 { font-size: 12pt; color: #003D7A; margin-top: 14px; }
  .header-block { background: #003D7A; color: #fff; padding: 18px 22px; margin-bottom: 24px; }
  .header-block h1 { color: #C8A04A; border: none; margin: 0; padding: 0; font-size: 18pt; }
  .header-block .sub { color: #eee; font-size: 10pt; margin-top: 6px; }
  .disclaimer { background: #fff8e1; border-left: 5px solid #C8A04A; padding: 12px 16px; margin: 18px 0; font-size: 10pt; }
  table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 10pt; }
  th { background: #003D7A; color: #fff; padding: 8px 10px; text-align: left; }
  td { border: 1px solid #ccc; padding: 7px 10px; vertical-align: top; }
  tr:nth-child(even) td { background: #f5f8ff; }
  .track-box { border: 2px solid #003D7A; border-radius: 6px; padding: 14px 18px; margin: 10px 0; }
  .track-minor { border-color: #003D7A; }
  .track-conc { border-color: #C8A04A; }
  .track-label { font-weight: bold; color: #003D7A; font-size: 12pt; }
  .gold { color: #C8A04A; font-weight: bold; }
  .risk-high { color: #c0392b; font-weight: bold; }
  .risk-med { color: #d68910; font-weight: bold; }
  .risk-low { color: #27ae60; font-weight: bold; }
  ul { margin: 8px 0; padding-left: 20px; }
  li { margin-bottom: 4px; }
  .footer { margin-top: 30px; border-top: 2px solid #003D7A; padding-top: 10px; font-size: 9pt; color: #666; }
  .ask-box { background: #003D7A; color: #fff; padding: 16px 20px; border-radius: 6px; margin: 20px 0; }
  .ask-box h3 { color: #C8A04A; margin-top: 0; }
  .ask-box ul li { margin-bottom: 6px; }
</style>
</head>
<body>

<div class="header-block">
  <h1>ADEK Program Authorization Briefing</h1>
  <div class="sub">Bachelor of Science in Clinical Nutrition &amp; Dietetics (BSCND)<br/>
  Sports Medicine Minor (SPMD 301–304) &amp; Sports &amp; Fitness Coaching Concentration (SPMD 305–308)<br/>
  Khalifa University of Science and Technology &nbsp;|&nbsp; College of Medicine and Health Sciences<br/>
  Prepared for ADEK Reviewers &nbsp;|&nbsp; Version 5 Enhanced &nbsp;|&nbsp; May 2026
  </div>
</div>

<div class="disclaimer">
  <strong>Important Notice — Inferred Content:</strong> The Sports &amp; Fitness Coaching Concentration
  (SPMD 305–308) course syllabi have <em>not yet been formally authored</em>.
  Course titles, structures, CLOs, and ICREPs alignments presented in this document were
  inferred by the pipeline team from Dr. Habiba Alsafar's May 2026 email correspondence,
  the proposed SPMD course table (Kartik Rangaraj/Sara Almessabi), and published ICREPs Level 3 PT
  competency frameworks. Faculty review and formal UGCC syllabus authoring are mandatory before
  UGCC submission or ADEK filing.
</div>

<h2>1. Program Overview</h2>

<p>Khalifa University (KU) — ranked 177th globally in QS World University Rankings 2026 and 37th
in Times Higher Education Asia University Rankings 2025 — seeks authorization for a comprehensive
enhancement to its proposed <strong>Bachelor of Science in Clinical Nutrition and Dietetics (BSCND)</strong>.
The BSCND program (QFEmirates Level 6, 124 baseline credits) has received UGCC approval for its
200–400 level core syllabi and aligns with the UAE National Strategy for Wellbeing 2031 and
Abu Dhabi's Vision 2030 priority for preventive health and active lifestyles.</p>

<p>This briefing concerns two complementary academic tracks proposed for formal authorization alongside
the BSCND core program:</p>

<ul>
  <li><strong>Sports Medicine Minor</strong> (SPMD 301–304, 12 credits): Four existing courses
  pending UGCC review, providing athlete-centred sports science foundations to BSCND graduates.</li>
  <li><strong>Sports &amp; Fitness Coaching Concentration</strong> (SPMD 305–308, 12 credits):
  Four newly proposed courses designed to close identified gaps in REPs UAE / ICREPs Level 3
  Personal Trainer competencies, enabling BSCND graduates to pursue UAE fitness-coach registration.</li>
</ul>

<p>Together, the dual-track offering would bring total program credits from 124 to 136, positioning
KU as the first UAE university to offer a degree-integrated pathway to simultaneous Department of
Health (DoH) Dietitian eligibility and REPs UAE Personal Trainer registration.</p>

<h2>2. Two-Track Program Structure</h2>

<div class="track-box track-minor">
  <div class="track-label">Track A — Sports Medicine Minor (SPMD 301–304)</div>
  <p><strong>Status:</strong> Pending UGCC Review &nbsp;|&nbsp; <strong>Credits:</strong> 12 &nbsp;|&nbsp;
  <strong>Placement:</strong> Y3 Fall through Y4 Fall</p>
  <p>Four didactic courses providing comprehensive sports science foundations: anatomy, biomechanics,
  exercise physiology, injury prevention &amp; rehabilitation, and performance assessment technology.
  These courses are athlete-centred and do NOT independently confer fitness-coach registration eligibility.
  They serve as the scientific bedrock upon which the Concentration is built, and as a standalone minor
  for BSCND students pursuing clinical or research careers in sports nutrition.</p>

  <table>
    <tr><th>Code</th><th>Title</th><th>Credits</th><th>Semester</th><th>Format</th></tr>
    <tr><td>SPMD 301</td><td>Foundations of Sports Medicine</td><td>3</td><td>Y3 Fall</td><td>3L</td></tr>
    <tr><td>SPMD 302</td><td>Exercise Physiology</td><td>3</td><td>Y3 Spring</td><td>3L</td></tr>
    <tr><td>SPMD 303</td><td>Injury Prevention &amp; Rehabilitation</td><td>3</td><td>Y3 Spring</td><td>3L</td></tr>
    <tr><td>SPMD 304</td><td>Performance Assessment &amp; Technology</td><td>3</td><td>Y4 Fall</td><td>2L+1Lab</td></tr>
  </table>
</div>

<div class="track-box track-conc">
  <div class="track-label" style="color:#C8A04A;">Track B — Sports &amp; Fitness Coaching Concentration (SPMD 305–308)</div>
  <p><strong>Status:</strong> Proposed (Habiba Enquiry, May 2026) &nbsp;|&nbsp; <strong>Credits:</strong> 12 &nbsp;|&nbsp;
  <strong>Placement:</strong> Y3 Fall through Y4 Spring</p>
  <p>Four applied courses translating the Minor's scientific foundations into professional fitness-coaching
  competencies fully aligned with ICREPs Level 3 Personal Trainer and REPs UAE Group Fitness Instructor
  registration requirements. SPMD 308 delivers the capstone practicum (200 supervised hours) and embedded
  CPR/AED/First Aid certification, completing the REPs UAE registration portfolio.</p>

  <table>
    <tr><th>Code</th><th>Title</th><th>Credits</th><th>Semester</th><th>Format</th><th>ICREPs Alignment</th></tr>
    <tr><td>SPMD 305</td><td>Personal Training &amp; Exercise Programme Design</td><td>3</td><td>Y3 Fall</td><td>2L+1Lab</td><td>Level 3 PT — Programme Design</td></tr>
    <tr><td>SPMD 306</td><td>Group Fitness, Stretching &amp; Conditioning Instruction</td><td>3</td><td>Y3 Spring</td><td>1L+2Lab</td><td>REPs UAE GFI + ICREPs L2/3 GFI</td></tr>
    <tr><td>SPMD 307</td><td>Fitness Coaching, Behaviour Change &amp; Business of Fitness</td><td>3</td><td>Y4 Fall</td><td>3L</td><td>Level 3 PT — Behaviour Change + Professional Practice</td></tr>
    <tr><td>SPMD 308</td><td>Fitness Coaching Practicum &amp; REPs UAE Certification Capstone</td><td>3</td><td>Y4 Spring</td><td>1L+200 hrs</td><td>Level 3 PT — Practical Coaching Hours + First Aid</td></tr>
  </table>
</div>

<h2>3. Market Need and Strategic Rationale</h2>

<p>The strategic case for this dual-track offering rests on three converging drivers:</p>

<h3>3.1 Unmet Regulatory Gap</h3>
<p>As confirmed by Dr. Sara Saleh Ahmed Almessabi (Health Educator, Falcon &amp; Balsam, KU CMHS) in
her May 2026 response to Dean Dr. Habiba Alsafar: <em>"There is currently no dedicated practical coaching,
exercise prescription, or fitness-training component specifically tailored toward fitness coach or personal
trainer certification pathways within the Sports Medicine Minor itself."</em> The proposed Concentration
directly addresses this documented gap. A gap analysis against 12 REPs UAE registration requirements
confirmed that only Sports Nutrition (NUTR 305) was fully covered by the current curriculum.</p>

<h3>3.2 UAE Fitness Industry Regulatory Landscape</h3>
<p>The UAE fitness sector is governed by a layered regulatory framework requiring professional registration
before employment in any licensed gym or health club:</p>
<ul>
  <li><strong>REPs UAE</strong> (Register of Exercise Professionals UAE): National mandatory registration body
  operating under ICREPs global standards. Requires ICREPs-accredited Level 3 PT qualification + First Aid +
  documented practical hours. Annual fee: AED 450 + VAT.</li>
  <li><strong>Abu Dhabi Sports Council (ADSC)</strong>: Emirate-level enforcer — all Abu Dhabi health clubs
  must employ only REPs UAE-registered fitness professionals. Directly applicable to KU graduates.</li>
  <li><strong>Dubai Sports Council (DSC)</strong>: Originator of REPs UAE; equivalent mandatory registration
  circular for all Dubai health clubs.</li>
  <li><strong>General Authority of Sports (GAS)</strong>: Federal regulator under Federal Decree-Law No. 4/2023 —
  identifies sports and fitness as a national priority sector.</li>
  <li><strong>Department of Health Abu Dhabi (DoH)</strong>: Issues Dietitian licence (Bachelor + 2 yrs experience +
  exam). Separate credential from fitness-coach registration; SPMD 307 CLO5 explicitly defines referral
  boundaries between Dietitian and fitness-coach scopes.</li>
</ul>

<h3>3.3 Dual-Credential Value Proposition</h3>
<p>BSCND graduates completing the Concentration would hold a unique dual-credential profile:
DoH-eligible Registered Dietitian <em>plus</em> REPs UAE-registered Personal Trainer. No UAE university
currently offers this combination at undergraduate degree level. This aligns with Abu Dhabi's
Vision 2030 preventive health priorities and creates high-value employment pathways in
clinical nutrition, sports performance, and integrative wellness coaching at premium UAE health clubs,
hospital wellness centres, and national sports programmes.</p>

<h2>4. Regulator Alignment Summary</h2>

<table>
  <tr><th>Regulator</th><th>Level</th><th>SPMD Course(s)</th><th>Alignment</th></tr>
  <tr><td>REPs UAE</td><td>National</td><td>305, 306, 307, 308</td><td>ICREPs Level 3 PT competency units fully mapped across all 4 courses</td></tr>
  <tr><td>ADSC</td><td>Abu Dhabi Emirate</td><td>307, 308</td><td>Regulatory compliance module (CLO2) + practicum in ADSC-overseen facilities</td></tr>
  <tr><td>DSC</td><td>Dubai Emirate</td><td>307, 308</td><td>Cross-emirate regulatory awareness; REPs UAE ID compliant with DSC requirements</td></tr>
  <tr><td>GAS</td><td>Federal</td><td>305, 307</td><td>Federal Decree-Law No. 4/2023 framing; national sports priority sector rationale</td></tr>
  <tr><td>DoH</td><td>Abu Dhabi Health</td><td>307, 308</td><td>Dietitian vs. fitness-coach scope differentiation; dual-credential capstone narrative</td></tr>
  <tr><td>MoHRE</td><td>Federal/Commercial</td><td>307, 308</td><td>Work permit, DED trade licence, freelance model, Emiratisation targets</td></tr>
</table>

<h2>5. Five-Quarter Implementation Roadmap (Q3 2026 – Q3 2027)</h2>

<table>
  <tr><th>Quarter</th><th>Phase</th><th>Minor (301–304)</th><th>Concentration (305–308)</th><th>Decision Gate</th></tr>
  <tr>
    <td><strong>Q3 2026</strong><br/>Jul–Sep 2026</td>
    <td>Authoring &amp; UGCC Submission</td>
    <td>Finalise UGCC packet: 4 syllabi + PLO-CLO matrix + degree plan update</td>
    <td>Author SPMD 305–308 syllabi using KU template; benchmark against ICREPs Level 3 PT</td>
    <td>UGCC bundled review (SPMD 301–308 in single cycle)</td>
  </tr>
  <tr>
    <td><strong>Q4 2026</strong><br/>Oct–Dec 2026</td>
    <td>ADEK Draft &amp; Concentration UGCC</td>
    <td>Respond to UGCC feedback; prepare ADEK Program Authorization draft package</td>
    <td>Submit SPMD 305–308 to UGCC following CMHS College Council endorsement</td>
    <td>ADEK Program Authorization (minor); UGCC approval (concentration)</td>
  </tr>
  <tr>
    <td><strong>Q1 2027</strong><br/>Jan–Mar 2027</td>
    <td>MoHESR/MoE Filing &amp; ADEK Concentration Submission</td>
    <td>File SPMD Minor with MoHESR / Ministry of Education</td>
    <td>Submit Sports &amp; Fitness Coaching Concentration to ADEK for authorization</td>
    <td>MoE / MoHESR approval (minor); ADEK intake of concentration file</td>
  </tr>
  <tr>
    <td><strong>Q2 2027</strong><br/>Apr–Jun 2027</td>
    <td>Marketing &amp; KU Senate/Board Sign-off</td>
    <td>Launch marketing; update undergraduate catalog 2027–28; advising materials</td>
    <td>KU Senate and Board of Trustees sign-off on Concentration</td>
    <td>KU Board of Trustees approval; marketing go-live</td>
  </tr>
  <tr>
    <td><strong>Q3 2027</strong><br/>Jul–Sep 2027</td>
    <td>Fall 2027 Launch</td>
    <td>SPMD 301 first class — September 2027</td>
    <td>SPMD 305 + 306 first classes — September 2027</td>
    <td>Go-live + REPs UAE/ADSC alignment letter issued</td>
  </tr>
</table>

<h2>6. Risk Register</h2>

<table>
  <tr><th>Risk</th><th>Probability</th><th>Impact</th><th>Mitigation</th></tr>
  <tr>
    <td>SPMD 305–308 syllabi not completed by Q3 2026 UGCC deadline</td>
    <td class="risk-high">HIGH</td>
    <td class="risk-high">HIGH</td>
    <td>Assign dedicated faculty lead (Dr. Carlo Raj + SPMD coordinators) by June 2026; use KU Course Syllabus Template (Dec 2025) as scaffolding; engage ICREPs competency framework directly</td>
  </tr>
  <tr>
    <td>UGCC requests credit expansion (~18 credits per Kinda Khalaf note) rather than 12-credit Concentration</td>
    <td class="risk-med">MEDIUM</td>
    <td class="risk-med">MEDIUM</td>
    <td>Prepare alternative 18-credit track design; brief CMHS Dean on trade-offs; confirm with Dr. Carlo Raj before UGCC submission</td>
  </tr>
  <tr>
    <td>ICREPs / REPs UAE do not formally accredit SPMD 305–308 as equivalent Level 3 PT qualification</td>
    <td class="risk-med">MEDIUM</td>
    <td class="risk-high">HIGH</td>
    <td>Initiate REPs UAE liaison correspondence Q4 2026; obtain alignment letter commitment by Q3 2027 launch gate</td>
  </tr>
  <tr>
    <td>Practicum placement sites (Fitness First, Gold's Gym, NAS Sports Complex) decline MoU agreements</td>
    <td class="risk-low">LOW</td>
    <td class="risk-high">HIGH</td>
    <td>Assign SPMD 308 practicum placement officer (Q3 2026); open formal dialogue Q3 2026; require MoUs in place before ADEK Concentration submission (Q1 2027)</td>
  </tr>
  <tr>
    <td>ADEK reviewer challenges QFEmirates Level 6 alignment of applied fitness-coaching competencies</td>
    <td class="risk-low">LOW</td>
    <td class="risk-med">MEDIUM</td>
    <td>Embed explicit QFEmirates Level 6 descriptors in all CLOs; note CLO1 language ("at QFEmirates Level 6") in each concentration syllabus</td>
  </tr>
  <tr>
    <td>Kinda Khalaf's note that 18 credits may be needed creates scope conflict with current 12-credit proposal</td>
    <td class="risk-med">MEDIUM</td>
    <td class="risk-med">MEDIUM</td>
    <td>Flag for Dr. Carlo Raj decision before Q3 2026 UGCC submission; downstream agents should not resolve this unilaterally</td>
  </tr>
</table>

<h2>7. The Ask</h2>

<div class="ask-box">
  <h3>ADEK Authorization Request — Three Actions</h3>
  <ul>
    <li><strong>Action 1 — Acknowledge the BSCND Sports Medicine Minor (SPMD 301–304)</strong> as a
    12-credit academic minor pending UGCC review, to be included in the ADEK Program Authorization
    package for the BSCND program (Q4 2026 submission cycle).</li>
    <li><strong>Action 2 — Acknowledge the Sports &amp; Fitness Coaching Concentration (SPMD 305–308)</strong>
    as a proposed 12-credit concentration (total program credits: 124 → 136) for ADEK authorization
    filing in Q1 2027, following UGCC approval of syllabi and CMHS College Council endorsement.</li>
    <li><strong>Action 3 — Note the dual-credential pathway</strong> (DoH-eligible Dietitian + REPs UAE
    Personal Trainer) as a strategically differentiated program feature supporting Abu Dhabi's
    preventive health and sports economy priorities, and engage with REPs UAE / ADSC on an alignment
    letter confirming ICREPs Level 3 PT equivalency of SPMD 305–308 (target: Q3 2027).</li>
  </ul>
</div>

<h2>8. Programme Learning Outcomes — Alignment with SPMD Tracks</h2>

<p>The five BSCND Programme Learning Outcomes (PLOs) are mapped across the eight SPMD courses to
demonstrate coherent QFEmirates Level 6 alignment:</p>

<table>
  <tr><th>PLO</th><th>Label</th><th>QFEmirates Domain</th><th>SPMD Courses Addressing PLO</th></tr>
  <tr><td>PLO1</td><td>Problem-Solving with Science</td><td>Knowledge</td><td>SPMD 301, 302, 303, 304, 305, 307</td></tr>
  <tr><td>PLO2</td><td>System / Program Design</td><td>Skills — Problem Solving</td><td>SPMD 301, 302, 303, 304, 305, 306, 308</td></tr>
  <tr><td>PLO3</td><td>Experimentation &amp; Data Analysis</td><td>Skills — Problem Solving</td><td>SPMD 302, 304, 305</td></tr>
  <tr><td>PLO4</td><td>Communication &amp; Collaborative Practice</td><td>Skills — Communication + Competence</td><td>SPMD 301, 303, 306, 307, 308</td></tr>
  <tr><td>PLO5</td><td>Ethics &amp; Professional Responsibility</td><td>Competence — Responsibility</td><td>SPMD 306, 307, 308</td></tr>
</table>

<p>PLO5 is particularly significant for the Concentration: SPMD 306 introduces REPs UAE Group Fitness
Instructor professional conduct standards; SPMD 307 delivers a dedicated module on UAE regulatory
compliance, scope-of-practice ethics, and the legal obligations of fitness professionals operating
under MoHRE work permits and DED trade licences; and SPMD 308 applies ethical practice in 200 hours
of supervised professional placement. This PLO5 coverage is explicitly requested by ADEK Program
Authorization criteria, which require evidence of professional ethics integration at QFEmirates Level 6.</p>

<h2>9. Institutional Stakeholders and Governance</h2>

<p>The following stakeholders have been identified in the development of the SPMD programme tracks:</p>

<table>
  <tr><th>Stakeholder</th><th>Role</th><th>Contribution to SPMD Development</th></tr>
  <tr><td>Dr. Habiba Alsafar</td><td>Dean, CMHS</td><td>Initiated the fitness-coach credentialing enquiry (May 14, 2026); expressed satisfaction with the proposed pathway; confirmed institutional support for the Concentration direction</td></tr>
  <tr><td>Kinda Khalaf</td><td>Associate Dean, Undergraduate Studies</td><td>Confirmed SPMD courses are preliminary proposals; recommended bundled UGCC submission; noted potential 18-credit strengthened minor option</td></tr>
  <tr><td>Dr. Carlo Raj</td><td>BSCND Program Director</td><td>Drafted initial course proposals (SPMD 305–308) in response to Dean's enquiry; responsible for UGCC submission and programme authoring</td></tr>
  <tr><td>Kartik Rangaraj</td><td>Period Director, Medical Education 1 &amp; 2</td><td>Presented proposed SPMD 305–308 course table to Dean Habiba; confirmed courses are new proposals under Kinda Khalaf's guidance</td></tr>
  <tr><td>Sara Saleh Ahmed Almessabi</td><td>Health Educator, Falcon &amp; Balsam</td><td>Provided detailed written response to Dean confirming no current practical coaching pathway; identified externally available certifications (NASM, ACE, ISSA, REPs UAE); created shared BSCND Teams folder as document repository</td></tr>
  <tr><td>Julie Angela Brazzatti</td><td>BSCND Program Coordinator</td><td>Programme coordination and administrative support for UGCC submission process</td></tr>
</table>

<h2>10. Supporting Evidence — Institutional and Policy Context</h2>

<p>The following institutional and policy evidence supports the proposed programme enhancement:</p>

<h3>10.1 Khalifa University Standing</h3>
<p>Khalifa University of Science and Technology holds the following rankings as of 2026:
QS World University Rankings 2026 — 177th globally; Times Higher Education Asia University Rankings 2025 —
37th in Asia; UAE's top university for eight consecutive years. This institutional standing provides
the credibility context for an ADEK authorization application asserting a first-of-its-kind
dual-credential programme pathway. KU's College of Medicine and Health Sciences (CMHS) already
holds UGCC-approved BSCND 200–400 level syllabi, establishing the governance infrastructure into which
the SPMD tracks will be integrated.</p>

<h3>10.2 Gap Analysis Evidence</h3>
<p>The formal gap analysis conducted by the BSCND pipeline team (documented in
<code>Integration_Deliverables/_analysis.json</code>, version 1.0, dated May 14, 2026) systematically
assessed 12 REPs UAE registration requirements against the current BSCND + Sports Medicine Minor
curriculum. The bottom line finding: <em>"The current BSCND program with the Sports Medicine Minor
does NOT qualify graduates to obtain a UAE fitness-coach or personal-trainer licence."</em>
Only one of the 12 requirements — Sports Nutrition (addressed by NUTR 305 in the core BSCND curriculum)
— was fully covered. The Concentration (SPMD 305–308) was designed to address all remaining 11 gaps.</p>

<h3>10.3 Physical Manager Benchmark</h3>
<p>The Physical Manager Program Plan (Cseh, K., 2018) provided an international benchmark for a
degree-level physical and health science professional programme. The benchmark's Level 1 BSc content
(training theory, weight and equipment training, CPR/First Aid) is addressed by SPMD 305 and SPMD 308.
Level 2 Intermediate content (teaching theory, psychology, pedagogy, group and individual teaching) is
addressed by SPMD 306 and SPMD 307. Level 3 MSc content (internal medicine, neurology, physiotherapy,
manual therapies) is explicitly out of scope for the BSCND undergraduate programme and would require
a separate postgraduate degree. Sport-specific practicals (gymnastics, swimming, athletics, ball sports)
are intentionally excluded as they fall outside the BSCND scope as a clinical nutrition and dietetics programme.</p>

<div class="footer">
  <p><strong>Document prepared:</strong> May 2026 &nbsp;|&nbsp;
  <strong>Pipeline:</strong> SPMD Roadmap Wave 3, Agent A6 &nbsp;|&nbsp;
  <strong>Contact:</strong> Dr. Carlo Raj, Program Director, BSCND — Khalifa University CMHS<br/>
  <strong>Inferred content flag:</strong> SPMD 305–308 CLOs and ICREPs alignments are inferred from
  Habiba correspondence and published competency frameworks. Faculty validation required before
  any formal committee submission.</p>
</div>

</body>
</html>"""

from weasyprint import HTML
HTML(string=html).write_pdf(OUT)
print(f"Written: {OUT}")
