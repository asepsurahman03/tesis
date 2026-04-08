"""
Script to rewrite BAB III in Proposal_Tesis_Bitcoin_BI_Indo.html
Replaces old incomplete BAB III with complete, structured methodology chapter
"""

import re

file_path = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The new BAB III content
NEW_BAB3 = '''    <h1>BAB III: METODOLOGI PENELITIAN DAN ARSITEKTUR BI FRAMEWORK</h1>
    <p style="text-align: justify;">Bab ini menguraikan secara sistematis desain penelitian yang diterapkan untuk menjawab seluruh rumusan masalah yang telah ditetapkan. Penelitian ini menggunakan <em>pendekatan kuantitatif eksperimental berbasis komputasi</em>, di mana keseluruhan proses—mulai dari akuisisi data berskala besar (<em>Big Data</em>), rekayasa fitur teknikal, pelatihan model <em>deep learning</em>, hingga transformasi hasil prediksi menjadi metrik risiko bisnis—dirancang dalam satu ekosistem yang terintegrasi, dapat direproduksi secara deterministik, dan dapat divalidasi secara empiris [23], [24].</p>

    <h2>A. Desain dan Pendekatan Penelitian</h2>
    <p style="text-align: justify;">Penelitian ini menggunakan <strong>metode penelitian eksperimental komparatif</strong> (<em>comparative experimental research</em>) yang bersifat kuantitatif. Pendekatan ini dipilih karena tujuan utama penelitian adalah membandingkan performa tiga algoritma prediksi (LSTM, GRU, dan XGBoost) secara objektif dan terukur pada dataset yang sama, dengan kondisi pengujian yang identik dan terkontrol. Kerangka desain penelitian berpijak pada paradigma <em>Design Science Research</em> (DSR), di mana luaran utama penelitian adalah sebuah artefak sistem (<em>4-Layer BI Framework</em>) yang dapat dievaluasi manfaatnya secara langsung oleh para pemangku kepentingan di dunia nyata [17], [28].</p>
    <p style="text-align: justify;">Penelitian ini bersifat <strong>evaluatif dan komparatif</strong>: menginvestigasi model mana yang paling tepat untuk konteks pengambilan keputusan investasi yang berbeda, serta membangun sistem pendukung keputusan berkelanjutan yang dapat diandalkan secara operasional oleh manajer investasi.</p>

    <h2>B. Alur Tahapan Penelitian</h2>
    <p style="text-align: justify;">Pelaksanaan penelitian ini disusun ke dalam <strong>lima tahapan pokok yang saling berkesinambungan</strong>. Setiap tahapan memiliki masukan (<em>input</em>), proses, dan keluaran (<em>output</em>) yang terdefinisi secara eksplisit sehingga seluruh alur penelitian bersifat dapat direproduksi oleh peneliti lain. Diagram alur pada Gambar 3.1 menjabarkan prosedur kerja secara runut: dimulai dari pengumpulan dan pra-pemrosesan data historis, rekayasa 15 fitur teknikal, pelatihan tiga model prediktif secara komparatif, evaluasi performa menggunakan metrik teknis dan bisnis, hingga integrasi hasil prediksi ke dalam prototipe <em>Business Intelligence Decision Support Dashboard</em>.</p>

    <div class="svg-figure" style="margin: 30px 0;">
        <img src="../04_Visualizations/Tahapan_Penelitian_BI.png" alt="Alur Lima Tahapan Metodologi Penelitian Bitcoin BI" style="width: 100%; max-width: 850px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #cbd5e1;" />
        <div class="figure-caption" style="text-align: center; margin-top: 12px; color: #475569; font-size: 10pt;">
            <strong>Gambar 3.1</strong> Alur Lima Tahapan Metodologi Penelitian: dari Akuisisi <em>Big Data</em> Binance API hingga Operasionalisasi Dasbor Kecerdasan Bisnis Eksekutif.
        </div>
    </div>

    <p style="text-align: justify;">Kelima tahapan di atas membentuk satu <em>pipeline</em> penelitian yang koheren. Tahap 1 dan 2 membangun fondasi kualitas data; Tahap 3 merupakan inti eksperimen komputasi; Tahap 4 menghasilkan bukti empiris komparatif; dan Tahap 5 mentransformasikan temuan ilmiah menjadi sistem yang dapat langsung dioperasikan oleh praktisi industri.</p>

    <h2>C. Kerangka Pemikiran dan Arsitektur Sistem (4-Layer BI Framework)</h2>
    <p style="text-align: justify;">Untuk menjawab tantangan penelitian ini secara sistemik, dirancanglah sebuah <strong>Kerangka Kerja <em>Business Intelligence</em> Empat Lapis</strong> (<em>4-Layer BI Framework</em>) yang mengintegrasikan seluruh komponen penelitian ke dalam satu arsitektur terpadu. Kerangka ini menggambarkan bagaimana data mentah mentransformasi dirinya melalui empat lapisan fungsional yang saling terhubung hingga menjadi sistem penunjang keputusan yang dapat langsung digunakan oleh manajer investasi. Gambar 3.2 menyajikan arsitektur lengkap dari kerangka pemikiran ini.</p>

    <div class="svg-figure" style="margin: 30px 0;">
        <img src="../04_Visualizations/Kerangka_Pemikiran_BI.png" alt="Kerangka Pemikiran 4-Layer BI Framework Bitcoin" style="width: 100%; max-width: 850px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #cbd5e1;" />
        <div class="figure-caption" style="text-align: center; margin-top: 12px; color: #475569; font-size: 10pt;">
            <strong>Gambar 3.2</strong> Kerangka Pemikiran Penelitian: Arsitektur <em>Business Intelligence</em> Empat Lapis — dari Sumber Data <em>Binance API</em> menuju <em>Decision Support Dashboard</em> dengan Metrik Risiko Eksekutif.
        </div>
    </div>

    <p style="text-align: justify;">Sebagaimana diilustrasikan pada Gambar 3.2, keempat lapisan arsitektur BI Framework bekerja secara sekuensial:</p>
    <ol class="rumusan">
        <li><strong>Lapisan 1 &ndash; Sumber &amp; Ingesti Data:</strong> Mengakuisisi 43.788 rekaman harga BTC/USDT per jam selama 5 tahun (2021&ndash;2026) dari <em>Binance Spot API</em>, yang memenuhi dimensi <em>Volume</em> dan <em>Velocity</em> Big Data.</li>
        <li><strong>Lapisan 2 &ndash; Rekayasa Fitur &amp; Pemodelan:</strong> Mengonstruksi 15 indikator teknikal, melatih tiga algoritma (LSTM, GRU, XGBoost) dengan metodologi <em>Walk-Forward Validation</em>, dan mengoptimalkan hiperparameter menggunakan <em>Grid Search</em>.</li>
        <li><strong>Lapisan 3 &ndash; Evaluasi &amp; <em>Explainable AI</em>:</strong> Mengukur performa melalui metrik teknis (RMSE, MAE, MAPE) dan metrik bisnis (<em>Win Rate</em>), serta menganalisis kontribusi fitur secara transparan menggunakan metode SHAP.</li>
        <li><strong>Lapisan 4 &ndash; BI Dashboard &amp; Penunjang Keputusan:</strong> Mentransformasikan keluaran prediksi menjadi metrik risiko eksekutif (<em>Sharpe Ratio</em>, VaR 95%, <em>Win Rate</em>) dan menyajikannya dalam prototipe <em>Decision Support Dashboard</em> yang fungsional.</li>
    </ol>

    <h2>D. Populasi, Sampel, dan Sumber Data</h2>
    <p style="text-align: justify;">Populasi dalam penelitian ini adalah seluruh data historis pergerakan harga pasangan aset BTC/USDT yang tersedia pada platform <em>Binance Exchange</em>. Sampel yang digunakan adalah data berfrekuensi tinggi dengan interval satu jam (<em>1h OHLCV</em>) yang tercatat pada periode <strong>Maret 2021 hingga awal 2026</strong>, dengan total <strong>43.788 baris rekaman</strong>. Penentuan periode ini didasarkan pada pertimbangan bahwa rentang waktu tersebut mencakup satu siklus penuh pasar kripto: kondisi <em>bull market</em> (ATH $69.000, Nov. 2021), <em>bear market</em> ekstrem (krisis FTX 2022), pemulihan, <em>halving</em> ke-4 (April 2024), hingga ATH baru di atas $100.000 (akhir 2024) [5], [6].</p>
    <p style="text-align: justify;">Setiap baris rekaman data mengandung enam variabel dasar: harga Pembukaan (<em>Open</em>), harga Tertinggi (<em>High</em>), harga Terendah (<em>Low</em>), harga Penutupan (<em>Close</em>), Volume transaksi, dan Cap waktu (<em>Timestamp</em>). Keenam variabel inilah yang menjadi bahan baku utama rekayasa 15 indikator teknikal [1], [13].</p>

    <h2>E. Pra-Pemrosesan Data (ETL): <em>Extraction, Transformation, and Load</em></h2>
    <p style="text-align: justify;">Demi menjaga integritas dan kejujuran data (<em>Veracity</em>), data mentah ditransisikan melalui tiga tahapan pra-pemrosesan (<em>ETL</em>): <strong>(1) Deteksi dan Penanganan Nilai Hilang</strong> &mdash; setiap celah data (<em>missing values</em>) yang disebabkan oleh keterlambatan respons server API ditambal menggunakan metode <em>Linear Polynomial Interpolation</em>; <strong>(2) Deteksi Pencilan</strong> (<em>Outlier Detection</em>) menggunakan metode <em>Interquartile Range</em> (IQR) untuk mengidentifikasi titik data ekstrem; dan <strong>(3) Normalisasi Data</strong> menggunakan metode <em>Min-Max Normalization</em> untuk mengecilkan rentang nilai ke skala [0, 1] guna mencegah ledakan gradien (<em>gradient explosion</em>) pada lapisan Neural Network:</p>

    <div class="equation">
        $$ X_{\\text{norm}} = \\frac{X - X_{\\min}}{X_{\\max} - X_{\\min}} \\eqno{(1)} $$
    </div>

    <h2>F. Rekayasa Fitur Teknikal (<em>Feature Engineering</em>)</h2>
    <p style="text-align: justify;">Memasukkan data harga mentah secara langsung ke dalam jaringan saraf tiruan akan sangat membatasi kemampuan model dalam mendeteksi pola-pola pasar yang kompleks. Oleh karena itu, dilakukan <em>Feature Engineering</em> — proses transformasi variabel harga mentah menjadi 15 indikator teknikal yang kaya informasi. Kelimabelas indikator ini dikelompokkan ke dalam lima kategori fungsional sebagaimana dijabarkan pada Tabel 3.1:</p>

    <div class="table-container">
        <div class="table-title">Tabel 3.1. Spesifikasi Lima Belas Fitur Teknikal sebagai Input Model Prediktif</div>
        <table>
            <tr>
                <th style="width:8%">No</th>
                <th style="width:32%">Fitur Teknikal</th>
                <th style="width:30%">Fungsi Observasi</th>
                <th style="width:30%">Formulasi Matematika</th>
            </tr>
            <tr>
                <td>1&ndash;5</td>
                <td>Open, High, Low, Close, Volume</td>
                <td>Data Harga Dasar OHLCV Raw</td>
                <td>\\(O_t, H_t, L_t, P_t, V_t\\)</td>
            </tr>
            <tr>
                <td>6&ndash;7</td>
                <td>Moving Average-7 (MA-7), MA-21</td>
                <td>Estimasi Tren Jangka Pendek &amp; Menengah</td>
                <td>\\(\\text{MA}_n = \\frac{1}{n}\\sum_{i=0}^{n-1} P_{t-i}\\)</td>
            </tr>
            <tr>
                <td>8</td>
                <td>Relative Strength Index (RSI-14)</td>
                <td>Deteksi Zona Jenuh Beli / Jenuh Jual</td>
                <td>Persamaan. (3)</td>
            </tr>
            <tr>
                <td>9&ndash;10</td>
                <td>MACD &amp; Batas Sinyal MACD</td>
                <td>Kalkulasi Akselerasi &amp; Momentum Tren</td>
                <td>Persamaan. (2)</td>
            </tr>
            <tr>
                <td>11&ndash;13</td>
                <td>Bollinger Upper, Lower, Width</td>
                <td>Kurungan Lebar Volatilitas Pasar</td>
                <td>\\(\\text{MA}_{20} \\pm 2\\sigma\\) &amp; Pers. (4)</td>
            </tr>
            <tr>
                <td>14</td>
                <td>Logarithm Returns</td>
                <td>Harmonisasi Data ke Distribusi Stasioner</td>
                <td>\\(r_t = \\ln(P_t / P_{t-1})\\)</td>
            </tr>
            <tr>
                <td>15</td>
                <td>Rolling Volatility 24-Jam</td>
                <td>Kuantifikasi Risiko Simpangan Harian</td>
                <td>\\(\\sigma_{24h}\\) &amp; Pers. (4)</td>
            </tr>
        </table>
    </div>

    <h2>G. Desain Pelatihan Model dan Validasi (<em>Walk-Forward Validation</em>)</h2>
    <p style="text-align: justify;">Risiko terbesar dalam pemodelan deret waktu finansial adalah <em>data leakage</em> — bocornya informasi dari data pengujian masa depan ke dalam proses pelatihan. Untuk mengeliminasi risiko ini, penelitian ini secara ketat menerapkan metodologi <strong><em>Walk-Forward Validation</em></strong>. Dalam skema ini, model dilatih pada jendela data historis yang terus bergeser maju, dan dievaluasi pada 168 jam data berikutnya (setara satu minggu) yang belum pernah dilihat oleh model sebelumnya. Dataset dibagi dengan proporsi <strong>80% Training | 10% Validasi | 10% Testing</strong>.</p>
    <p style="text-align: justify;">Ketiga model dilatih dan dibandingkan pada kondisi yang identik:</p>
    <ul class="manfaat">
        <li><strong>LSTM</strong> &mdash; Arsitektur dengan tiga gerbang (Input, Forget, Output) untuk mempertahankan memori jangka panjang [10].</li>
        <li><strong>GRU</strong> &mdash; Arsitektur yang disederhanakan dengan dua gerbang (Update, Reset) untuk efisiensi komputasi yang lebih tinggi [11].</li>
        <li><strong>XGBoost</strong> &mdash; Model <em>ensemble baseline</em> berbasis pohon keputusan sebagai pembanding non-sekuensial [22].</li>
    </ul>
    <p style="text-align: justify;">Optimasi hiperparameter dilakukan menggunakan <em>Grid Search Cross-Validation</em> yang mencakup: jumlah <em>Hidden Layers</em> (1&ndash;3 lapis), jumlah unit neuron per lapisan (32&ndash;128), <em>Dropout Rate</em> (0,1&ndash;0,3), dan <em>Learning Rate</em> pada optimizer Adam [29]. Mekanisme <em>Early Stopping</em> diterapkan untuk mencegah <em>overfitting</em> [30], [31].</p>

    <h2>H. Formulasi Matematis Indikator Teknikal Utama</h2>
    <h3>1. MACD dan RSI (Detektor Momentum Tren)</h3>
    <p style="text-align: justify;">Akselerasi perubahan tren pasar (<em>trend reversals</em>) dideteksi menggunakan rumusan <em>Moving Average Convergence Divergence</em> (MACD):</p>
    <div class="equation">
        $$ MACD = EMA_{12}(P) - EMA_{26}(P) \\eqno{(2)} $$
    </div>
    <p style="text-align: justify;">Zona kejenuhan pasar (<em>overbought/oversold</em>) dikuantifikasi menggunakan <em>Relative Strength Index</em> (RSI-14):</p>
    <div class="equation">
        $$ RSI = 100 - \\left(\\frac{100}{1 + \\frac{EMA(\\text{Gain})}{EMA(\\text{Loss})}}\\right) \\eqno{(3)} $$
    </div>

    <h3>2. Volatilitas Terukur dan Stabilisasi Stasioner</h3>
    <p style="text-align: justify;">Simpangan volatilitas harian diukur menggunakan deviasi bergulir (<em>Rolling Standard Deviation</em>) untuk menjaga stasioneritas data:</p>
    <div class="equation">
        $$ \\sigma_t = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (\\Delta P_i - \\bar{P})^2} \\eqno{(4)} $$
    </div>

    <h3>3. Mekanisme Gerbang LSTM</h3>
    <p style="text-align: justify;">Superioritas LSTM dalam mempertahankan konteks jangka panjang berpijak pada mekanisme gerbang selektif. Gerbang <em>Forget</em> (\\(f_t\\)) dan gerbang <em>Input</em> (\\(i_t\\)) bekerja secara kolaboratif mengatur informasi mana yang dipertahankan atau dihapus dari memori sel:</p>
    <div class="equation">
        $$ f_t = \\sigma(W_f \\cdot [h_{t-1}, x_t] + b_f) \\eqno{(5)} $$
    </div>
    <div class="equation">
        $$ i_t = \\sigma(W_i \\cdot [h_{t-1}, x_t] + b_i) \\eqno{(6)} $$
    </div>

    <h3>4. Gerbang Pembaruan GRU</h3>
    <p style="text-align: justify;">GRU menyatukan mekanisme gerbang LSTM menjadi satu gerbang pembaruan (<em>Update Gate</em> \\(z_t\\)) yang lebih efisien secara komputasi tanpa mengorbankan kemampuan memori temporal:</p>
    <div class="equation">
        $$ z_t = \\sigma(W_z \\cdot [h_{t-1}, x_t] + b_z) \\eqno{(7)} $$
    </div>

    <h2>I. Evaluasi Performa dan Transformasi ke BI Dashboard</h2>
    <p style="text-align: justify;">Evaluasi model dilakukan pada dua dimensi yang saling melengkapi. <strong>Dimensi Pertama</strong> adalah metrik teknis standar: <em>Root Mean Square Error</em> (RMSE) — mengukur rata-rata kesalahan kuadrat prediksi; <em>Mean Absolute Error</em> (MAE) — mengukur rata-rata kesalahan absolut; dan <em>Mean Absolute Percentage Error</em> (MAPE) — mengukur kesalahan relatif terhadap nilai aktual. <strong>Dimensi Kedua</strong> adalah metrik bisnis: <em>Directional Win Rate</em> — persentase ketepatan prediksi arah naik/turun yang memiliki implikasi keputusan langsung bagi investor.</p>
    <p style="text-align: justify;">Keluaran dari model terbaik selanjutnya ditransformasikan ke dalam tiga metrik risiko eksekutif pada lapisan BI Dashboard: (1) <strong><em>Sharpe Ratio</em></strong> sebagai ukuran efisiensi imbal hasil per unit risiko (ambang target &ge;1,0); (2) <strong><em>Value at Risk</em> (VaR 95%)</strong> sebagai estimasi kerugian maksimum pada tingkat kepercayaan 95%; dan (3) <strong><em>Directional Win Rate</em></strong> sebagai indikator arah keputusan dengan ambang target &ge;55%. Ketiga metrik ini disajikan secara terintegrasi dalam <em>Decision Support Dashboard</em> yang dirancang untuk dapat langsung diinterpretasikan oleh manajer investasi tanpa memerlukan keahlian teknis mendalam [12], [13].</p>'''

# Find the old BAB III section and replace it
# Start marker: <h1>BAB III:
# End marker: just before <h2 ...>Daftar Pustaka
old_start = content.find('    <h1>BAB III:')
old_end = content.find('\n    <h2 style="text-align:center; text-transform:uppercase;">Daftar Pustaka')

if old_start == -1:
    print("ERROR: Could not find BAB III start marker")
    exit(1)
if old_end == -1:
    print("ERROR: Could not find Daftar Pustaka end marker")
    exit(1)

print(f"Found BAB III at position {old_start}")
print(f"Found Daftar Pustaka at position {old_end}")
print(f"Old BAB III length: {old_end - old_start} chars")

new_content = content[:old_start] + NEW_BAB3 + '\n\n' + content[old_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ BAB III rewritten successfully!")
print(f"New file size: {len(new_content)} bytes")
