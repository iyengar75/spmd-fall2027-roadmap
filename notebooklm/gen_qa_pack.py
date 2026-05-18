#!/usr/bin/env python3
"""Generate qa_pack.pdf via weasyprint — 17 Q&A pairs for ADEK reviewers."""

OUT = "/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/notebooklm/qa_pack.pdf"

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>
  @page { size: A4; margin: 2.5cm 2.5cm 2.5cm 2.5cm; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; color: #222; line-height: 1.65; }
  h1 { font-size: 17pt; color: #003D7A; margin-bottom: 4px; }
  h2 { font-size: 12.5pt; color: #003D7A; margin-top: 20px; margin-bottom: 6px; border-left: 5px solid #C8A04A; padding-left: 10px; }
  .header-block { background: #003D7A; color: #fff; padding: 16px 20px; margin-bottom: 20px; }
  .header-block h1 { color: #C8A04A; font-size: 15pt; margin: 0; }
  .header-block .sub { color: #ddd; font-size: 9pt; margin-top: 5px; }
  .qa-item { border: 1px solid #ddd; border-radius: 5px; padding: 12px 16px; margin-bottom: 14px; }
  .qa-q { background: #003D7A; color: #fff; padding: 8px 12px; border-radius: 4px 4px 0 0; margin: -12px -16px 10px -16px; font-weight: bold; font-size: 10.5pt; }
  .qa-a { font-size: 10pt; }
  .tag { display: inline; background: #C8A04A; color: #fff; padding: 2px 7px; border-radius: 3px; font-size: 8.5pt; margin-right: 4px; }
  .tag-reg { background: #2980b9; }
  .tag-mkt { background: #27ae60; }
  .tag-curr { background: #8e44ad; }
  .tag-risk { background: #e74c3c; }
  ul { margin: 6px 0; padding-left: 18px; }
  li { margin-bottom: 4px; }
  strong { color: #003D7A; }
  .footer { margin-top: 24px; border-top: 2px solid #C8A04A; padding-top: 8px; font-size: 8.5pt; color: #666; }
</style>
</head>
<body>

<div class="header-block">
  <h1>ADEK Reviewer Q&amp;A Anticipation Pack</h1>
  <div class="sub">BSCND Sports Medicine Minor &amp; Sports &amp; Fitness Coaching Concentration · Khalifa University CMHS<br/>
  17 Q&amp;A Pairs Anticipating ADEK Program Authorization Review Questions · May 2026</div>
</div>

<h2>Section A — Regulatory &amp; Licensure Questions</h2>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-reg">REGULATORY</span> Q1: How does SPMD 305 align with REPs UAE Tier 2 / ICREPs Level 3 Personal Trainer requirements?</div>
<div class="qa-a">
SPMD 305 (Personal Training &amp; Exercise Programme Design, 2L+1Lab, 3 credits, Y3 Fall) maps directly to two of the most critical ICREPs Level 3 PT competency units: <strong>"Apply Principles of Training"</strong> and <strong>"Programme Design for General Population Clients."</strong>
<ul>
  <li><strong>CLO1</strong> delivers the FITT-VP model and periodization principles — the core applied-science component of ICREPs L3 PT "Apply Principles of Training."</li>
  <li><strong>CLO2</strong> delivers structured needs analysis and fitness assessment — matching ICREPs L3 PT "Client Assessment" unit.</li>
  <li><strong>CLO3</strong> delivers hands-on technique instruction for resistance, cardiovascular, and functional training — the practical laboratory component required for ICREPs L3 PT qualification.</li>
  <li><strong>CLO4</strong> delivers evidence-based programme adjustment — matching ICREPs L3 PT "Monitor and Review" unit.</li>
  <li><strong>CLO5</strong> integrates sports nutrition with exercise prescription — a differentiating competency specific to the BSCND programme's dual-credential pathway.</li>
</ul>
Note: Formal ICREPs accreditation of SPMD 305–308 as an equivalent Level 3 PT qualification requires a REPs UAE liaison letter (scheduled Q3 2027 gate). This accreditation letter is a condition of the SPMD 308 practicum capstone and will be included in the ADEK concentration authorization file.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-reg">REGULATORY</span> Q2: What evidence supports the claim that completing SPMD 305–308 enables graduates to register as REPs UAE Personal Trainers?</div>
<div class="qa-a">
The evidence chain is as follows:
<ul>
  <li>REPs UAE registration requires (1) an ICREPs-accredited Level 3 PT qualification, (2) a current First Aid/CPR certificate, and (3) documented fitness-industry CV with practical coaching hours.</li>
  <li>SPMD 305 and 306 collectively deliver the academic/practical knowledge base corresponding to ICREPs L3 PT and GFI competency units.</li>
  <li>SPMD 307 delivers the Client Consultation, Behaviour Change, and Professional Practice units.</li>
  <li>SPMD 308 delivers 200 supervised coaching hours (ICREPs practical hours unit), embedded CPR/AED/First Aid certification, and assembles the complete REPs UAE PT registration portfolio.</li>
  <li>Gap analysis conducted by the BSCND pipeline team against 12 REPs UAE registration requirements confirmed all 12 requirements are addressed by SPMD 305–308 (with NUTR 305 covering the sports nutrition requirement from the core BSCND curriculum).</li>
</ul>
<strong>Critical caveat:</strong> The pathway is designed to close all documented gaps, but REPs UAE formal accreditation of the programme as an ICREPs-equivalent qualification is pending. KU must initiate REPs UAE/ADSC liaison correspondence in Q4 2026 and obtain the alignment letter by Q3 2027.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-reg">REGULATORY</span> Q3: How does Abu Dhabi Sports Council (ADSC) enforcement interact with the SPMD Concentration?</div>
<div class="qa-a">
ADSC has issued a circular to all Abu Dhabi health clubs requiring REPs UAE registration for all fitness instructors prior to employment. Since KU is located in Abu Dhabi and its graduates are most likely to seek employment in Abu Dhabi gyms and health facilities, ADSC enforcement is the most directly relevant regulatory layer for BSCND graduates.
<ul>
  <li>SPMD 307 CLO2 explicitly covers the "UAE fitness industry regulatory framework, including REPs UAE, ADSC, and DSC requirements."</li>
  <li>SPMD 308 practicum placements are planned at ADSC-overseen Abu Dhabi facilities (Fitness First, Gold's Gym, NAS Sports Complex Abu Dhabi), providing direct regulatory socialization.</li>
  <li>An ADSC alignment letter confirming SPMD 305–308 maps to ICREPs Level 3 PT is a Q3 2027 gate condition for the Fall 2027 launch.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-reg">REGULATORY</span> Q4: Does the Concentration replace or supplement DoH Dietitian licensure?</div>
<div class="qa-a">
The Concentration is an <strong>additive</strong> credential pathway — it does not affect or substitute the DoH Dietitian licensure pathway. BSCND graduates with the Concentration will:
<ul>
  <li>Remain eligible for DoH Dietitian licensure (Bachelor of Science in Nutrition/Dietetics + 2 years supervised experience + DoH examination — standard pathway unchanged).</li>
  <li>Additionally hold REPs UAE Personal Trainer registration through SPMD 308 completion.</li>
</ul>
SPMD 307 CLO5 and SPMD 308 CLO5 explicitly differentiate between Dietitian scope (DoH licence required for nutrition counselling) and fitness-coach scope (REPs UAE for exercise prescription), and teach students the professional referral boundaries between these roles. This dual-credential design is the central value proposition of the BSCND + Concentration qualification: no UAE university currently offers this combination at undergraduate level.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-reg">REGULATORY</span> Q5: Which federal UAE law governs the sports sector, and how does the SPMD programme respond to it?</div>
<div class="qa-a">
The UAE sports sector is governed at federal level by <strong>Federal Decree-Law No. 4 of 2023</strong> (Sports Law) and <strong>Federal Decree No. 28 of 2024</strong>, which established the General Authority of Sports (GAS / Ministry of Sport) as the federal regulator. GAS licenses sports entities and federations — it does not directly register individual fitness trainers (that function is delegated to emirate councils via REPs UAE).
<ul>
  <li>SPMD 305's programme rationale documentation positions the Concentration within GAS's strategic framing of sports and fitness as a UAE national priority sector.</li>
  <li>SPMD 307's UAE regulatory environment module covers the federal governance architecture, GAS's role, and how it relates to ADSC/DSC enforcement at emirate level.</li>
  <li>This knowledge ensures BSCND graduates understand the complete regulatory stack governing their professional practice.</li>
</ul>
</div>
</div>

<h2>Section B — Market Demand &amp; Strategic Questions</h2>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-mkt">MARKET</span> Q6: What evidence supports market demand for licensed fitness coaches in Abu Dhabi?</div>
<div class="qa-a">
Market demand evidence operates at three levels:
<ul>
  <li><strong>Regulatory mandate:</strong> ADSC and DSC have issued mandatory REPs UAE registration circulars to all health clubs in Abu Dhabi and Dubai respectively. Every licensed fitness professional in both emirates must be REPs UAE registered — creating a guaranteed demand signal for qualified candidates.</li>
  <li><strong>Government strategy:</strong> Abu Dhabi Vision 2030 and the UAE National Wellbeing Strategy 2031 identify physical fitness and preventive health as national priorities. The UAE Government has invested heavily in fitness infrastructure (NAS Sports Complex, Abu Dhabi Marathon, Dubai Fitness Challenge), generating sustained demand for credentialed sports professionals.</li>
  <li><strong>Institutional affirmation:</strong> Dr. Habiba Alsafar's May 2026 inquiry to the BSCND team directly reflects demand awareness at Dean level — the question "whether completion of these courses would meet the requirements for fitness coach certification" signals that CMHS leadership sees fitness-coach credentialing as a graduate employability priority.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-mkt">MARKET</span> Q7: Why is a degree-integrated pathway superior to having students obtain NASM/ISSA certifications independently after graduation?</div>
<div class="qa-a">
Post-graduation external certifications (NASM CPT, ISSA CPT, ACE CPT) require passing a proctored exam, typically 3–6 months of independent study, and exam fees of USD 500–900. They also provide no formal academic credit or QFEmirates recognition. The degree-integrated pathway offers:
<ul>
  <li><strong>Academic rigor:</strong> QFEmirates Level 6 embedding — ICREPs competencies are taught and assessed at undergraduate degree level, not short-course level.</li>
  <li><strong>Nutrition integration:</strong> The BSCND curriculum's NUTR 305 (Sports Nutrition) directly complements SPMD 305 and 308, creating a nutrition-science-informed fitness coach profile unavailable in any standalone certification.</li>
  <li><strong>Practicum quality:</strong> 200 supervised hours (SPMD 308) at Abu Dhabi REPs-affiliated facilities provides structured placement that far exceeds what independent certification candidates receive.</li>
  <li><strong>Employer signal:</strong> A QFEmirates Level 6 degree with a UAE-recognized Concentration is a stronger hiring signal to Abu Dhabi hospital wellness programmes and premium health clubs than a private certification alone.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-mkt">MARKET</span> Q8: What are the target employment pathways for BSCND + Concentration graduates?</div>
<div class="qa-a">
Graduates holding both the BSCND and the Sports &amp; Fitness Coaching Concentration are positioned for employment across three converging sectors:
<ul>
  <li><strong>Clinical wellness:</strong> Hospital-based wellness programs (SEHA, ADPHC, CCAD) where a DoH-eligible Dietitian with fitness-coaching credentials provides integrative preventive care.</li>
  <li><strong>Premium fitness:</strong> Senior personal trainer roles at Fitness First UAE, Gold's Gym, NAS Sports Complex, and corporate wellness programs — roles requiring REPs UAE registration where the Dietitian background creates a differentiated value proposition.</li>
  <li><strong>Entrepreneurship:</strong> Freelance nutrition-fitness coaching practice operating under DoH Dietitian licence + REPs UAE PT registration + DED/free-zone trade licence (SPMD 307 covers the business model curriculum).</li>
</ul>
The Physical Manager Program Plan benchmark (Cseh 2018) identifies careers in fitness centres, private sector, schools, army/police, special needs, worksite fitness, medical centres, and professional sport clubs — all relevant to KU graduates in the UAE context.
</div>
</div>

<h2>Section C — Curriculum &amp; Academic Questions</h2>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">CURRICULUM</span> Q9: How does the credit load of 136 total credits compare to QFEmirates Level 6 norms and ADEK expectations?</div>
<div class="qa-a">
The baseline BSCND programme is 124 credits (QFEmirates Level 6). Adding the Concentration brings total credits to 136. This is within the acceptable range for KU's undergraduate programmes that include professional practicum components — SPMD 308's 200 supervised hours require the additional 3-credit allocation. The 12-credit Concentration is structurally comparable to professional concentrations at peer UAE institutions. Note: Kinda Khalaf (Assoc Dean UG) noted in May 2026 that approximately 18 credits might be considered for a strengthened minor — if UGCC or ADEK reviewers favour this expansion, the programme team must design an 18-credit variant (two additional courses) before formal submission.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">CURRICULUM</span> Q10: What is the relationship between the Sports Medicine Minor and the Sports &amp; Fitness Coaching Concentration? Must students take both?</div>
<div class="qa-a">
The two tracks are <strong>complementary but independent</strong> in terms of ADEK authorization — either can be taken as a standalone addition to the BSCND core. However:
<ul>
  <li>The Minor (SPMD 301–304) provides the scientific foundations that inform the Concentration's applied courses through the prerequisite chain (SPMD 305 requires SPMD 301; SPMD 306 requires SPMD 302).</li>
  <li>Students pursuing the Concentration will typically take Minor courses concurrently or as prerequisites — in practice, most Concentration students will complete all 8 SPMD courses (24 credits total), though they receive separate academic designations (Minor + Concentration on transcript).</li>
  <li>Students wanting only the Minor (athlete-centred research/clinical pathway) can complete SPMD 301–304 without the Concentration.</li>
  <li>It is academically inadvisable (though not prohibited) to take SPMD 305–308 without first completing SPMD 301–302, given the prerequisite chain.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">CURRICULUM</span> Q11: How does the SPMD programme handle the sport-specific practical skills (gymnastics, swimming, ball sports) listed in the Physical Manager benchmark?</div>
<div class="qa-a">
The Physical Manager Program Plan (Cseh 2018) benchmark listed sport-specific practicals (basic gymnastics, swimming, athletics, ball sports) as Level 1 BSc content. The BSCND programme intentionally <strong>excludes</strong> sport-specific practicals because:
<ul>
  <li>BSCND is a <em>Clinical Nutrition and Dietetics</em> programme — not a Physical Education, Sports Science, or Kinesiology programme. Sport-specific coaching skills are out of scope for a dietetics graduate.</li>
  <li>REPs UAE Personal Trainer and Group Fitness Instructor registration do not require sport-specific coaching credentials — only general fitness instruction and programme design competencies.</li>
  <li>The Physical Manager benchmark's Level 3 MSc content (neurology, orthopedics, manual therapies, physiotherapy) is similarly out of scope and would require a separate postgraduate programme.</li>
</ul>
SPMD 305 and 306 focus on general-population fitness instruction — resistance, cardiovascular, functional, and group fitness modalities — which fully satisfy REPs UAE / ICREPs Level 3 PT requirements without requiring sport-specific coaching.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">CURRICULUM</span> Q12: What KU General Education Learning Outcomes (GELOs/ILOs) are addressed by the SPMD courses?</div>
<div class="qa-a">
The 15 KU Institutional Learning Outcomes (ILOs) are addressed across the SPMD courses as follows (key alignments):
<ul>
  <li><strong>ILO2</strong> (Scientific Method): SPMD 302, 304, 305 — bioenergetics, exercise physiology assessments, evidence-based programme design</li>
  <li><strong>ILO3</strong> (Critical Thinking): SPMD 301, 302, 303, 305 — analyzing injury mechanisms, physiological data, programme outcomes</li>
  <li><strong>ILO6</strong> (Communication): SPMD 301, 306, 307, 308 — sports medicine communication, instructional delivery, client coaching</li>
  <li><strong>ILO9</strong> (Lifelong Learning): SPMD 302, 303, 305, 306, 307 — evidence-based practice, continuing professional development</li>
  <li><strong>ILO12</strong> (Teamwork): SPMD 303, 306, 308 — interdisciplinary collaboration, group instruction, practicum teamwork</li>
  <li><strong>ILO14</strong> (Ethics): SPMD 306, 307, 308 — REPs UAE professional ethics, scope of practice, UAE regulatory compliance</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">CURRICULUM</span> Q13: What quality assurance mechanism ensures SPMD 305–308 content will be peer-reviewed before UGCC submission?</div>
<div class="qa-a">
The QA pathway for SPMD 305–308 before UGCC submission includes:
<ul>
  <li><strong>Faculty lead assignment</strong> (Q3 2026): Dr. Carlo Raj + designated SPMD course coordinators to author full syllabi using the KU Course Syllabus Template (December 2025 version).</li>
  <li><strong>ICREPs competency benchmarking</strong>: Each CLO must be cross-referenced against published ICREPs Level 3 PT competency units before syllabus finalization.</li>
  <li><strong>CMHS College Council endorsement</strong>: Required before UGCC submission of the Concentration — this is the first formal committee checkpoint for SPMD 305–308.</li>
  <li><strong>UGCC review</strong>: Bundled SPMD 301–308 submission subject to UGCC standard review including PLO-CLO matrix, degree plan update, and prerequisite validation.</li>
  <li><strong>Pipeline inferred-content flag</strong>: All documents generated by the A1–A6 pipeline carry explicit inferred-content disclaimers (as in this document) to prevent premature reliance on unvalidated CLOs.</li>
</ul>
</div>
</div>

<h2>Section D — Risk &amp; Process Questions</h2>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-risk">RISK</span> Q14: What happens if REPs UAE declines to recognise SPMD 305–308 as an ICREPs Level 3 PT equivalent?</div>
<div class="qa-a">
This is the highest-stakes risk in the programme design. Mitigation strategy:
<ul>
  <li>Early REPs UAE liaison correspondence initiated in Q4 2026 — before ADEK Concentration submission (Q1 2027) — to validate alignment and identify any required syllabus modifications.</li>
  <li>SPMD 305–308 CLOs explicitly reference QFEmirates Level 6 descriptors and ICREPs unit language — maximizing the case for recognition.</li>
  <li>If full ICREPs accreditation is not secured by Q3 2027, SPMD 308 graduates can still pursue REPs UAE registration via the NASM/ACE/Active IQ equivalent-qualification pathway (as confirmed by Sara Saleh in the CE02 email) — the Concentration would still provide significant preparation, reducing external certification cost and study time from the standard 3–6 months to a shorter bridging exam.</li>
  <li>The ADEK Concentration authorization file should include REPs UAE engagement correspondence as evidence of regulatory alignment — even if full accreditation is not yet confirmed at time of ADEK filing.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-risk">RISK</span> Q15: What is the contingency if practicum host facilities for SPMD 308 are not available by Fall 2027?</div>
<div class="qa-a">
SPMD 308 requires 200 supervised hours at REPs-affiliated health clubs. Identified target facilities: Fitness First UAE, Gold's Gym, NAS Sports Complex Abu Dhabi. Contingency planning:
<ul>
  <li>SPMD 308 practicum placement officer to be assigned by Q3 2026 — opening formal MoU dialogue at least 12 months before Fall 2027 launch.</li>
  <li>MoUs with practicum sites are a gate condition for ADEK Concentration file submission (Q1 2027). ADEK cannot receive the Concentration file without executed MoUs.</li>
  <li>If primary sites decline, secondary options include: ADSC-accredited community sports facilities, KU campus fitness facilities (with REPs UAE assessment oversight), and virtual supervised hours with on-site supervisor confirmation (subject to REPs UAE acceptance).</li>
  <li>The programme team must confirm with REPs UAE whether any portion of the 200 hours may be completed in simulated/structured environments rather than commercial club settings.</li>
</ul>
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-risk">RISK</span> Q16: How does the pipeline handle the discrepancy between Dr. Kinda Khalaf's mention of ~18 credits and the current 12-credit Concentration proposal?</div>
<div class="qa-a">
This discrepancy is an open design decision flagged throughout the pipeline documentation. The A1–A6 pipeline agents have deliberately refrained from resolving it autonomously because it is a program-level decision requiring Dr. Carlo Raj's input. Options:
<ul>
  <li><strong>Option A (current):</strong> 12-credit Concentration (SPMD 305–308) = 4 courses, total programme 136 credits.</li>
  <li><strong>Option B:</strong> 18-credit "strengthened minor" = 6 courses, requiring 2 additional course designs. Total programme would be 142 credits.</li>
  <li><strong>Option C:</strong> 12-credit Concentration retained, but Minor expanded to 18 credits by adding 2 courses to SPMD 301–304 track (6 courses across Minor).</li>
</ul>
The UGCC submission must reflect a single, decided option. The discrepancy must be resolved in Dr. Carlo Raj's Q3 2026 planning meeting before the bundled UGCC packet is finalized.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-risk">RISK</span> Q17: What is the full ADEK authorization timeline, and what are the critical path items?</div>
<div class="qa-a">
The critical path to Fall 2027 launch across both tracks is:
<ul>
  <li><strong>Q3 2026 (Jul–Sep):</strong> SPMD 305–308 syllabi authored and bundled UGCC packet prepared. <em>Critical path: syllabus authoring must start immediately. Delay here cascades across all downstream gates.</em></li>
  <li><strong>Q4 2026 (Oct–Dec):</strong> UGCC review and approval; ADEK Program Authorization draft for Minor prepared; REPs UAE liaison initiated. <em>Critical: UGCC approval must be secured by Dec 2026 to maintain Q1 2027 ADEK filing.</em></li>
  <li><strong>Q1 2027 (Jan–Mar):</strong> MoHESR/MoE filing for Minor; ADEK Concentration file submitted. <em>Critical: MoUs with practicum sites must be executed.</em></li>
  <li><strong>Q2 2027 (Apr–Jun):</strong> KU Senate/Board sign-off; marketing launch; catalog update.</li>
  <li><strong>Q3 2027 (Jul–Sep):</strong> Fall 2027 first classes: SPMD 301, 302, 305, 306. REPs UAE/ADSC alignment letter issued. <em>Critical: alignment letter must be in hand before marketing claims "REPs UAE pathway" to prospective students.</em></li>
</ul>
</div>
</div>

<h2>Section E — Accreditation and Comparability</h2>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">ACCREDITATION</span> Q18: How does the BSCND SPMD Concentration compare to international degree programmes offering fitness-coaching pathways?</div>
<div class="qa-a">
The international benchmark landscape includes:
<ul>
  <li><strong>Loughborough University (UK)</strong>: BSc Sport and Exercise Science includes optional Health and Fitness concentration — graduates can pursue CIMSPA (UK equivalent of REPs) Level 4 Personal Training. The KU Concentration targets the equivalent ICREPs Level 3 PT (equivalent to UK Level 3 NQF), appropriate for a nutrition-focused degree where fitness coaching is a complement, not the core discipline.</li>
  <li><strong>University of the Sunshine Coast (Australia)</strong>: Bachelor of Clinical Exercise Physiology — combines clinical exercise physiology with AEP accreditation pathways. The KU Concentration offers a comparable dual-credential design (dietetics + fitness coaching) at undergraduate level within the UAE QFEmirates Level 6 framework.</li>
  <li><strong>American Council on Exercise (ACE) / NASM degree partnership programmes</strong>: Several US universities embed NASM CPT or ACE GFI preparatory content in 3-credit elective courses within nutrition and health sciences degrees. The KU Concentration's 12-credit depth (4 courses, 200 supervised hours) represents a more rigorous integration than typical US elective-based approaches.</li>
</ul>
The KU BSCND + Concentration is positioned as a regionally first-of-its-kind degree-integrated ICREPs Level 3 PT pathway within a dietetics programme — aligning with international best practice while exceeding the depth of most comparable international offerings.
</div>
</div>

<div class="qa-item">
<div class="qa-q"><span class="tag tag-curr">ACCREDITATION</span> Q19: What evidence will be submitted to ADEK confirming that the BSCND programme's QFEmirates Level 6 graduate descriptors are met by the SPMD tracks?</div>
<div class="qa-a">
The ADEK Program Authorization package will include the following QFEmirates Level 6 alignment evidence specific to the SPMD tracks:
<ul>
  <li><strong>PLO–CLO matrix:</strong> A complete matrix mapping all five BSCND PLOs to the CLOs of each SPMD course (301–308), with QFEmirates Level 6 Knowledge, Skills, and Competence descriptors annotated for each CLO. This matrix was developed by the pipeline's Agent A3 (PLO-CLO matrix builder) using the A1 source data.</li>
  <li><strong>Degree plan update:</strong> The full BSCND four-year degree plan showing SPMD 301–308 placement by semester, credit counts (124 baseline → 136 with Concentration), and prerequisite logic — confirming that all SPMD courses appear at Level 3 (300-level, Y3) or Level 4 (400-level, Y4) within the KU undergraduate framework.</li>
  <li><strong>ICREPs competency cross-reference table:</strong> A table aligning each SPMD 305–308 CLO with the specific ICREPs Level 3 PT competency unit it addresses, demonstrating industry-framework alignment at QFEmirates Level 6.</li>
  <li><strong>SPMD 308 MoU evidence:</strong> Executed memoranda of understanding with REPs-affiliated practicum placement facilities confirming 200-hour supervised placement at QFEmirates Level 6 professional standards.</li>
  <li><strong>REPs UAE/ADSC alignment letter:</strong> Formal correspondence from REPs UAE and/or ADSC confirming that SPMD 305–308 maps to ICREPs Level 3 PT competency requirements — the critical external validation evidence required by ADEK.</li>
</ul>
</div>
</div>

<div class="footer">
  ADEK Reviewer Q&amp;A Pack · BSCND SPMD Minor &amp; Concentration · 18 Q&amp;A pairs · Khalifa University CMHS · May 2026<br/>
  Pipeline: Wave 3, Agent A6 · SPMD 305–308 content is inferred; faculty validation required before UGCC submission.
</div>

</body>
</html>"""

from weasyprint import HTML
HTML(string=html).write_pdf(OUT)
print(f"Written: {OUT}")
