"""
Script to generate a clean, professional research methodology flowchart (Tahapan Penelitian)
for the Bitcoin BI Thesis Proposal - Chapter 3
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# --- Color Palette ---
COLOR_PRIMARY    = '#961d5a'   # Deep maroon/magenta (thesis brand)
COLOR_BOX_BG     = '#fdf0f5'   # Very light pink background for box content
COLOR_ACCENT     = '#c94a85'   # Lighter pink for sub-details
COLOR_WHITE      = '#ffffff'
COLOR_DARK_TEXT  = '#2d1a25'
COLOR_GRAY_TEXT  = '#5c3d4e'
COLOR_ARROW      = '#961d5a'
COLOR_BORDER     = '#961d5a'
COLOR_BG         = '#ffffff'

# --- Stage Data ---
stages = [
    {
        "num": "TAHAP 1",
        "title": "PENGUMPULAN & PRA-PEMROSESAN DATA",
        "icon": "①",
        "details": [
            "Akuisisi 43.788 data historis BTC/USDT per jam (2021–2026) via Binance Spot API",
            "Penanganan missing values menggunakan Linear Polynomial Interpolation",
            "Normalisasi data mentah dengan metode Min-Max Scaler ke rentang [0, 1]",
        ]
    },
    {
        "num": "TAHAP 2",
        "title": "REKAYASA FITUR (FEATURE ENGINEERING)",
        "icon": "②",
        "details": [
            "Konstruksi 15 indikator teknikal: MA-7, MA-21, RSI-14, MACD, Bollinger Bands, dll.",
            "Seleksi fitur berbasis kontribusi prediktif menggunakan metode SHAP (Explainable AI)",
            "Pembagian dataset: 80% Training | 10% Validation | 10% Testing",
        ]
    },
    {
        "num": "TAHAP 3",
        "title": "PELATIHAN & OPTIMASI MODEL PREDIKTIF",
        "icon": "③",
        "details": [
            "Pelatihan tiga model: LSTM, GRU (Deep Learning), dan XGBoost (Baseline Ensemble)",
            "Optimasi hiperparameter menggunakan Grid Search Cross-Validation",
            "Implementasi Walk-Forward Validation (jendela 168 jam) untuk mencegah data leakage",
        ]
    },
    {
        "num": "TAHAP 4",
        "title": "EVALUASI & KOMPARASI PERFORMA MODEL",
        "icon": "④",
        "details": [
            "Pengukuran metrik teknis: RMSE, MAE, MAPE antar ketiga model",
            "Analisis trade-off: Presisi Numerik (RMSE) vs. Akurasi Arah Pasar (Win Rate %)",
            "Interpretasi kontribusi fitur menggunakan SHAP Value Visualization",
        ]
    },
    {
        "num": "TAHAP 5",
        "title": "INTEGRASI BI DASHBOARD & METRIK RISIKO",
        "icon": "⑤",
        "details": [
            "Transformasi output prediksi ke metrik risiko eksekutif: Sharpe Ratio & VaR (95%)",
            "Pembangunan prototipe BI Decision Support Dashboard yang fungsional dan interaktif",
            "Validasi kelayakan sistem oleh calon pengguna (manajer investasi & analis keuangan)",
        ]
    },
]

# --- Layout ---
fig_width  = 12
stage_h    = 1.55   # height of each stage block
gap        = 0.28   # gap between stages for arrow
total_h    = len(stages) * stage_h + len(stages) * gap + 1.4  # top/bottom margin

fig, ax = plt.subplots(figsize=(fig_width, total_h))
ax.set_xlim(0, 1)
ax.set_ylim(0, total_h)
ax.axis('off')
fig.patch.set_facecolor(COLOR_BG)

# --- Title ---
title_y = total_h - 0.42
ax.text(0.5, title_y, "ALUR TAHAPAN METODOLOGI PENELITIAN",
        ha='center', va='center', fontsize=15, fontweight='bold',
        color=COLOR_PRIMARY, fontfamily='DejaVu Serif',
        transform=ax.transData)
ax.text(0.5, title_y - 0.29,
        "Pemodelan Aset Digital Terintegrasi Business Intelligence Dashboard",
        ha='center', va='center', fontsize=9.5, fontstyle='italic',
        color=COLOR_GRAY_TEXT, fontfamily='DejaVu Serif')

# thin decorative line under title
ax.plot([0.05, 0.95], [title_y - 0.44, title_y - 0.44],
        color=COLOR_PRIMARY, linewidth=1.2, alpha=0.4)

# --- Draw stages ---
x_left  = 0.04
x_right = 0.96
box_w   = x_right - x_left

start_y = total_h - 1.1   # top edge of first stage

for i, stage in enumerate(stages):
    top_y    = start_y - i * (stage_h + gap)
    bottom_y = top_y - stage_h
    mid_y    = (top_y + bottom_y) / 2

    # --- Outer shadow effect ---
    shadow = FancyBboxPatch((x_left + 0.003, bottom_y - 0.012), box_w, stage_h,
                             boxstyle="round,pad=0.018", linewidth=0,
                             facecolor='#d0a0b8', alpha=0.25, zorder=1)
    ax.add_patch(shadow)

    # --- Header band ---
    header_h = 0.38
    header_patch = FancyBboxPatch((x_left, top_y - header_h), box_w, header_h,
                                   boxstyle="round,pad=0.012",
                                   linewidth=0, facecolor=COLOR_PRIMARY, zorder=2)
    ax.add_patch(header_patch)

    # --- Body background ---
    body_h = stage_h - header_h
    body_patch = FancyBboxPatch((x_left, bottom_y), box_w, body_h,
                                 boxstyle="round,pad=0.012",
                                 linewidth=1.5, edgecolor=COLOR_PRIMARY,
                                 facecolor=COLOR_BOX_BG, zorder=2)
    ax.add_patch(body_patch)

    # --- Stage number label (left of header) ---
    ax.text(x_left + 0.026, top_y - header_h / 2,
            stage["num"] + ":",
            ha='left', va='center', fontsize=8.2, fontweight='bold',
            color='#f9d0e3', fontfamily='DejaVu Serif', zorder=3)

    # --- Header Title ---
    ax.text(0.5, top_y - header_h / 2,
            stage["title"],
            ha='center', va='center', fontsize=9.8, fontweight='bold',
            color=COLOR_WHITE, fontfamily='DejaVu Serif', zorder=3)

    # --- Detail bullets ---
    n_items = len(stage["details"])
    item_spacing = body_h / (n_items + 0.8)
    for j, detail in enumerate(stage["details"]):
        item_y = bottom_y + body_h - (j + 0.75) * item_spacing
        # bullet dot
        ax.plot(x_left + 0.028, item_y, 'o',
                color=COLOR_PRIMARY, markersize=4.5, zorder=4)
        ax.text(x_left + 0.048, item_y, detail,
                ha='left', va='center', fontsize=7.6,
                color=COLOR_DARK_TEXT, fontfamily='DejaVu Serif',
                zorder=4, wrap=True)

    # --- Arrow between stages ---
    if i < len(stages) - 1:
        arrow_top    = bottom_y
        arrow_bottom = bottom_y - gap
        arrow_mid    = (arrow_top + arrow_bottom) / 2

        # Arrow shaft
        ax.annotate("",
            xy=(0.5, arrow_bottom + 0.02),
            xytext=(0.5, arrow_top - 0.005),
            arrowprops=dict(
                arrowstyle="-|>",
                color=COLOR_ARROW,
                lw=2.0,
                mutation_scale=16,
            ),
            zorder=5
        )

# --- Footer note ---
footer_y = stages[-1]["num"]  # dummy
last_top = start_y - (len(stages) - 1) * (stage_h + gap)
last_bottom = last_top - stage_h
ax.text(0.5, last_bottom - 0.18,
        "Sumber: Rancangan Metodologi Penelitian (2025) | Universitas Nusa Putra",
        ha='center', va='center', fontsize=7.2,
        color='#9b7a89', fontstyle='italic', fontfamily='DejaVu Serif')

plt.tight_layout(pad=0.3)
output_path = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\04_Visualizations\Tahapan_Penelitian_BI.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight',
            facecolor=COLOR_BG, edgecolor='none')
plt.close()
print(f"✅ Diagram saved to: {output_path}")
