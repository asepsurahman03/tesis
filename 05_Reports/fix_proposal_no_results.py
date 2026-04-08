# fix_proposal_no_results.py
# Menghapus semua angka hasil eksperimen dari BAB I proposal
# dan menggantinya dengan bahasa prospektif yang sesuai untuk proposal tesis

filepath = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ========== FIX 1: Rumusan Masalah poin 3 - hapus angka hasil ==========
old = (
    "        <li>Bagaimana karakteristik dan implikasi dari <em>tradeoff</em> performa yang terjadi antara model GRU\n"
    "            (yang unggul dalam presisi numerik dengan RMSE 0,1058) dan model LSTM (yang unggul dalam akurasi arah\n"
    "            pergerakan pasar dengan <em>Win Rate</em> 72,3%) untuk konteks pengambilan keputusan investasi yang\n"
    "            berbeda?</li>\n"
)
new = (
    "        <li>Bagaimana karakteristik dan implikasi <em>tradeoff</em> performa yang diperkirakan akan terjadi\n"
    "            antara model GRU (yang dihipotesiskan lebih unggul dalam presisi numerik) dan model LSTM (yang\n"
    "            dihipotesiskan lebih unggul dalam akurasi arah pergerakan pasar) untuk konteks pengambilan keputusan\n"
    "            investasi yang berbeda?</li>\n"
)
content = content.replace(old, new)

# ========== FIX 2: Tujuan poin 5 - hapus angka hasil spesifik ==========
old = (
    "        <li>Mentransformasikan keluaran prediktif model Deep Learning ke dalam metrik risiko finansial\n"
    "            eksekutif&mdash;termasuk <em>Sharpe Ratio</em> (LSTM: 1,45), <em>Value at Risk</em> (VaR 95%: -2,34%),\n"
    "            dan <em>Directional Win Rate</em> (LSTM: 72,3%)&mdash;yang disajikan dalam prototipe <em>BI Decision\n"
    "            Support Dashboard</em> yang fungsional dan siap dioperasikan oleh manajemen lembaga keuangan.</li>\n"
)
new = (
    "        <li>Mentransformasikan keluaran prediktif model Deep Learning ke dalam metrik risiko finansial\n"
    "            eksekutif&mdash;meliputi <em>Sharpe Ratio</em>, <em>Value at Risk</em> (VaR pada tingkat kepercayaan\n"
    "            95%), dan <em>Directional Win Rate</em>&mdash;yang akan disajikan dalam prototipe <em>BI Decision\n"
    "            Support Dashboard</em> yang fungsional dan siap dioperasikan oleh manajemen lembaga keuangan.</li>\n"
)
content = content.replace(old, new)

# ========== FIX 3: Manfaat Teoritis - hapus angka perbandingan model ==========
old = (
    "        <li>Membuktikan secara empiris keberadaan <em>tradeoff</em> antara akurasi numerik (RMSE: GRU 0,1058\n"
    "            vs. LSTM 0,1145) dan akurasi arah pasar (Win Rate: LSTM 72,3% vs. GRU 69,8%), yang merupakan temuan\n"
    "            kritis bagi pengembangan strategi pemodelan finansial ke depan.</li>\n"
)
new = (
    "        <li>Mengidentifikasi secara empiris keberadaan <em>tradeoff</em> antara akurasi numerik (RMSE) dan\n"
    "            akurasi arah pasar (<em>Win Rate</em>) pada arsitektur Deep Learning finansial, yang diharapkan\n"
    "            menjadi kontribusi kritis bagi pengembangan strategi pemodelan ke depan.</li>\n"
)
content = content.replace(old, new)

# ========== FIX 4: Manfaat Praktis - hapus angka VaR dan Sharpe ==========
old = (
    "        <li>Membantu lembaga keuangan dalam mengukur dan memitigasi risiko paparan aset kripto secara kuantitatif\n"
    "            melalui kalkulasi otomatis metrik risiko seperti <em>Value at Risk</em> (VaR 95%: -2,34%) dan\n"
    "            <em>Sharpe Ratio</em> (LSTM: 1,45) yang dihasilkan dari model terbaik.</li>\n"
)
new = (
    "        <li>Membantu lembaga keuangan dalam mengukur dan memitigasi risiko paparan aset kripto secara kuantitatif\n"
    "            melalui kalkulasi otomatis metrik risiko seperti <em>Value at Risk</em> (VaR) dan\n"
    "            <em>Sharpe Ratio</em> yang akan dihasilkan dari model terbaik yang ditemukan dalam penelitian.</li>\n"
)
content = content.replace(old, new)

# ========== FIX 5: Latar Belakang - hapus angka spesifik hasil model ==========
old = (
    "        Seorang manajer investasi tidak dapat mengambil keputusan strategis\n"
    "        semata dari nilai RMSE sebuah model; mereka membutuhkan metrik bisnis yang terukur dan dapat ditafsirkan,\n"
    "        seperti <em>Win Rate</em> (akurasi arah pergerakan pasar), <em>Sharpe Ratio</em> (efisiensi imbal hasil per\n"
    "        unit risiko), dan <em>Value at Risk</em> (estimasi kerugian maksimum pada tingkat kepercayaan tertentu)\n"
    "        [13], [14].</p>\n"
)
new = (
    "        Seorang manajer investasi tidak dapat mengambil keputusan strategis\n"
    "        semata dari nilai RMSE sebuah model; mereka membutuhkan metrik bisnis yang terukur dan dapat ditafsirkan,\n"
    "        seperti <em>Win Rate</em> (akurasi arah pergerakan pasar), <em>Sharpe Ratio</em> (efisiensi imbal hasil per\n"
    "        unit risiko), dan <em>Value at Risk</em> (estimasi kerugian maksimum pada tingkat kepercayaan\n"
    "        tertentu) [13], [14].</p>\n"
)
content = content.replace(old, new)

