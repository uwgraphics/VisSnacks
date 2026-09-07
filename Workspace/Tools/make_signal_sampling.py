#!/usr/bin/env python3
"""
Generate a signal-sampling illustration (adequate sampling vs. aliasing
from undersampling) as vector SVG (and rasterized PNG).

Produces two style variants:
  - "modern": clean, minimal, muted single-accent-color redesign
  - "color":  textbook-style with distinct colors + legend + axes

Usage:
    python3 make_signal_sampling.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---------------------------------------------------------------------------
# Signal / sampling parameters
# ---------------------------------------------------------------------------
F_TRUE = 5.0        # Hz, frequency of the true continuous signal
DURATION = 1.0      # seconds shown
FS_GOOD = 40.0      # Hz, adequate sample rate (8 samples/cycle, >> Nyquist=10Hz)
FS_BAD = 6.0        # Hz, undersampling rate (Nyquist=3Hz < 5Hz -> aliasing)

# Analytically, sampling a 5 Hz sine at 6 Hz aliases to -1 Hz, i.e. the
# samples lie exactly on y = -sin(2*pi*1*t). (5 - 6 = -1, so
# sin(2*pi*5*t_n) == sin(2*pi*(-1)*t_n) at t_n = n/6 exactly.)
F_ALIAS = F_TRUE - FS_BAD  # = -1.0 Hz

t_dense = np.linspace(0, DURATION, 2000)
true_signal = np.sin(2 * np.pi * F_TRUE * t_dense)
alias_curve = np.sin(2 * np.pi * F_ALIAS * t_dense)

t_good = np.arange(0, DURATION, 1.0 / FS_GOOD)
y_good = np.sin(2 * np.pi * F_TRUE * t_good)

t_bad = np.arange(0, DURATION, 1.0 / FS_BAD)
y_bad = np.sin(2 * np.pi * F_TRUE * t_bad)

# sanity check: samples should sit on both curves
assert np.allclose(y_bad, np.sin(2 * np.pi * F_ALIAS * t_bad), atol=1e-9)


def render(style: str, out_base: str):
    if style == "modern":
        FIG_BG = "#ffffff"
        TRUE_COLOR = "#1f2933"      # near-black slate
        SAMPLE_COLOR = "#e8590c"    # single warm accent for samples
        ALIAS_COLOR = "#e8590c"
        ALIAS_ALPHA = 0.55
        LINEWIDTH = 2.0
        SAMPLE_SIZE = 46
        TITLE_COLOR = "#1f2933"
        SUBTITLE_COLOR = "#5c6773"
        SHOW_AXES = False
        SHOW_LEGEND = False
        FONT = "DejaVu Sans"
    elif style == "color":
        FIG_BG = "#ffffff"
        TRUE_COLOR = "#333333"
        SAMPLE_COLOR = "#d62728"     # red
        ALIAS_COLOR = "#1f77b4"      # blue
        ALIAS_ALPHA = 1.0
        LINEWIDTH = 1.8
        SAMPLE_SIZE = 42
        TITLE_COLOR = "#111111"
        SUBTITLE_COLOR = "#333333"
        SHOW_AXES = True
        SHOW_LEGEND = True
        FONT = "DejaVu Sans"
    else:
        raise ValueError(style)

    plt.rcParams["font.family"] = FONT

    fig, axes = plt.subplots(2, 1, figsize=(8, 7), facecolor=FIG_BG)

    # --- Top panel: adequately sampled ------------------------------------
    ax = axes[0]
    ax.set_facecolor(FIG_BG)
    ax.plot(t_dense, true_signal, color=TRUE_COLOR, linewidth=LINEWIDTH,
             label="True signal", solid_capstyle="round", zorder=2)
    ax.scatter(t_good, y_good, s=SAMPLE_SIZE, color=SAMPLE_COLOR,
               edgecolor=FIG_BG if style == "modern" else "none",
               linewidth=0.8, zorder=3, label="Samples")

    ax.set_title("Adequately Sampled Signal", color=TITLE_COLOR,
                 fontsize=15, fontweight="bold", pad=14)
    ax.text(0.5, -0.32,
            f"$f$ = {F_TRUE:.0f} Hz,  $f_s$ = {FS_GOOD:.0f} Hz  "
            f"($f_s$ > 2$f$ — Nyquist satisfied)",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=10, color=SUBTITLE_COLOR)

    # --- Bottom panel: undersampled / aliased ------------------------------
    ax2 = axes[1]
    ax2.set_facecolor(FIG_BG)
    ax2.plot(t_dense, true_signal, color=TRUE_COLOR, linewidth=LINEWIDTH,
              label="True signal", solid_capstyle="round", zorder=2)
    ax2.plot(t_dense, alias_curve, color=ALIAS_COLOR, linewidth=LINEWIDTH,
              linestyle=(0, (6, 3)), alpha=ALIAS_ALPHA, zorder=2,
              label="Aliased reconstruction")
    ax2.scatter(t_bad, y_bad, s=SAMPLE_SIZE, color=SAMPLE_COLOR,
                edgecolor=FIG_BG if style == "modern" else "none",
                linewidth=0.8, zorder=3, label="Samples")

    ax2.set_title("Aliased Signal Due to Undersampling", color=TITLE_COLOR,
                  fontsize=15, fontweight="bold", pad=14)
    ax2.text(0.5, -0.32,
             f"$f$ = {F_TRUE:.0f} Hz,  $f_s$ = {FS_BAD:.0f} Hz  "
             f"($f_s$ < 2$f$ — appears as {abs(F_ALIAS):.0f} Hz)",
             transform=ax2.transAxes, ha="center", va="top",
             fontsize=10, color=SUBTITLE_COLOR)

    for a in (ax, ax2):
        a.set_ylim(-1.35, 1.35)
        a.set_xlim(t_dense[0], t_dense[-1])
        if SHOW_AXES:
            a.set_xlabel("Time (s)", fontsize=9, color=SUBTITLE_COLOR)
            a.set_ylabel("Amplitude", fontsize=9, color=SUBTITLE_COLOR)
            a.spines["top"].set_visible(False)
            a.spines["right"].set_visible(False)
            a.spines["left"].set_color("#888888")
            a.spines["bottom"].set_color("#888888")
            a.tick_params(colors="#555555", labelsize=8)
            a.grid(True, linewidth=0.4, alpha=0.35)
        else:
            for spine in a.spines.values():
                spine.set_visible(False)
            a.set_xticks([])
            a.set_yticks([])
            a.axhline(0, color="#c9ccd1", linewidth=0.8, zorder=1)

    if SHOW_LEGEND:
        for a in (ax, ax2):
            a.legend(loc="upper right", fontsize=8, framealpha=0.9,
                      borderpad=0.6, handlelength=2.2)

    fig.tight_layout(h_pad=4.0, rect=[0, 0, 1, 1])

    fig.savefig(f"{out_base}.svg", format="svg", facecolor=FIG_BG)
    fig.savefig(f"{out_base}.png", format="png", dpi=200, facecolor=FIG_BG)
    plt.close(fig)
    print(f"wrote {out_base}.svg and {out_base}.png")


if __name__ == "__main__":
    render("modern", "signal-sampling-modern")
    render("color", "signal-sampling-color")
