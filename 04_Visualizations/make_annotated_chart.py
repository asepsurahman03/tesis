import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import datetime

# Historical monthly BTC price approximations (USD)
months = [
    '2021-03','2021-05','2021-07','2021-11',
    '2022-01','2022-02','2022-05','2022-07','2022-11',
    '2023-01','2023-06','2023-09','2023-10','2023-12',
    '2024-03','2024-04','2024-06','2024-10','2024-11',
    '2025-01','2025-04','2025-07','2025-10','2025-12',
    '2026-01'
]
prices = [
    55000, 57000, 32000, 67000,
    43000, 43000, 30000, 23000, 16500,
    22000, 30000, 27000, 27000, 43000,
    71000, 63000, 60000, 68000, 96000,
    99000, 83000, 102000, 92000, 107000,
    80000
]

dates = [datetime.datetime.strptime(m, '%Y-%m') for m in months]

fig, ax = plt.subplots(figsize=(15, 7.5))
ax.fill_between(dates, prices, alpha=0.12, color='#f7931a')
ax.plot(dates, prices, color='#f7931a', linewidth=2.5)

ax.set_facecolor('#f9f9f9')
fig.patch.set_facecolor('#ffffff')
ax.grid(True, linestyle='--', alpha=0.35, color='gray')
ax.set_xlabel('Tahun', fontsize=12, labelpad=8)
ax.set_ylabel('Harga Bitcoin (USD)', fontsize=12, labelpad=8)
ax.set_title(
    'Gambar 1. Dinamika Harga Bitcoin (BTC/USDT) Periode 2021-2026\n'
    'Bukti Volatilitas Ekstrem dan Sensitivitas terhadap Faktor Geopolitik & Makroekonomi',
    fontsize=12, fontweight='bold', pad=14
)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))

# --- Event annotations ---
# Format: (month_str, approx_price, label, direction, color, x_offset_months)
events = [
    ('2021-11', 67000,  'ATH $69K\n(Nov 2021)', 'up', '#27ae60', 0),
    ('2022-02', 43000,  'Invasi Rusia\nke Ukraina\n(Feb 2022)', 'down', '#c0392b', 1),
    ('2022-05', 30000,  'Collapse\nTerra/LUNA\n(Mei 2022)', 'down', '#c0392b', 0),
    ('2022-11', 16500,  'Kolaps\nFTX\n(Nov 2022)', 'down', '#c0392b', 0),
    ('2023-10', 27000,  'Perang\nHamas-Israel\n(Okt 2023)', 'down', '#c0392b', 0),
    ('2024-04', 63000,  'Halving BTC &\nSerangan Iran\nke Israel\n(Apr 2024)', 'up', '#e67e22', 0),
    ('2024-11', 96000,  'ATH Baru ~$100K\nTrump Terpilih\n(Nov 2024)', 'up', '#27ae60', 0),
    ('2025-04', 83000,  'Eskalasi\nAS-Iran\n(2025)', 'down', '#c0392b', 0),
]

for month_str, y_val, label, direction, color, offset in events:
    dt = datetime.datetime.strptime(month_str, '%Y-%m')
    if direction == 'up':
        yt = y_val + 18000
    else:
        yt = y_val - 18000

    ax.annotate(
        label,
        xy=(dt, y_val),
        xytext=(dt, yt),
        fontsize=7.8,
        color=color,
        fontweight='bold',
        ha='center',
        va='center',
        arrowprops=dict(arrowstyle='->', color=color, lw=1.4),
        bbox=dict(boxstyle='round,pad=0.35', facecolor='white', edgecolor=color, alpha=0.92, linewidth=1.2)
    )

# Legend
legend_elements = [
    Line2D([0], [0], color='#f7931a', linewidth=2.5, label='Harga BTC/USDT (bulanan)'),
    mpatches.Patch(color='#27ae60', label='Peristiwa Positif / Puncak Harga'),
    mpatches.Patch(color='#c0392b', label='Krisis / Tekanan Geopolitik'),
    mpatches.Patch(color='#e67e22', label='Peristiwa Campuran'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.95, edgecolor='#cccccc')

plt.tight_layout()
out_path = r'e:/Nusa Putra/S2/Semester 2/Business Intellegence/Penelitian/Analisis Bit Coin/04_Visualizations/btc_annotated_events.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight')
print('SUCCESS: Chart saved to', out_path)
