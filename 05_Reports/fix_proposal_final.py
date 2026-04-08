"""
fix_proposal_final.py  –  Hapus semua angka hasil eksperimen dari proposal
Menggunakan regex yang lebih fleksibel, bukan exact string matching.
"""
import re

filepath = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original = content  # backup
changes = 0

# ============================================================
# 1. ABSTRAK — buang semua angka hasil, ganti ke bahasa rencana
# ============================================================
# Ganti seluruh blok abstrak dengan versi prospektif
abstrak_pattern = re.compile(
    r'(<div class="abstract-section">)(.*?)(</div>)',
    re.DOTALL
)

new_abstrak_body = """
        <strong>Abstrak</strong>— Volatilitas yang tinggi pada pasar cryptocurrency menuntut adanya model prediksi yang
        mampu mengintegrasikan data berskala besar (Big Data) secara real-time ke dalam sistem pendukung keputusan
        (Decision Support System/DSS). Penelitian ini mengusulkan kerangka kerja <em>Business Intelligence</em> (BI)
        empat lapis yang berencana mengintegrasikan analitika Big Data dengan pemodelan prediksi deep learning.
        Penelitian akan memanfaatkan dataset berfrekuensi tinggi selama lima tahun yang terdiri dari 43.786 data
        harga historis Bitcoin (BTC/USDT) per jam dari API Binance, memenuhi karakteristik kerangka Big Data.
        Sebanyak 15 indikator teknikal akan diekstraksi sebagai fitur input dan dievaluasi menggunakan SHapley
        Additive exPlanations (SHAP). Algoritma deep learning berbasis sekuensial—yakni Long Short-Term Memory
        (LSTM) dan Gated Recurrent Units (GRU)—akan dibandingkan dengan XGBoost sebagai model baseline (acuan).
        Arsitektur model akan dioptimasi menggunakan metode Grid Search. Pengujian Walk-Forward Validation
        direncanakan untuk mengukur performa komparatif antar model. Luaran prediksi akan diterjemahkan ke
        dalam metrik risiko finansial seperti Sharpe Ratio, Win Rate, dan Value at Risk (VaR) pada antarmuka
        BI Dashboard. Proposal ini diharapkan menghasilkan sistem pendukung keputusan yang reliabel bagi para
        manajer investasi untuk memitigasi risiko pasar cryptocurrency menggunakan kecerdasan buatan.
        <br><br>
        <strong>Kata Kunci</strong>— Business Intelligence, Prediksi Cryptocurrency, Big Data Analytics,
        Deep Learning, XGBoost, LSTM, GRU, Informatika Finansial, Bitcoin.
    """

def replace_abstrak(m):
    return m.group(1) + new_abstrak_body + m.group(3)

new_content, n = abstrak_pattern.subn(replace_abstrak, content, count=1)
if n:
    content = new_content
    changes += 1
    print(f"[OK] Abstrak diperbaiki")
else:
    print(f"[SKIP] Abstrak: pola tidak cocok")

# ============================================================
# 2. Semua angka RMSE spesifik yang masih tersisa
# ============================================================
# RMSE 0.1058 / 0.1145 / 0.1524 dan variannya
rmse_specific = [
    (r'RMSE[:\s]*0[.,]1058', 'RMSE terkecil yang diharapkan dari model GRU'),
    (r'RMSE[:\s]*0[.,]1145', 'RMSE yang diharapkan dari model LSTM'),
    (r'RMSE[:\s]*0[.,]1524', 'RMSE model baseline XGBoost'),
    (r'0[.,]1058', 'nilai RMSE terbaik yang diharapkan'),
    (r'0[.,]1145', 'nilai RMSE LSTM yang diharapkan'),
    (r'0[.,]1524', 'nilai RMSE baseline yang diharapkan'),
]
for pattern, replacement in rmse_specific:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x: {pattern} -> {replacement[:40]}")

# ============================================================
# 3. Win Rate angka spesifik
# ============================================================
winrate_specific = [
    (r'72[.,]3\s*%', 'Win Rate tertinggi yang diharapkan dari LSTM'),
    (r'69[.,]8\s*%', 'Win Rate GRU yang diharapkan'),
    (r'58[.,]4\s*%', 'Win Rate XGBoost yang diharapkan'),
]
for pattern, replacement in winrate_specific:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x: {pattern} -> {replacement[:40]}")

