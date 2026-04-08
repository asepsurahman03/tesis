import re
import os

file_path = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

new_tbody = '''            <tbody>
                <tr>
                    <td>1</td>
                    <td><em>Forecasting and trading cryptocurrencies with machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Sebastião &amp; Godinho (2021) [4]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Evaluasi ketangguhan algoritma <em>Machine Learning</em> klasik (Random Forest, SVM, Regresi Logistik) dalam memprediksi arah pergerakan kripto harian untuk simulasi <em>trading</em> riil.<br><strong>Algoritma:</strong> Random Forest, SVM.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Random Forest secara konsisten menghasilkan <em>Directional Accuracy</em> melampaui 55% dan berhasil mencetak margin imbal hasil di atas strategi <em>Buy-and-Hold</em> standar.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Terbatas pada algoritma statis yang gagal merekam dependensi sekuensial panjang (memori waktu) pada volatilitas kripto. Tidak adanya XAI (transparansi) dan metrik risiko seperti VaR membenarkan urgensi tesis Anda yang menggunakan GRU/LSTM serta lapisan interpretatif SHAP di dalam antarmuka BI Dashboard.</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><em>Applications of deep learning in stock market prediction: Recent progress</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Jiang (2021) [21]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Kajian literatur ekstensif tentang implementasi arsitektur <em>Deep Learning</em> pada penangkapan tren dan turbulensi harga ekstrim deret waktu aset finansial.<br><strong>Algoritma:</strong> RNN, LSTM, CNN.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Arsitektur gerbang LSTM tervalidasi sangat efektif mengatasi masalah <em>vanishing gradient</em>, mendominasi model konvensional untuk mengunci pola masa lalu yang panjang (<em>Long-Memory effects</em>).</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Kompleksitas arsitektur sel LSTM menyebabkan laju iterasi lambat sangat membebani sistem komputasi berfrekuensi tinggi (seperti data per-jam). Riset ini tidak membandingkan LSTM secara langsung dengan varian efisiennya (GRU), posisi krusial yang dibenturkan pada simulasi kinerja prediktif penelitian tesis ini.</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><em>Short-term bitcoin market prediction via machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Jaquart dkk. (2021) [8]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Prediksi harga asimetris Bitcoin menggunakan data makro sentimen dan log teknikal berfrekuensi sangat pendek, mulai dari observasi hitungan per-jam hingga 24 jam.<br><strong>Algoritma:</strong> Prediksi Ansambel regresi.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Frekuensi pengamatan 1-24 jam adalah penekan RMSE paling kritis. Arsitektur ensemble terbukti optimal mengatasi tren kejut dalam jendela waktu sesingkat itu tanpa tertahan linieritas.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Rawan bias pengamatan akibat metodologi komparatif persilangan silang statis (K-Fold murni). Situasi ini menjadi fondasi valid bagi tesis Anda untuk beralih mengimplementasikan <em>Walk-Forward Validation</em> absolut, untuk memastikan keabsahan DSS (<em>Decision Support System</em>) tanpa kebocoran data masa depan.</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><em>Prediction of cryptocurrency returns using machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Akyildirim dkk. (2021) [29]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Memilah tingkat pencarian profit nilai imbal hasil ekstrim dari kelas derivatif kripto melalui serangkaian algoritma penalti loss pemotong kelebihan galat fluktuasi acak.<br><strong>Algoritma:</strong> XGBoost (<em>Extreme Gradient Boosting</em>).</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Logika penalti kerugian dari XGBoost sangat dominan meredam efek pencilan tak terkontrol di batas tebing angka acak, menjadikannya tameng presisi melawan volatilitas <em>noise</em>.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Prediksi masih di dalam ruang hitam tertutup tanpa visualisasi fitur kausal di mata manajer investasi rasional. Tesis Anda menjadikan XGBoost sekadar <em>Baseline Anchor</em> pelompat ukur akurasi model, untuk dikomparasi kapabilitas pembedahannya melawan kecerdasan saraf jaringan dalam GRU &amp; LSTM dan XAI SHAP.</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><em>How do economic policy uncertainty and geopolitical risk drive Bitcoin volatility?</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Ben Nouir dkk. (2023) [6]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Pembuktian rasio rambatan efek guncangan kepanikan geopolitik global bersenjata serta gejolak kepanikan kebijakan bank sentral memicu jatuh naiknya posisi pasokan Bitcoin.<br><strong>Algoritma:</strong> Model regresi ekonometrika VAR klasik.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Berita geopolitik destruktif sangat cepat diproses pasar menjadi tren kejut penurunan beruntun asimetris yang mematahkan segenap postulat keseimbangan Hipotesis Pasar Efisien (EMH).</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Riset terbatas merekam fenomena kepanikan semata melalui ekonometrika linier, tidak sanggup memitigasi kerugian. Keterbatasan struktural murni ini dijawab dengan integrasi konversi kalkulasi riset pada model Anda menjadi metrik perlindungan eksekutif mutlak (misalnya, simulasi batas rugi harian via 95% perhitungan *Value at Risk* di level BI Dashboard).</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><em>Forecasting cryptocurrency prices using LSTM, GRU, and bi-directional LSTM</em><br><span style="color: #f39c12; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q2)</span></td>
                    <td>Seabe dkk. (2023) [13]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Evaluasi kehandalan duel langsung sesama keluarga komputasi syaraf pengunci memori deret waktu untuk menuntaskan eror reduksi pada interval harian harga <em>cryptocurrency</em>.<br><strong>Algoritma:</strong> LSTM konvensional, penyesuaian batas GRU, Bi-LSTM.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Struktur efisien sel memori GRU berhasil memangkas lambatnya penyesuaian bobot LSTM secara telak, sembari simultan juga menghancurkan simpangan nilai RMSE pada rentang tes volatilitas pendek.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Riset terjebak obsesi pencapaian simpangan nilai mutlak persentase yang abai menerjemahkan maknanya secara industri ritel manajerial. Oleh karenanya, rumusan objektif Tesis Anda merancang eksplorasi **<em>Trade-Off Accuracy vs Profit Precision</em>**, yang menimbang ketepatan arah gerak pasar secara proporsional sebagai pertimbangan rekomendasi performa.</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><em>Explainable artificial intelligence modeling to forecast bitcoin prices</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Goodell dkk. (2023) [16]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Introduksi algoritma analitika persentase matematis teori permainan kooperatif menembus proteksi pembobotan model <em>Deep Learning</em> pada penentuan keputusan beli dan jual pasar digital.<br><strong>Algoritma:</strong> Metodologi ekuilibrium distribusi fitur XAI SHAP.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Sistem XAI SHAP terbukti gemilang mengungkap bahwa jaringan syaraf independen bersandar radikal memprioritaskan fitur derivasi tren sentimen momentum (seperti indikator RSI/Moving Average) ketimbang pada titik keseimbangan harga biasa semata.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan (Gap ke Tesis):</strong> Fokus XAI terbatas meratifikasi algoritma parsial mandiri tunggal. Pada pelaporan evaluasi parameter ini, tesis Anda memaksa penetrasi transendental XAI menjadi fasilitator parameter uji di medan adu tinju memori lintas arsitektur langsung dalam duel ekstrem antara pemenang efisien sel GRU murni di hadapan presisi bobot retensi arah jangka waktu LSTM model komparatif yang disatupadankan pada Dashboard.</td>
                </tr>
            </tbody>'''

pattern = re.compile(r'<tbody>.*?</tbody>', re.DOTALL)

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub(new_tbody, content)

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {file_path}')
    else:
        print(f'No replacement needed or tbody not found: {file_path}')
else:
    print(f'Not found: {file_path}')
