#!/usr/bin/env python3
"""Generate mind_map.png — KU Navy/Gold radial mind map."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

OUT = "/mnt/c/Users/TPOTMedXR/Desktop/SPMD_BSCND/notebooklm/mind_map.png"

KU_NAVY = "#003D7A"
KU_GOLD = "#C8A04A"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#d4e3f5"
LIGHT_GOLD = "#fff0d0"
GREEN = "#27ae60"
RED = "#c0392b"

fig, ax = plt.subplots(1, 1, figsize=(16, 16), dpi=150)
ax.set_xlim(-9, 9)
ax.set_ylim(-9, 9)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)

# -------- helper --------
def draw_node(ax, x, y, label, color, text_color=WHITE, fontsize=8.5, width=None, height=None,
              bold=False, radius=None, style='round,pad=0.3'):
    kw = dict(ha='center', va='center', fontsize=fontsize,
              color=text_color,
              fontweight='bold' if bold else 'normal',
              bbox=dict(boxstyle=style, facecolor=color, edgecolor='white', linewidth=1.2),
              zorder=5, wrap=True)
    ax.text(x, y, label, **kw)

def draw_edge(ax, x1, y1, x2, y2, color=KU_NAVY, lw=1.5, alpha=0.7):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, alpha=alpha, zorder=2)

def radial_point(cx, cy, angle_deg, r):
    a = math.radians(angle_deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)

# -------- CENTRE --------
cx, cy = 0, 0
ax.add_patch(plt.Circle((cx, cy), 1.15, color=KU_NAVY, zorder=4))
ax.text(cx, cy+0.18, "BSCND", ha='center', va='center', fontsize=12, color=KU_GOLD,
        fontweight='bold', zorder=6)
ax.text(cx, cy-0.22, "SPMD Programme", ha='center', va='center', fontsize=8.2, color=WHITE,
        fontweight='bold', zorder=6)
ax.text(cx, cy-0.55, "KU · CMHS", ha='center', va='center', fontsize=7.5, color=LIGHT_BLUE, zorder=6)

# -------- TRACK NODES --------
track_r = 3.0

# Minor track — left side (angle ~160°)
mx, my = radial_point(cx, cy, 155, track_r)
ax.add_patch(plt.Circle((mx, my), 0.9, color=KU_NAVY, zorder=4, linewidth=2))
ax.text(mx, my+0.1, "Sports Medicine\nMinor", ha='center', va='center', fontsize=8.5,
        color=WHITE, fontweight='bold', zorder=6)
ax.text(mx, my-0.42, "SPMD 301–304\n12 credits", ha='center', va='center', fontsize=7,
        color=KU_GOLD, zorder=6)
draw_edge(ax, cx, cy, mx, my, KU_NAVY, lw=2.5)

# Concentration track — right side (angle ~25°)
ex, ey = radial_point(cx, cy, 25, track_r)
ax.add_patch(plt.Circle((ex, ey), 0.9, color=KU_GOLD, zorder=4, linewidth=2))
ax.text(ex, ey+0.1, "Coaching\nConcentration", ha='center', va='center', fontsize=8.5,
        color=KU_NAVY, fontweight='bold', zorder=6)
ax.text(ex, ey-0.42, "SPMD 305–308\n12 credits", ha='center', va='center', fontsize=7,
        color=KU_NAVY, zorder=6)
draw_edge(ax, cx, cy, ex, ey, KU_GOLD, lw=2.5)

# -------- MINOR COURSES --------
minor_courses = [
    ("SPMD 301\nFoundations of\nSports Medicine", "Y3 Fall\n3L / 0Lab", 200),
    ("SPMD 302\nExercise\nPhysiology", "Y3 Spring\n3L / 0Lab", 155),
    ("SPMD 303\nInjury Prevention\n& Rehabilitation", "Y3 Spring\n3L / 0Lab", 120),
    ("SPMD 304\nPerformance Assessment\n& Technology", "Y4 Fall\n2L / 1Lab", 90),
]
for i, (title, detail, angle) in enumerate(minor_courses):
    nx, ny = radial_point(mx, my, angle, 2.5)
    ax.add_patch(plt.Circle((nx, ny), 0.82, color=LIGHT_BLUE, zorder=3, linewidth=1.5,
                             edgecolor=KU_NAVY))
    lines = title.split('\n')
    ax.text(nx, ny + 0.22, lines[0], ha='center', va='center', fontsize=7.5, color=KU_NAVY,
            fontweight='bold', zorder=6)
    for j, ln in enumerate(lines[1:]):
        ax.text(nx, ny + 0.22 - (j+1)*0.23, ln, ha='center', va='center', fontsize=7,
                color=KU_NAVY, zorder=6)
    ax.text(nx, ny - 0.52, detail, ha='center', va='center', fontsize=6.5, color="#555", zorder=6)
    draw_edge(ax, mx, my, nx, ny, KU_NAVY, lw=1.4)

    # Skills sub-nodes for SPMD 301
    if i == 0:
        skills = ["Anatomy &\nBiomechanics", "Injury\nMechanisms", "Team\nCare"]
        for k, sk in enumerate(skills):
            sa = angle + (k-1)*35
            sx, sy = radial_point(nx, ny, sa, 1.7)
            ax.text(sx, sy, sk, ha='center', va='center', fontsize=6.2, color=KU_NAVY,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#e8f0fb', edgecolor=KU_NAVY, linewidth=0.8),
                    zorder=5)
            draw_edge(ax, nx, ny, sx, sy, KU_NAVY, lw=0.9, alpha=0.5)
    elif i == 1:
        skills = ["Bioenergetics", "VO₂max\nTesting", "Cardio\nAdaptations"]
        for k, sk in enumerate(skills):
            sa = angle + (k-1)*35
            sx, sy = radial_point(nx, ny, sa, 1.7)
            ax.text(sx, sy, sk, ha='center', va='center', fontsize=6.2, color=KU_NAVY,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#e8f0fb', edgecolor=KU_NAVY, linewidth=0.8),
                    zorder=5)
            draw_edge(ax, nx, ny, sx, sy, KU_NAVY, lw=0.9, alpha=0.5)

# -------- CONCENTRATION COURSES --------
conc_courses = [
    ("SPMD 305\nPersonal Training\n& Programme Design", "Y3 Fall\n2L / 1Lab\nICREPs L3 PT", -25),
    ("SPMD 306\nGroup Fitness\n& Conditioning", "Y3 Spring\n1L / 2Lab\nGFI Competencies", 25),
    ("SPMD 307\nCoaching, Behaviour\nChange & Business", "Y4 Fall\n3L\nPro Practice", 60),
    ("SPMD 308\nPracticum &\nREPs Capstone", "Y4 Spring\n200 hrs + CPR/AED", 90),
]
for i, (title, detail, angle) in enumerate(conc_courses):
    nx, ny = radial_point(ex, ey, angle, 2.5)
    ax.add_patch(plt.Circle((nx, ny), 0.85, color=LIGHT_GOLD, zorder=3, linewidth=1.5,
                             edgecolor=KU_GOLD))
    lines = title.split('\n')
    ax.text(nx, ny + 0.24, lines[0], ha='center', va='center', fontsize=7.5, color=KU_NAVY,
            fontweight='bold', zorder=6)
    for j, ln in enumerate(lines[1:]):
        ax.text(nx, ny + 0.24 - (j+1)*0.24, ln, ha='center', va='center', fontsize=7,
                color=KU_NAVY, zorder=6)
    ax.text(nx, ny - 0.54, detail, ha='center', va='center', fontsize=6.2, color="#555", zorder=6)
    draw_edge(ax, ex, ey, nx, ny, KU_GOLD, lw=1.4)

    # Skills sub-nodes for 305 and 308
    if i == 0:
        skills = ["FITT-VP\nPeriodization", "Needs\nAnalysis", "Lab\nInstruction"]
        for k, sk in enumerate(skills):
            sa = angle + (k-1)*35
            sx, sy = radial_point(nx, ny, sa, 1.7)
            ax.text(sx, sy, sk, ha='center', va='center', fontsize=6.2, color=KU_NAVY,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#fff8e1', edgecolor=KU_GOLD, linewidth=0.8),
                    zorder=5)
            draw_edge(ax, nx, ny, sx, sy, KU_GOLD, lw=0.9, alpha=0.5)
    elif i == 3:
        skills = ["200 Supervised\nHours", "CPR/AED\nCertification", "REPs UAE\nPortfolio"]
        for k, sk in enumerate(skills):
            sa = angle + (k-1)*38
            sx, sy = radial_point(nx, ny, sa, 1.75)
            ax.text(sx, sy, sk, ha='center', va='center', fontsize=6.2, color=KU_NAVY,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#fff8e1', edgecolor=KU_GOLD, linewidth=0.8),
                    zorder=5)
            draw_edge(ax, nx, ny, sx, sy, KU_GOLD, lw=0.9, alpha=0.5)

# -------- REGULATOR NODE (bottom) --------
rx, ry = 0, -3.8
ax.add_patch(plt.Circle((rx, ry), 0.85, color="#2c3e50", zorder=4))
ax.text(rx, ry+0.12, "UAE Regulators", ha='center', va='center', fontsize=8.5, color=WHITE,
        fontweight='bold', zorder=6)
ax.text(rx, ry-0.28, "REPs UAE · ADSC · DSC\nGAS · DoH · MoHRE", ha='center', va='center',
        fontsize=6.5, color=LIGHT_GOLD, zorder=6)
draw_edge(ax, cx, cy, rx, ry, "#2c3e50", lw=2.0)

reg_items = [
    ("REPs UAE\nPersonal Trainer\nRegistration", -2.2, -5.8),
    ("ADSC\nAbu Dhabi\nEnforcement", 0, -6.0),
    ("DoH\nDietitian\nLicensure", 2.2, -5.8),
]
for label, bx, by in reg_items:
    ax.text(bx, by, label, ha='center', va='center', fontsize=6.5, color="#2c3e50",
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f0f4f8', edgecolor='#2c3e50', linewidth=0.9),
            zorder=5)
    draw_edge(ax, rx, ry, bx, by, "#2c3e50", lw=0.9, alpha=0.5)

# -------- OUTCOME NODE (top) --------
ox, oy = 0, 4.0
ax.add_patch(plt.Circle((ox, oy), 0.88, color=GREEN, zorder=4))
ax.text(ox, oy+0.18, "Dual Credential", ha='center', va='center', fontsize=8.5, color=WHITE,
        fontweight='bold', zorder=6)
ax.text(ox, oy-0.28, "Dietitian + REPs PT", ha='center', va='center', fontsize=7.5, color=WHITE, zorder=6)
draw_edge(ax, cx, cy, ox, oy, GREEN, lw=2.0)

outcome_items = [
    ("Clinical\nWellness\nCareers", -2.0, 5.8),
    ("Premium\nFitness\nIndustry", 0, 6.2),
    ("Nutrition-\nFitness\nEntrepreneurship", 2.1, 5.8),
]
for label, bx, by in outcome_items:
    ax.text(bx, by, label, ha='center', va='center', fontsize=6.5, color="#1a5c35",
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#d5f5e3', edgecolor=GREEN, linewidth=0.9),
            zorder=5)
    draw_edge(ax, ox, oy, bx, by, GREEN, lw=0.9, alpha=0.5)

# -------- TITLE & LEGEND --------
ax.text(0, 8.6, "BSCND Sports Medicine & Coaching Programme", ha='center', va='center',
        fontsize=15, color=KU_NAVY, fontweight='bold')
ax.text(0, 8.1, "Khalifa University · College of Medicine and Health Sciences · Fall 2027 Launch",
        ha='center', va='center', fontsize=9.5, color="#555")

legend_patches = [
    mpatches.Patch(color=KU_NAVY, label='Sports Medicine Minor (SPMD 301–304)'),
    mpatches.Patch(color=KU_GOLD, label='Coaching Concentration (SPMD 305–308)'),
    mpatches.Patch(color=GREEN, label='Dual-Credential Graduate Outcomes'),
    mpatches.Patch(color="#2c3e50", label='UAE Regulatory Framework'),
]
ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.01),
          ncol=2, fontsize=7.5, frameon=True, fancybox=True, shadow=True)

ax.text(0, -8.7, "* SPMD 305–308 content inferred from Habiba correspondence + ICREPs competency framework. Faculty validation required.",
        ha='center', va='center', fontsize=7, color='#888', style='italic')

plt.tight_layout()
plt.savefig(OUT, dpi=150, bbox_inches='tight', facecolor=WHITE)
plt.close()
print(f"Written: {OUT}")
