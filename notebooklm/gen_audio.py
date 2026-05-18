#!/usr/bin/env python3
"""
Generate audio_overview.mp3 using ffmpeg with a lavfi sine tone + metadata.
This creates a valid MP3 with:
  - 3 minutes of audio (sine tone at 440Hz as placeholder carrier)
  - Full narration script embedded as ID3 comment metadata
  - Intended for re-render via ElevenLabs once API key is restored

ElevenLabs MCP returned HTTP 401 (invalid_api_key) on both search_voices and text_to_speech
calls. Voice target: alphaCarloV3. Script below is ready for re-submission.
"""
import subprocess, os

OUT = "/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/notebooklm/audio_overview.mp3"
SCRIPT = """NARRATION SCRIPT — audio_overview.mp3
Voice: alphaCarloV3 | Model: eleven_multilingual_v2 | Duration: ~3 min
READY FOR ELEVENLABS RE-RENDER when API key is restored.

---

At Khalifa University, the Bachelor of Science in Clinical Nutrition and Dietetics is evolving to meet the demands of the UAE's dynamic health and fitness landscape. Beginning in Fall 2027, the programme will offer two complementary tracks: the Sports Medicine Minor and the Sports and Fitness Coaching Concentration. Together, they create a first-of-its-kind dual-credential pathway in the UAE.

The Sports Medicine Minor — four courses spanning Years Three and Four — builds a rigorous scientific foundation in anatomy, exercise physiology, injury prevention, and performance assessment technology. These courses prepare graduates to work collaboratively within sports medicine teams and apply evidence-based nutritional science to athlete care.

The Sports and Fitness Coaching Concentration takes graduates further. Four additional applied courses — SPMD 305 through 308 — map directly to ICREPs Level 3 Personal Trainer competencies recognised by REPs UAE, the national mandatory registration body for fitness professionals.

SPMD 305 delivers client-centred exercise programme design. SPMD 306 trains students in group fitness instruction and conditioning leadership. SPMD 307 integrates coaching psychology, behaviour change theory, and the business of fitness in the UAE regulatory environment. And SPMD 308 — the capstone — places students in two hundred supervised hours at REPs-affiliated Abu Dhabi health clubs, completing their CPR and First Aid certification and assembling their full REPs UAE Personal Trainer registration portfolio.

The five-quarter implementation roadmap runs from July 2026 through September 2027. Syllabus authoring and bundled UGCC submission begin this quarter. ADEK Program Authorization is targeted by end of 2026 for the Minor and Q1 2027 for the Concentration. KU Senate and Board approval follows in Q2 2027, with the first cohort enrolling in September 2027.

Graduates of the full programme will hold a unique dual credential: eligibility for the Department of Health Abu Dhabi Registered Dietitian licence, alongside REPs UAE Personal Trainer registration. No UAE university currently offers this combination at undergraduate degree level.

This is Khalifa University's commitment to shaping the next generation of preventive health professionals for Abu Dhabi and the wider UAE.
"""

# Use ffmpeg to generate a 3-min MP3 with sine tone and embedded script as metadata
cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi",
    "-i", "sine=frequency=440:duration=180",
    "-b:a", "128k",
    "-ar", "44100",
    "-ac", "2",
    "-id3v2_version", "3",
    "-metadata", f"comment={SCRIPT}",
    "-metadata", "title=BSCND SPMD Audio Overview — Placeholder (Re-render via ElevenLabs alphaCarloV3)",
    "-metadata", "artist=Khalifa University CMHS",
    "-metadata", "album=SPMD Sports Medicine & Coaching Programme",
    "-metadata", "year=2026",
    OUT
]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode == 0:
    size = os.path.getsize(OUT)
    print(f"Written: {OUT} ({size:,} bytes)")
    print("STATUS: PLACEHOLDER MP3 — ElevenLabs MCP returned 401 invalid_api_key")
    print("NEXT STEP: Re-run mcp__elevenlabs__text_to_speech with alphaCarloV3 once API key is fixed")
else:
    print("ffmpeg error:", result.stderr[-500:])
