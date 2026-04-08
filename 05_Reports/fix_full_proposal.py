"""
fix_full_proposal.py
Menyesuaikan SELURUH dokumen Proposal_Tesis_Bitcoin_BI_Indo.html agar:
1. Abstrak      -> deskripsi penelitian yang DIRENCANAKAN (bukan hasil)
2. BAB I        -> bahasan rencana penelitian (sudah dibersihkan sebagian)
3. BAB III      -> tabel hasil diganti tabel TARGET/RENCANA EVALUASI
4. Semua bagian -> bahasa prospektif ("akan", "diharapkan", "direncanakan")
"""

import re

filepath = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)
changes = []

# ============================================================
# FIX A: ABSTRAK — Ganti ke versi prospektif
# ============================================================
old_abstrak = content[content.find('<div class="abstract-section">'):content.find('</div>', content.find('<div class="abstract-section">'))+6]

new_abstrak = '''<div class="abstract-section">
        <strong>Abstrak</strong>— Volatilitas yang tinggi pada pasar cryptocurrency menuntut adanya model prediksi yang
        mampu mengintegrasikan data berskala besar (Big Data) secara real-time ke dalam sistem pendukung keputusan
        (Decision Support System). Penelitian ini mengusulkan kerangka kerja Business Intelligence (BI) empat lapis yang
        mengintegrasikan analitika Big Data dengan pemodelan prediksi menggunakan deep learning. Penelitian akan
        memanfaatkan dataset berfrekuensi tinggi selama lima tahun yang terdiri dari 43.786 data harga historis Bitcoin
        (BTC/USDT) per jam dari API Binance, sehingga memenuhi karakteristik kerangka Big Data. Sebanyak 15 indikator
        teknikal akan diekstraksi sebagai fitur input dan dievaluasi tingkat kepentingannya menggunakan SHapley Additive
        exPlanations (SHAP). Algoritma deep learning berbasis sekuensial, yakni Long Short-Term Memory (LSTM) dan Gated
        Recurrent Units (GRU), akan dibandingkan dengan algoritma XGBoost sebagai model baseline (acuan). Arsitektur
        model akan dioptimasi menggunakan metode Grid Search untuk menemukan kombinasi parameter terbaik. Pengujian
        Walk-Forward Validation akan dilakukan untuk mengukur performa komparatif antar model berdasarkan metrik RMSE,
        MAE, dan MAPE. Luaran prediksi selanjutnya akan diterjemahkan ke dalam indikator risiko finansial korporasi
        seperti Sharpe Ratio, Win Rate, dan Value at Risk (VaR) yang disajikan dalam antarmuka BI Dashboard. Proposal
        penelitian ini diharapkan menghasilkan suatu sistem operasional yang reliabel bagi para manajer investasi untuk
        memitigasi risiko pasar cryptocurrency menggunakan kecerdasan buatan.
        <br><br>
        <strong>Kata Kunci</strong>— Business Intelligence, Prediksi Cryptocurrency, Big Data Analytics, Deep Learning,
        XGBoost, LSTM, GRU, Informatika Finansial, Bitcoin.
    </div>'''

if old_abstrak in content:
    content = content.replace(old_abstrak, new_abstrak)
    changes.append("ABSTRAK: Diubah ke bahasa prospektif")
else:
    changes.append("ABSTRAK: Tidak ditemukan pola persis, dilewati")

# ============================================================
# FIX B: Tabel hasil kuantitatif (Tabel perbandingan RMSE)
# Ganti ke tabel rencana evaluasi / target metrik
# ============================================================

# Cari dan ganti tabel komparasi RMSE (Table I / Tabel I)
old_table_rmse_title = 'Tabel I. Diagnostik Kesalahan'
old_table_perf = ''