# ============================================================
# 4. Sharpe Ratio angka spesifik
# ============================================================
sharpe_specific = [
    (r'Sharpe\s+Ratio\s*[\(（][^)]*1[.,]45[^)]*[\)）]', 'Sharpe Ratio yang akan dievaluasi'),
    (r'Sharpe\s+Ratio\s*[\(（][^)]*0[.,]95[^)]*[\)）]', 'Sharpe Ratio baseline yang akan diukur'),
    (r'Sharpe\s+Ratio\s*[\(（][^)]*1[.,]32[^)]*[\)）]', 'Sharpe Ratio GRU yang akan diukur'),
    (r'LSTM[:\s]*1[.,]45', 'LSTM: nilai akan dievaluasi'),
    (r'1[.,]45\b', 'nilai yang akan dievaluasi'),
]
for pattern, replacement in sharpe_specific:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x Sharpe: {pattern} -> {replacement[:40]}")

# ============================================================
# 5. VaR angka spesifik
# ============================================================
var_specific = [
    (r'-2[.,]34\s*%', 'nilai VaR yang akan diestimasi'),
    (r'-4[.,]10?\s*%', 'nilai VaR baseline yang akan diestimasi'),
    (r'-2[.,]67\s*%', 'nilai VaR GRU yang akan diestimasi'),
    (r'VaR\s+95[%﹪]\s*[:\-]\s*-?[\d.,]+%?', 'VaR (95%) yang akan dihitung'),
    (r'VaR.*?-[\d.,]+%', 'VaR yang akan diestimasikan'),
]
for pattern, replacement in var_specific:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x VaR: {pattern} -> {replacement[:40]}")

# ============================================================
# 6. MAE / MAPE angka spesifik
# ============================================================
mae_specific = [
    (r'MAE[:\s]*0[.,]094\d*', 'MAE GRU yang diharapkan'),
    (r'MAE[:\s]*0[.,]100\d*', 'MAE LSTM yang diharapkan'),
    (r'MAE[:\s]*0[.,]126\d*', 'MAE baseline yang diharapkan'),
    (r'MAPE[:\s]*13[.,]13\s*%', 'MAPE GRU yang diharapkan'),
    (r'MAPE[:\s]*13[.,]96\s*%', 'MAPE LSTM yang diharapkan'),
    (r'MAPE[:\s]*16[.,]5\d*\s*%', 'MAPE baseline yang diharapkan'),
    (r'0[.,]0948\b', 'nilai MAE terbaik yang diharapkan'),
    (r'0[.,]1008\b', 'nilai MAE LSTM yang diharapkan'),
    (r'0[.,]1260\b', 'nilai MAE baseline yang diharapkan'),
]
for pattern, replacement in mae_specific:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x MAE/MAPE: {pattern}")

# ============================================================
# 7. Ubah kalimat "terbukti" / "berhasil" / "mengungkap" -> prospektif
# ============================================================
kalimat_fixes = [
    (r'Model GRU terbukti menjadi arsitektur yang paling presisi',
     'Model GRU diharapkan menjadi arsitektur yang paling presisi'),
    (r'terbukti sangat dominan',
     'diharapkan memberikan dominasi performa'),
    (r'penelitian ini memenuhi karakteristik',
     'penelitian ini diharapkan memenuhi karakteristik'),
    (r'model ini berhasil\s+mengkalkulasikan',
     'model ini diharapkan mampu mengkalkulasikan'),
    (r'Pengujian Walk-Forward Validation menunjukkan temuan komparatif yang\s+kritis:',
     'Pengujian Walk-Forward Validation direncanakan untuk mengungkap temuan komparatif kritis'),
    (r'terbukti menjadi',
     'diharapkan menjadi'),
    (r'telah terbukti',
     'diharapkan terbukti'),
    (r'berhasil mengkalkulasikan',
     'diharapkan dapat mengkalkulasikan'),
]
for pattern, replacement in kalimat_fixes:
    new_c, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Ganti {n}x kalimat: {pattern[:50]}")

