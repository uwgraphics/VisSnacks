"""Draft figure: the NOIR levels of measurement as a ladder.

Renders the four levels of measurement as accumulating rungs, so the
"each rung supports every operation below it, plus one more" property is
visible rather than merely asserted. Also shows categorical as a closed,
finite subset of nominal.

Deliberately does NOT repeat the level descriptions or examples - those
live in the page's table. This figure carries only the ladder property.

Outputs into the page bundle:
    content/tutorials/data-abstraction-cheat-sheet/noir-ladder.{svg,png}

Run:  /opt/anaconda3/envs/p314/bin/python Workspace/Tools/noir_ladder.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

OUT = Path("content/tutorials/data-abstraction-cheat-sheet")

INK, MUTED, HAIR = "#1a1a1a", "#6b6b6b", "#d6d6d6"
NEW_FILL, NEW_EDGE = "#dbeafe", "#3b6fb0"      # the operation this rung adds
OLD_FILL, OLD_EDGE = "#f4f4f4", "#c9c9c9"      # inherited from below
CAT_EDGE = "#b8860b"

# bottom -> top: level, the operation it ADDS, and what that operation buys
LEVELS = [
    ("Nominal",  "=  \u2260", "identity"),
    ("Ordinal",  "<  >",       "order"),
    ("Interval", "+  \u2212", "differences"),
    ("Ratio",    "\u00d7  \u00f7", "ratios"),
]

CHIP_W, CHIP_H, CHIP_GAP = 1.16, 0.52, 0.13
X0, ROW_H = 1.85, 0.86


def chip(ax, x, y, label, is_new):
    ax.add_patch(FancyBboxPatch(
        (x, y - CHIP_H / 2), CHIP_W, CHIP_H,
        boxstyle="round,pad=0,rounding_size=0.1",
        facecolor=NEW_FILL if is_new else OLD_FILL,
        edgecolor=NEW_EDGE if is_new else OLD_EDGE,
        linewidth=1.3 if is_new else 1.0, zorder=3))
    ax.text(x + CHIP_W / 2, y, label, ha="center", va="center",
            fontsize=13 if is_new else 12,
            color=INK if is_new else MUTED,
            fontweight="bold" if is_new else "normal", zorder=4)


fig, ax = plt.subplots(figsize=(8.4, 4.4))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

n = len(LEVELS)
Y0 = 0.55
X_LABEL = X0 + n * (CHIP_W + CHIP_GAP) + 0.18   # meaning labels share one column

for i, (name, _adds, meaning) in enumerate(LEVELS):
    y = Y0 + i * ROW_H

    ax.plot([0.32, X_LABEL + 1.45], [y - ROW_H / 2] * 2,
            color=HAIR, lw=0.9, zorder=1)

    ax.text(0.40, y, name, ha="left", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # inherited operations, then the one this rung adds
    for j in range(i + 1):
        chip(ax, X0 + j * (CHIP_W + CHIP_GAP), y, LEVELS[j][1], is_new=(j == i))

    ax.text(X_LABEL, y, meaning, ha="left", va="center",
            fontsize=11.5, style="italic", color=NEW_EDGE)

top = Y0 + (n - 1) * ROW_H
ax.annotate("", xy=(0.20, top + 0.30), xytext=(0.20, Y0 - 0.30),
            arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.3,
                            shrinkA=0, shrinkB=0))
ax.text(0.20, top + 0.42, "operations accumulate", ha="left", va="bottom",
        fontsize=10, color=MUTED)

# categorical: a closed, finite subset of nominal. Sits clear of the bottom rung.
cat_top, cat_h = Y0 - ROW_H / 2 - 0.20, 0.42
ax.add_patch(FancyBboxPatch(
    (0.32, cat_top - cat_h), 5.05, cat_h,
    boxstyle="round,pad=0,rounding_size=0.07",
    facecolor="none", edgecolor=CAT_EDGE, linewidth=1.2,
    linestyle=(0, (4, 2.5)), zorder=3))
ax.text(2.845, cat_top - cat_h / 2,
        "categorical  =  nominal  +  closed, finite value set",
        ha="center", va="center", fontsize=11, color=CAT_EDGE)
ax.plot([1.05, 1.05], [Y0 - ROW_H / 2, cat_top], color=CAT_EDGE, lw=1.0, zorder=2)

ax.set_xlim(0, X_LABEL + 1.55)
ax.set_ylim(cat_top - cat_h - 0.30, top + 0.80)
ax.axis("off")
fig.tight_layout(pad=0.3)

OUT.mkdir(parents=True, exist_ok=True)
for ext, kw in (("svg", {}), ("png", {"dpi": 200})):
    fig.savefig(OUT / f"noir-ladder.{ext}", facecolor="white",
                bbox_inches="tight", pad_inches=0.14, **kw)
print("wrote", OUT / "noir-ladder.svg", "and .png")