# Temukan blok table-container yang memuat RMSE 0.1524
rmse_pattern = re.compile(
    r'(<div class="table-container">.*?0\.1524.*?</div>\s*</div>)',
    re.DOTALL
)
match = rmse_pattern.search(content)
if match:
    old_table_perf = match.group(1)
    new_table_perf = '''<div class="table-container">
        <div class="table-title">Tabel I. Rencana Evaluasi Metrik Performa Model (Target Pengujian Walk-Forward Validation)
        </div>
        <table>
            <tr>
                <th>Metrik Evaluasi</th>
                <th>XGBoost (Baseline)</th>
                <th>LSTM</th>
                <th>GRU</th>
            </tr>
            <tr>
                <td>RMSE (Root Mean Square Error)</td>
                <td colspan="3" style="font-style:italic;">Akan dihitung dari hasil Walk-Forward Validation</td>
            </tr>
            <tr>
                <td>MAE (Mean Absolute Error)</td>
                <td colspan="3" style="font-style:italic;">Akan dihitung dari hasil Walk-Forward Validation</td>
            </tr>
            <tr>
                <td>MAPE (Mean Absolute Percentage Error)</td>
                <td colspan="3" style="font-style:italic;">Akan dihitung dari hasil Walk-Forward Validation</td>
            </tr>
            <tr>
                <td>Waktu Komputasi (detik)</td>
                <td colspan="3" style="font-style:italic;">Akan diukur saat eksekusi pelatihan model</td>
            </tr>
        </table>
        <p style="font-size:9.5pt; font-style:italic; text-indent:0; margin-top:4px;">
            * Tabel di atas merupakan rancangan skema evaluasi. Nilai aktual akan diisi setelah eksperimen dilaksanakan.
        </p>
    </div>'''
    content = content.replace(old_table_perf, new_table_perf)
    changes.append("TABEL RMSE: Diganti ke rancangan evaluasi (tanpa angka hasil)")
else:
    changes.append("TABEL RMSE: Pola tidak ditemukan, dilewati")

# ============================================================
# FIX C: Tabel metrik bisnis (Win Rate, Sharpe, VaR)
# ============================================================
biz_pattern = re.compile(
    r'(<div class="table-container">.*?(?:Win Rate|Sharpe|VaR|58\.4|72\.3|69\.8|1\.45|0\.95|1\.32|-2\.34|-4\.10|-2\.67).*?</div>\s*</div>)',
    re.DOTALL
)
match2 = biz_pattern.search(content)
if match2:
    old_table_biz = match2.group(1)
    new_table_biz = '''<div class="table-container">
        <div class="table-title">Tabel II. Rencana Evaluasi Metrik Risiko Bisnis (Target Lapisan BI Analytics)
        </div>
        <table>
            <tr>
                <th>Metrik BI / Risiko Bisnis</th>
                <th>XGBoost (Baseline)</th>
                <th>LSTM</th>
                <th>GRU</th>
            </tr>
            <tr>
                <td>Directional Win Rate (%)</td>
                <td colspan="3" style="font-style:italic;">Akan dihitung dari prediksi arah vs. arah aktual pasar</td>
            </tr>
            <tr>
                <td>Sharpe Ratio</td>
                <td colspan="3" style="font-style:italic;">Akan dikalkulasi berdasarkan return prediktif model</td>
            </tr>
            <tr>
                <td>Value at Risk / VaR (95%)</td>
                <td colspan="3" style="font-style:italic;">Akan diestimasi dari distribusi residual prediksi model</td>
            </tr>
        </table>
        <p style="font-size:9.5pt; font-style:italic; text-indent:0; margin-top:4px;">
            * Tabel di atas merupakan rancangan skema transformasi output BI. Nilai aktual akan diisi setelah eksperimen dilaksanakan.
        </p>
    </div>'''
    content = content.replace(old_table_biz, new_table_biz)
    changes.append("TABEL WIN RATE/SHARPE/VAR: Diganti ke rancangan evaluasi (tanpa angka hasil)")
else:
    changes.append("TABEL BISNIS: Pola tidak ditemukan, dilewati")