# ========== FIX 6: Sistematika BAB V - ubah dari 'hasil' ke 'rencana' ==========
old = (
    "        <strong>BAB V &ndash; HASIL EKSPERIMEN DAN ANALISIS PERBANDINGAN</strong> menyajikan dan menganalisis\n"
    "        hasil empiris dari pengujian Walk-Forward Validation secara komprehensif, memuat tabel komparasi metrik\n"
    "        performa teknis (RMSE, MAE, MAPE), analisis residual, serta transformasi keluaran prediktif ke dalam\n"
    "        metrik risiko bisnis (Win Rate, Sharpe Ratio, Value at Risk). Temuan utama&mdash;termasuk\n"
    "        <em>tradeoff</em> GRU vs. LSTM&mdash;diinterpretasikan secara mendalam dalam konteks investasi nyata.\n"
)
new = (
    "        <strong>BAB V &ndash; RENCANA PENGUJIAN DAN EVALUASI MODEL</strong> menguraikan rencana pengujian\n"
    "        empiris secara komprehensif menggunakan metodologi Walk-Forward Validation. Bab ini memaparkan skema\n"
    "        komparasi metrik performa teknis (RMSE, MAE, MAPE) yang akan dievaluasi antar model, rencana analisis\n"
    "        residual, serta rencana transformasi keluaran prediktif ke dalam metrik risiko bisnis (Win Rate, Sharpe\n"
    "        Ratio, Value at Risk). Bab ini juga menguraikan hipotesis mengenai kemungkinan <em>tradeoff</em> antara\n"
    "        GRU dan LSTM yang akan diinvestigasi secara mendalam dalam konteks investasi nyata.\n"
)
content = content.replace(old, new)

# ========== FIX 7: Sistematika BAB VI - ubah dari 'merangkum' ke 'akan merangkum' ==========
old = (
    "        <strong>BAB VI &ndash; KESIMPULAN DAN REKOMENDASI</strong> merangkum kontribusi ilmiah dan praktis utama\n"
    "        dari penelitian ini, menjawab secara langsung seluruh rumusan masalah yang telah ditetapkan, serta\n"
    "        mengajukan saran dan arah penelitian lanjutan yang dapat mengembangkan kerangka kerja BI-ML Framework\n"
    "        ini lebih jauh di masa depan.\n"
)
new = (
    "        <strong>BAB VI &ndash; KESIMPULAN DAN REKOMENDASI</strong> akan merangkum kontribusi ilmiah dan praktis\n"
    "        utama yang diharapkan dari pelaksanaan penelitian ini, menjawab seluruh rumusan masalah yang telah\n"
    "        ditetapkan berdasarkan hasil eksperimen, serta mengajukan saran dan arah penelitian lanjutan yang dapat\n"
    "        mengembangkan kerangka kerja BI-ML Framework ini lebih jauh di masa depan.\n"
)
content = content.replace(old, new)

# ========== FIX 8: Abstrak - angka hasil boleh ada di abstrak sebagai preliminary/expected ==========
# Tapi angka di abstrak perlu diframing ulang sebagai "hasil awal" bukan final
# Cari bagian abstrak
abstrak_old = (
    "        mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio (LSTM: 1.45) dan Value at Risk (VaR 95%:\n"
    "        -2.34%). Proposal penelitian ini diharapkan menghasilkan suatu sistem operasional yang reliabel bagi para\n"
    "        manajer investasi untuk memitigasi risiko pasar cryptocurrency menggunakan akurasi kecerdasan buatan.\n"
)
abstrak_new = (
    "        mengkalkulasikan batas paparan risiko korporasi seperti <em>Sharpe Ratio</em> dan\n"
    "        <em>Value at Risk</em> (VaR). Proposal penelitian ini diharapkan menghasilkan suatu sistem operasional\n"
    "        yang reliabel bagi para manajer investasi untuk memitigasi risiko pasar cryptocurrency menggunakan\n"
    "        kecerdasan buatan.\n"
)
content = content.replace(abstrak_old, abstrak_new)

# ========== Verifikasi ==========
checks_should_be_gone = [
    'RMSE 0,1058',
    'Win Rate</em> 72,3%',
    'VaR 95%: -2,34%',
    'Sharpe Ratio</em> (LSTM: 1,45)',
    'RMSE: GRU 0,1058',
    'Win Rate: LSTM 72,3%',
    'LSTM: 1.45',
    '-2.34%',
]

checks_should_exist = [
    '1.1 Latar Belakang',
    '1.2 Identifikasi Masalah',
    '1.3 Rumusan Masalah',
    '1.4 Tujuan Penelitian',
    '1.5 Manfaat Penelitian',
    '1.6 Batasan Penelitian',
    '1.7 Sistematika Penulisan',
    'RENCANA PENGUJIAN',
    'Walk-Forward Validation',
    'Value at Risk',
    'Sharpe Ratio',
    'Win Rate',
]

print('=== CEK angka hasil (seharusnya HILANG) ===')
all_clean = True
for check in checks_should_be_gone:
    found = check in content
    status = 'MASIH ADA!' if found else 'BERSIH OK'
    if found:
        all_clean = False
    print(f'  [{status}] {check}')

print('\n=== CEK konten penting (seharusnya ADA) ===')
all_present = True
for check in checks_should_exist:
    found = check in content
    status = 'OK' if found else 'HILANG!'
    if not found:
        all_present = False
    print(f'  [{status}] {check}')

if all_clean and all_present:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\nSUCCESS! File disimpan. Ukuran: {len(content)} chars')
else:
    print('\nADA MASALAH - File TIDAK disimpan, periksa di atas!')
