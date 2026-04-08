"""
Script to generate Kerangka Pemikiran Penelitian (Conceptual Framework)
for the Bitcoin BI Thesis Proposal
Style: matching Tahapan_Penelitian_BI.png (maroon/magenta brand)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# --- Color Palette (matching Tahapan_Penelitian style) ---
COLOR_PRIMARY   = '#961d5a'   # Deep maroon/magenta (thesis brand)
COLOR_BOX_BG    = '#fdf0f5'   # Very light pink background
COLOR_ACCENT    = '#c94a85'   # Lighter pink
COLOR_WHITE     = '#ffffff'
COLOR_DARK_TEXT = '#2d1a25'
COLOR_GRAY_TEXT = '#5c3d4e'
COLOR_ARROW     = '#961d5a'
COLOR_BG        = '#ffffff'

# Layer colors (distinct per column)
COL1_HEADER  = '#1e3a5f'   # Dark navy  - Lapisan Data
COL1_BODY    = '#eef4fb'   # Light blue tint
COL1_BORDER  = '#3b82c4'

COL2_HEADER  = '#5b21b6'   # Purple - Lapisan Pemodelan
COL2_BODY    = '#f3f0ff'
COL2_BORDER  = '#7c3aed'

COL3_HEADER  = '#065f46'   # Dark green - Evaluasi
COL3_BODY    = '#ecfdf5'
COL3_BORDER  = '#059669'

COL4_HEADER  = '#961d5a'   # Maroon - BI Dashboard (brand color)
COL4_BODY    = '#fff0f6'
COL4_BORDER  = '#c94a85'

fig_w = 16
fig_h = 10.5
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')
fig.patch.set_facecolor(COLOR_BG)

# =====================================================================
# TITLE
# =====================================================================
ax.text(fig_w/2, fig_h - 0.38, "KERANGKA PEMIKIRAN PENELITIAN",
        ha='center', va='center', fontsize=22, fontweight='bold',
        color=COLOR_PRIMARY, fontfamily='DejaVu Serif')
ax.text(fig_w/2, fig_h - 0.82,
        "Sistem Business Intelligence Prediksi Harga Bitcoin Berbasis Deep Learning (2021–2026)",
        ha='center', va='center', fontsize=11, fontstyle='italic',
        color=COLOR_GRAY_TEXT, fontfamily='DejaVu Serif')
ax.plot([0.5, fig_w-0.5], [fig_h - 1.05, fig_h - 1.05],
        color=COLOR_PRIMARY, linewidth=1.2, alpha=0.4)

# =====================================================================
# LAYOUT: 4 columns
# =====================================================================
TOP_Y  = fig_h - 1.3
BOT_Y  = 1.0
COL_H  = TOP_Y - BOT_Y   # total height of columns

# Column x-centers and widths
c_margin = 0.35
total_w  = fig_w - 2 * c_margin
arrow_w  = 0.55
col_w    = (total_w - 3 * arrow_w) / 4
x_starts = []
cx = c_margin
for i in range(4):
    x_starts.append(cx)
    cx += col_w
    if i < 3:
        cx += arrow_w

# helper: draw a column box with header
def draw_column(ax, x, y_top, y_bot, w,
                header_txt, header_color, body_color, border_color,
                items, item_sub=None):
    h = y_top - y_bot
    header_h = 0.55

    # shadow
    shadow = FancyBboxPatch((x + 0.04, y_bot - 0.06), w, h,
                             boxstyle="round,pad=0.05", linewidth=0,
                             facecolor='#b0b0b0', alpha=0.18, zorder=1)
    ax.add_patch(shadow)

    # header
    hdr = FancyBboxPatch((x, y_top - header_h), w, header_h,
                          boxstyle="round,pad=0.05",
                          linewidth=0, facecolor=header_color, zorder=2)
    ax.add_patch(hdr)

    # header text
    ax.text(x + w/2, y_top - header_h/2, header_txt,
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color='white', fontfamily='DejaVu Serif', zorder=3)

    # body
    body_h = h - header_h
    body = FancyBboxPatch((x, y_bot), w, body_h,
                           boxstyle="round,pad=0.05",
                           linewidth=2, edgecolor=border_color,
                           facecolor=body_color, zorder=2)
    ax.add_patch(body)

    # items
    n = len(items)
    spacing = body_h / (n + 0.5)
    for j, itm in enumerate(items):
        iy = y_bot + body_h - (j + 0.7) * spacing
        # sub-card background
        card = FancyBboxPatch((x + 0.10, iy - 0.30), w - 0.20, 0.56,
                               boxstyle="round,pad=0.04",
                               linewidth=1, edgecolor=border_color,
                               facecolor='white', alpha=0.9, zorder=3)
        ax.add_patch(card)

        main_lbl = itm[0]
        sub_lbl  = itm[1] if len(itm) > 1 else ""
        ax.text(x + w/2, iy + 0.06, main_lbl,
                ha='center', va='center', fontsize=8.8, fontweight='bold',
                color=header_color, fontfamily='DejaVu Serif', zorder=4)
        if sub_lbl:
            ax.text(x + w/2, iy - 0.13, sub_lbl,
                    ha='center', va='center', fontsize=7.6,
                    color=COLOR_DARK_TEXT, fontfamily='DejaVu Serif', zorder=4,
                    style='italic')

# helper: draw horizontal arrow
def draw_arrow(ax, x_from, x_to, y):
    ax.annotate("",
        xy=(x_to, y), xytext=(x_from, y),
        arrowprops=dict(
            arrowstyle="-|>",
            color=COLOR_PRIMARY,
            lw=2.2,
            mutation_scale=20,
        ), zorder=6)

# =====================================================================
# COLUMN 1 – LAPISAN DATA (Deep Navy)
# =====================================================================
c1x = x_starts[0]
draw_column(ax, c1x, TOP_Y, BOT_Y + 1.25, col_w,
            "1. LAPISAN DATA\n(Sumber & Ingesti)",
            COL1_HEADER, COL1_BODY, COL1_BORDER,
            [
                ("43.788 Rekaman BTC/USDT",   "Interval Per Jam · Maret 2021 – 2026"),
                ("Sumber: Binance Spot API",   "OHLCV · REST Endpoint Resmi"),
                ("Pra-Pemrosesan ETL",         "Interpolasi · Normalisasi Min-Max [0,1]"),
            ])

# =====================================================================
# COLUMN 2 – LAPISAN REKAYASA FITUR + PEMODELAN (Purple)
# =====================================================================
c2x = x_starts[1]
draw_column(ax, c2x, TOP_Y, BOT_Y + 1.25, col_w,
            "2. LAPISAN REKAYASA\n& PEMODELAN",
            COL2_HEADER, COL2_BODY, COL2_BORDER,
            [
                ("15 Indikator Teknikal",      "MA-7/21 · RSI · MACD · BB · Volatilitas"),
                ("LSTM  vs  GRU  vs  XGBoost", "Walk-Forward Validation · 168 Jam"),
                ("Optimasi: Grid Search",       "Dropout · Early Stopping · Adam Optim."),
            ])

# =====================================================================
# COLUMN 3 – EVALUASI & XAI (Dark Green)
# =====================================================================
c3x = x_starts[2]
draw_column(ax, c3x, TOP_Y, BOT_Y + 1.25, col_w,
            "3. LAPISAN EVALUASI\n& EXPLAINABLE AI",
            COL3_HEADER, COL3_BODY, COL3_BORDER,
            [
                ("Metrik Teknis",              "RMSE · MAE · MAPE Antar Model"),
                ("Trade-off Analisis",          "Presisi Numerik vs. Win Rate Arah"),
                ("SHAP Value (XAI)",            "Kontribusi Fitur secara Transparan"),
            ])

# =====================================================================
# COLUMN 4 – BI DASHBOARD (Maroon brand)
# =====================================================================
c4x = x_starts[3]
draw_column(ax, c4x, TOP_Y, BOT_Y + 1.25, col_w,
            "4. LAPISAN BI\nDASHBOARD",
            COL4_HEADER, COL4_BODY, COL4_BORDER,
            [
                ("Metrik Risiko Eksekutif",    "Sharpe Ratio · VaR 95% · Win Rate"),
                ("Decision Support Dashboard", "Prototipe Interaktif & Fungsional"),
                ("Target Pengguna",             "Manajer Investasi · Analis Keuangan"),
            ])

# =====================================================================
# ARROWS between columns (at mid-height of columns)
# =====================================================================
mid_y = (TOP_Y + BOT_Y + 1.25) / 2
for i in range(3):
    x_from = x_starts[i] + col_w + 0.04
    x_to   = x_starts[i+1] - 0.04
    draw_arrow(ax, x_from, x_to, mid_y)

# =====================================================================
# BOTTOM BANNER – Research Hypothesis
# =====================================================================
ban_y    = BOT_Y + 0.18
ban_h    = 0.88
ban_x    = c_margin
ban_w    = fig_w - 2*c_margin

shadow_ban = FancyBboxPatch((ban_x + 0.05, ban_y - 0.06), ban_w, ban_h,
                             boxstyle="round,pad=0.05", linewidth=0,
                             facecolor='#b0b0b0', alpha=0.18, zorder=1)
ax.add_patch(shadow_ban)

banner = FancyBboxPatch((ban_x, ban_y), ban_w, ban_h,
                         boxstyle="round,pad=0.05",
                         linewidth=2, edgecolor='#fbbf24',
                         facecolor='#1e293b', zorder=2)
ax.add_patch(banner)

# dashed connecting line from each column bottom to banner
for i in range(4):
    xc = x_starts[i] + col_w/2
    ax.plot([xc, xc], [BOT_Y + 1.25, ban_y + ban_h],
            color='#94a3b8', linewidth=1.8, linestyle='--', zorder=1, alpha=0.6)
    ax.annotate("", xy=(xc, ban_y + ban_h - 0.02), xytext=(xc, BOT_Y + 1.27),
                arrowprops=dict(arrowstyle="-|>", color='#94a3b8', lw=1.5, mutation_scale=12), zorder=5)

ax.text(ban_x + ban_w/2, ban_y + ban_h/2 + 0.16,
        "HIPOTESIS UTAMA PENELITIAN",
        ha='center', va='center', fontsize=12.5, fontweight='bold',
        color='white', fontfamily='DejaVu Serif', zorder=4)
ax.text(ban_x + ban_w/2, ban_y + ban_h/2 - 0.08,
        "H₁: Deep Learning (LSTM/GRU) melebihi XGBoost dalam presisi RMSE  "
        "|  H₂: LSTM unggul Win Rate  |  H₃: SHAP valid mengungkap fitur kritis  "
        "|  H₄: VaR & Sharpe Ratio mendukung keputusan investasi",
        ha='center', va='center', fontsize=8.2,
        color='#fef3c7', fontfamily='DejaVu Serif', zorder=4)

# =====================================================================
# FOOTER
# =====================================================================
ax.text(fig_w/2, 0.14,
        "Sumber: Rancangan Konseptual Penelitian (2025) | Universitas Nusa Putra, Sukabumi",
        ha='center', va='center', fontsize=7.5,
        color='#9b7a89', fontstyle='italic', fontfamily='DejaVu Serif')

plt.tight_layout(pad=0.3)
output_path = (r'e:\Nusa Putra\S2\Semester 2\Business Intellegence'
               r'\Penelitian\Analisis Bit Coin\04_Visualizations\Kerangka_Pemikiran_BI.png')
plt.savefig(output_path, dpi=200, bbox_inches='tight',
            facecolor=COLOR_BG, edgecolor='none')
plt.close()
print(f"✅ Kerangka Pemikiran saved to: {output_path}")