# ============================================================
# FIX D: Narasi hasil di BAB III (setelah tabel)
# Ubah kalimat yang menyatakan hasil menjadi rencana
# ============================================================
replacements_narasi = [
    # Narasi tentang GRU unggul RMSE
    (
        "Dibalik itu, LSTM mampu memprediksi arah\n"
        "        pergerakan pasar (Win Rate) lebih baik di angka 72.3% dibandingkan GRU (69.8%) dan XGBoost (58.4%).",
        "Selain itu, akan dievaluasi pula kemampuan masing-masing model dalam memprediksi arah\n"
        "        pergerakan pasar (Win Rate) sebagai metrik komplementer terhadap RMSE."
    ),
    # Kalimat hasil GRU terbukti
    (
        "Model GRU terbukti menjadi arsitektur yang paling presisi dengan tingkat kesalahan terendah (RMSE:\n"
        "        0.1058), mengungguli LSTM (RMSE: 0.1145) dan XGBoost (RMSE: 0.1524).",
        "Model GRU dihipotesiskan akan menghasilkan presisi numerik yang lebih baik dibandingkan LSTM dan XGBoost,\n"
        "        yang akan dibuktikan melalui pengujian Walk-Forward Validation."
    ),
    # Kalimat Sharpe di abstrak versi lama
    (
        "mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio (LSTM: 1.45) dan Value at Risk (VaR 95%:\n"
        "        -2.34%).",
        "mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio dan Value at Risk (VaR)."
    ),
    # Narasi hasil di bab lapisan 4
    (
        "Pengujian Walk-Forward Validation menunjukkan temuan komparatif yang\n"
        "        kritis: Model GRU terbukti menjadi arsitektur yang paling presisi dengan tingkat kesalahan terendah (RMSE:\n"
        "        0.1058), mengungguli LSTM (RMSE: 0.1145) dan XGBoost (RMSE: 0.1524). Dibalik itu, LSTM mampu memprediksi arah\n"
        "        pergerakan pasar (Win Rate) lebih baik di angka 72.3% dibandingkan GRU (69.8%) dan XGBoost (58.4%). Dengan\n"
        "        menerjemahkan luaran prediksi ini ke dalam metrik finansial pada antarmuka BI Dashboard, model ini berhasil\n"
        "        mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio (LSTM: 1.45) dan Value at Risk (VaR 95%:\n"
        "        -2.34%).",
        "Pengujian Walk-Forward Validation akan dilakukan untuk mengungkap temuan komparatif antar ketiga model\n"
        "        (LSTM, GRU, XGBoost) berdasarkan metrik RMSE, MAE, dan MAPE. Luaran prediksi selanjutnya akan\n"
        "        ditransformasikan ke dalam metrik finansial pada antarmuka BI Dashboard, seperti Sharpe Ratio,\n"
        "        Win Rate, dan Value at Risk (VaR)."
    ),
    # Kalimat "Contrasting the ensemble..."
    (
        "Contrasting the ensemble baseline, the GRU topology dominated holistic proximity alignments, returning an\n"
        "        optimal 0.1058 RMSE alongside minimal percentage disparity measurements (MAPE 13.13%).",
        "Diperkirakan bahwa arsitektur sekuensial (GRU dan LSTM) akan mendominasi performa dibandingkan\n"
        "        XGBoost, yang akan dikonfirmasi melalui pengujian empiris menggunakan Walk-Forward Validation."
    ),
    # Kalimat "XGBoost drastically failed"
    (
        "Fundamentally, XGBoost drastically failed calculating precise long-term trajectory\n"
        "        targets returning a massive 0.1524 RMSE, heavily confirming standard tree regressions completely\n"
        "        breakdown confronting highly sequential long-memory financial variances.",
        "Diperkirakan bahwa XGBoost sebagai model tabular akan menghasilkan RMSE yang lebih besar dibandingkan\n"
        "        model sekuensial, karena keterbatasannya dalam menangkap dependensi temporal jangka panjang."
    ),
    # Hasil LSTM win rate 72.3% di narasi
    (
        "The Long\n"
        "        Short-Term matrix universally maintained operational trajectory alignment generating phenomenal 72.3%\n"
        "        verified win limits alongside remarkably limited downside constraints (VaR registering minimally at\n"
        "        -2.34%).",
        "Diharapkan model LSTM mampu mempertahankan keunggulan dalam akurasi arah pergerakan pasar\n"
        "        dibandingkan GRU dan XGBoost, berkat kemampuannya menyimpan memori jangka panjang."
    ),
    # Sistem Pendukung Keputusan yang "mengkalkulasikan"
    (
        "Dengan\n"
        "        menerjemahkan luaran prediksi ini ke dalam metrik finansial pada antarmuka BI Dashboard, model ini berhasil\n"
        "        mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio (LSTM: 1.45) dan Value at Risk (VaR 95%:\n"
        "        -2.34%). Proposal penelitian ini diharapkan menghasilkan suatu sistem operasional yang reliabel bagi para\n"
        "        manajer investasi untuk memitigasi risiko pasar cryptocurrency menggunakan akurasi kecerdasan buatan.",
        "Luaran prediksi ini selanjutnya akan diterjemahkan ke dalam metrik finansial pada antarmuka BI Dashboard,\n"
        "        seperti Sharpe Ratio dan Value at Risk (VaR). Proposal penelitian ini diharapkan menghasilkan suatu\n"
        "        sistem operasional yang reliabel bagi para manajer investasi untuk memitigasi risiko pasar cryptocurrency\n"
        "        menggunakan kecerdasan buatan."
    ),
]