# ============================================================
# 8. Ganti tabel hasil dengan tabel rencana evaluasi
# ============================================================
# Cari tabel yang masih punya angka hasil
tabel_fixes = [
    # Baris RMSE dengan angka
    (r'<td>0[.,]1524</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>0[.,]1145</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td><b>0[.,]1058</b></td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>0[.,]1058</td>', '<td><em>Akan diukur</em></td>'),
    # Baris MAE
    (r'<td>0[.,]1260</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>0[.,]1008</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td><b>0[.,]0948</b></td>', '<td><em>Akan diukur</em></td>'),
    # Baris MAPE
    (r'<td>16[.,]50%</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>13[.,]96%</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td><b>13[.,]13%</b></td>', '<td><em>Akan diukur</em></td>'),
    # Baris waktu komputasi
    (r'<td><b>12[.,]4s</b></td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>106[.,]6s</td>', '<td><em>Akan diukur</em></td>'),
    (r'<td>192[.,]2s</td>', '<td><em>Akan diukur</em></td>'),
    # Baris Win Rate
    (r'<td>58[.,]4%</td>', '<td><em>Akan dievaluasi</em></td>'),
    (r'<td><b>72[.,]3%</b></td>', '<td><em>Akan dievaluasi</em></td>'),
    (r'<td>69[.,]8%</td>', '<td><em>Akan dievaluasi</em></td>'),
    # Baris Sharpe
    (r'<td>0[.,]95</td>', '<td><em>Akan dihitung</em></td>'),
    (r'<td><b>1[.,]45</b></td>', '<td><em>Akan dihitung</em></td>'),
    (r'<td>1[.,]32</td>', '<td><em>Akan dihitung</em></td>'),
    # Baris VaR
    (r'<td>-4[.,]10%</td>', '<td><em>Akan diestimasi</em></td>'),
    (r'<td><b>-2[.,]34%</b></td>', '<td><em>Akan diestimasi</em></td>'),
    (r'<td>-2[.,]67%</td>', '<td><em>Akan diestimasi</em></td>'),
]
for pattern, replacement in tabel_fixes:
    new_c, n = re.subn(pattern, replacement, content)
    if n:
        content = new_c
        changes += n
        print(f"[OK] Tabel: Ganti {n}x {pattern} -> {replacement[:30]}")

# ============================================================
# 9. Ubah judul tabel
# ============================================================
judul_tabel_fixes = [
    ('Table I. Quantitative Deep Learning Loss Diagnostics',
     'Table I. Rencana Evaluasi Metrik Performa Model (Akan Diisi Setelah Eksperimen)'),
    ('Tabel I. Diagnostik Kesalahan',
     'Tabel I. Rencana Evaluasi Metrik Performa Model'),
    ('Table II. Dynamic Information and Risk Constraints',
     'Table II. Rencana Evaluasi Metrik Risiko Bisnis (Akan Diisi Setelah Eksperimen)'),
    ('Tabel II. Informasi Dinamis',
     'Tabel II. Rencana Evaluasi Metrik Risiko Bisnis'),
]
for old, new in judul_tabel_fixes:
    if old in content:
        content = content.replace(old, new)
        changes += 1
        print(f"[OK] Judul tabel diperbarui: {old[:50]}")

# ============================================================
# VERIFIKASI AKHIR
# ============================================================
print("\n" + "="*60)
print("VERIFIKASI SISA ANGKA HASIL")
print("="*60)
sisa = []
cek_pola = [
    r'\b0\.1058\b', r'\b0\.1145\b', r'\b0\.1524\b',
    r'\b72\.3\b', r'\b69\.8\b', r'\b58\.4\b',
    r'\b1\.45\b', r'\b0\.95\b', r'\b1\.32\b',
    r'-2\.34', r'-4\.10', r'-2\.67',
    r'\b13\.13\b', r'\b13\.96\b', r'\b16\.50\b',
    r'\b0\.0948\b', r'\b0\.1008\b', r'\b0\.1260\b',
]
for p in cek_pola:
    m = re.search(p, content)
    if m:
        ctx = content[max(0, m.start()-50):m.end()+50].replace('\n', ' ')
        sisa.append(f"  MASIH ADA [{p}] -> ...{ctx}...")

if sisa:
    print(f"PERINGATAN: {len(sisa)} angka hasil masih ditemukan:")
    for s in sisa:
        print(s[:120])
else:
    print("BERSIH: Tidak ada angka hasil eksperimen yang tersisa!")

# ============================================================
# SIMPAN
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal perubahan: {changes}")
print(f"Ukuran asli   : {len(original):,} chars")
print(f"Ukuran baru   : {len(content):,} chars")
print("File BERHASIL disimpan!")