for old_n, new_n in replacements_narasi:
    if old_n in content:
        content = content.replace(old_n, new_n)
        changes.append(f"NARASI: Diperbaiki -> '{old_n[:60].strip()}...'")

# ============================================================
# FIX E: Heading BAB hasil -> BAB rencana
# ============================================================
heading_fixes = [
    (
        '<h1>METODOLOGI PELATIHAN DEEP ARCHITECTURE (HYPERPARAMETER)</h1>',
        '<h1>RENCANA METODOLOGI PELATIHAN DEEP ARCHITECTURE (HYPERPARAMETER)</h1>'
    ),
]
for old_h, new_h in heading_fixes:
    if old_h in content:
        content = content.replace(old_h, new_h)
        changes.append(f"HEADING: '{old_h[4:50]}' diperbarui")

# ============================================================
# FIX F: Perbaiki semua angka hasil yang mungkin tersisa
# ============================================================
# Cari sisa angka spesifik dan laporkan
sisa_angka = []
patterns_to_check = [
    r'RMSE[:\s]*0\.1[0-9]+',
    r'72\.3\s*%',
    r'69\.8\s*%',
    r'58\.4\s*%',
    r'VaR.*-2\.3[0-9]',
    r'VaR.*-4\.1[0-9]',
    r'Sharpe.*1\.4[0-9]',
    r'Sharpe.*0\.9[0-9]',
    r'Sharpe.*1\.3[0-9]',
    r'MAE.*0\.094',
    r'MAE.*0\.100',
    r'MAPE.*13\.',
    r'MAPE.*13\.9',
    r'MAPE.*16\.5',
]
for p in patterns_to_check:
    matches = re.findall(p, content)
    if matches:
        sisa_angka.extend(matches)

# ============================================================
# SIMPAN FILE
# ============================================================
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# ============================================================
# LAPORAN
# ============================================================
print("=" * 60)
print("HASIL PERBAIKAN PROPOSAL TESIS")
print("=" * 60)
print(f"\nUkuran asli : {original_len:,} chars")
print(f"Ukuran baru : {len(content):,} chars")
print(f"\nPerubahan yang dilakukan ({len(changes)} item):")
for i, c in enumerate(changes, 1):
    print(f"  {i}. {c}")

if sisa_angka:
    print(f"\n[PERHATIAN] Sisa angka hasil yang mungkin perlu ditinjau:")
    for s in sisa_angka[:15]:
        print(f"  - {s}")
else:
    print("\n[OK] Tidak ada sisa angka hasil eksperimen yang terdeteksi.")

print("\nFile berhasil disimpan!")
