import io

new_text_1 = '''    <div class="abstract-section">
        <strong>Abstrak</strong> Volatilitas yang tinggi pada pasar cryptocurrency menuntut adanya model prediksi yang mampu mengintegrasikan data berskala besar (Big Data) secara real-time ke dalam sistem pendukung keputusan (Decision Support System). Penelitian ini mengusulkan kerangka kerja Business Intelligence (BI) empat lapis yang mengintegrasikan analitika Big Data dengan pemodelan prediksi menggunakan deep learning. Memanfaatkan dataset berfrekuensi tinggi selama lima tahun yang terdiri dari 43.786 data harga historis Bitcoin (BTC/USDT) per jam dari API Binance, penelitian ini memenuhi karakteristik kerangka Big Data. Sebanyak 15 indikator teknikal diekstraksi sebagai fitur input dan dievaluasi tingkat kepentingannya menggunakan SHapley Additive exPlanations (SHAP). Algoritma deep learning berbasis sekuensial, yakni Long Short-Term Memory (LSTM) dan Gated Recurrent Units (GRU), dibandingkan dengan algoritma XGBoost sebagai model baseline (acuan). Arsitektur model dioptimasi menggunakan metode Grid Search untuk menemukan kombinasi parameter terbaik (termasuk penggunaan dua hidden layers, 50 node, dan fungsi Dropout 20%). Pengujian Walk-Forward Validation menunjukkan temuan komparatif yang kritis: Model GRU terbukti menjadi arsitektur yang paling presisi dengan tingkat kesalahan terendah (RMSE: 0.1058), mengungguli LSTM (RMSE: 0.1145) dan XGBoost (RMSE: 0.1524). Dibalik itu, LSTM mampu memprediksi arah pergerakan pasar (Win Rate) lebih baik di angka 72.3% dibandingkan GRU (69.8%) dan XGBoost (58.4%). Dengan menerjemahkan luaran prediksi ini ke dalam metrik finansial pada antarmuka BI Dashboard, model ini berhasil mengkalkulasikan batas paparan risiko korporasi seperti Sharpe Ratio (LSTM: 1.45) dan Value at Risk (VaR 95%: -2.34%). Proposal penelitian ini diharapkan menghasilkan suatu sistem operasional yang reliabel bagi para manajer investasi untuk memitigasi risiko pasar cryptocurrency menggunakan akurasi kecerdasan buatan.
        <br><br>
        <strong>Kata Kunci</strong> Business Intelligence, Prediksi Cryptocurrency, Big Data Analytics, Deep Learning, XGBoost, LSTM, GRU, Informatika Finansial, Bitcoin.
    </div>

    <h1>BAB I: PENDAHULUAN</h1>
    <p>Digitalisasi ekonomi global dalam satu dekade terakhir telah menjadikan aset kriptokhususnya Bitcoin (BTC)sebagai instrumen kelas aset yang sangat dominan di sektor finansial. Namun, karakteristik pasar mata uang kripto yang beroperasi 24 jam penuh tanpa henti, bersifat sangat terdesentralisasi, serta rentan terhadap perubahan sentimen makroekonomi, menyebabkan pergerakannya sangat ekstrem dan penuh ketidakpastian. Kondisi volatilitas ekstrim inilah yang menjadikan prediksi harga Bitcoin sebagai salah satu tantangan komputasi paling rumit di ranah pemodelan finansial masa depan [1], [2], [3]. Sistem prediksi yang menggunakan statistik tradisional (seperti model ARIMA) seringkali mensyaratkan kondisi pasar yang selalu stabil (stasioner). Hal ini terbukti mengalami kegagalan fungsi ketika diterapkan untuk menganalisis data transaksi volume tinggi yang saling terdistorsi oleh noise frekuensi [4], [5]. Model finansial klasik tersebut tidak mampu menangkap pola perubahan arah harga (*non-linear temporal dependencies*) yang tersembunyi di dalam laju pergerakan pasar masa kini [6].</p>
    <p>Oleh karena itu, para ahli riset data saat ini telah mengalihkan fokus dari perhitungan regresi statistik murni ke arah penerapan arsitektur Kecerdasan Buatan (Artificial Intelligence) berbasis Jaringan Saraf Tiruan (Neural Networks) yang terintegrasi dengan kerangka kerja Big Data. Penggunaan deep learning memampukan sistem untuk mempelajari rekam jejak puluhan ribu transaksi secara mandiri, sehingga pola-pola pergerakan harga yang sangat rumit dan saling tumpang tindih dapat dipetakan secara matematis tanpa campur tangan dan paksaan asumsi linier dari manusia.</p>
    <p>Di satu sisi, mayoritas publikasi literatur mengenai penerapan Jaringan Saraf Tiruan pada prediksi harga sekadar berfokus pada hasil akhir berupa tebakan angka (misalnya memperkirakan bahwa harga esok hari adalah \.000). Namun di sisi lain, sangat jarang ditemukan penelitian yang merangkai prediksi angka tersebut menjadi sebuah Kerangka *Business Intelligence* komprehensif (End-to-End). Eksekutif perusahaan atau penasihat investasi tidak bisa mengambil keputusan hanya bermodalkan angka prediksi dari komputer. Nilai keluaran *Deep Learning* tersebut harus diterjemahkan (ditranslasikan) terlebih dahulu ke dalam indikator fungsi bisnis nyata; seperti evaluasi ketahanan rasio risiko (Sharpe Ratio), estimasi target persentase keuntungan (Win Rate), serta peringatan batas kerugian terburuk (Value at Risk).</p>
    <p>Untuk mengisi kesenjangan antara riset akademis yang sempit dan kebutuhan operasional industri tersebut, Proposal Tesis ini merancang sebuah sistem holistik bernama "BI-ML Framework" (Kerangka Intelijen Bisnis & Pembelajaran Mesin). Tujuan utama disertasi adalah untuk membandingkan secara komprehensif performa peramalan harga dari arsitektur Deep Learning berbasis memori gerbang waktu, yakni *Long Short-Term Memory (LSTM)* dan *Gated Recurrent Unit (GRU)*, serta menyandingkannya dengan rujukan model tabular populer *Extreme Gradient Boosting (XGBoost)*. Hasil analisis model-model tersebut kemudian ditarik menuju tahap perancangan visualisasi keputusan (Dashboard Sistem Pendukung Keputusan) agar dapat diadopsi secara riil di dunia manajerial finansial.</p>

    <h1>BAB II: KAJIAN TEORITIS DAN TINJAUAN PUSTAKA</h1>
    <h2>A. Keterbatasan Metodologi Analisis Tradisional</h2>
    <p>Dalam tataran literatur teori finansial masa lampau, pasar investasi seringkali diasumsikan selalu berada pada kondisi seimbang (*Efficient Market Hypothesis/EMH*) [7]. Namun, aset seperti cryptocurrency telah terbukti seringkali mengalami kejadian penyimpangan asimetris atau efek pengulangan tren jangka menengah yang tidak masuk akal (*Long-Memory effects*). Hal inilah yang menyebabkan gagalnya indikator-indikator regresi sekuensial sederhana di dunia modern. Menyikapi kebuntuan statistik, metode berbasis *ensemble machine learning* (pembelajaran kombinasi mesin majemuk) seperti XGBoost kerap dijadikan standar dasar (*baseline estimator*) dalam riset kontemporer karena daya tahannya yang lebih baik terhadap anomali data ketimbang rumusan statistik konvensional [8].</p>
    
    <h2>B. Perkembangan Arsitektur Saraf Deep Learning Berbasis Memori</h2>
    <p>Pendekatan Jaringan Saraf Tiruan konvensional memiliki titik lemah yang fatal saat menangani deret waktu finansial yang sangat panjang, yakni fenomena hilangnya ingatan mesin dalam memproses data (*Vanishing Gradient Problem*). Untuk menangani hal tersebut, Hochreiter dan Schmidhuber [9] merevolusi pemodelan dengan menciptakan arsitektur *Long Short-Term Memory* (LSTM). LSTM memiliki kemampuan unik di mana ia dibekali sub-gerbang logika independen yang bertugas menyeleksi memori mana yang patut diingat untuk tren masa depan, dan mana yang patut dilupakan (*Information Retention Mechanism*). Selanjutnya, Cho dkk [10] merampingkan kompleksitas arsitektur LSTM tersebut dan menyempurnakannya ke dalam bentuk *Gated Recurrent Unit* (GRU) yang menjanjikan kecepatan pelatihan (komputasi) yang jauh lebih cepat tanpa mengorbankan akurasi pola. Penerapan dari kedua algoritma prediktif top-tier dunia ini telah terbukti sangat dominan [11], [12], dan penerapannya yang dilebur bersama infrastruktur korporasi BI (*Business Intelligence*) tengah menjadi tonggak inovasi yang diteliti lebih mendalam [13], [14].</p>

    <h1>BAB III: ARSITEKTUR SISTEM DAN METODOLOGI BI FRAMEWORK</h1>
    <p>Agar penelitian ini dapat diuji ulang secara empiris dan akurat (*deterministic reproducibility*), skema pemrosesan Big Data dirancang ketat ke dalam struktur siklus empat lapisan (*4-Layer BI Framework*). Pendekatan lapis per lapis menjembatani pergerakan transisi dari pengolahan miliaran kode angka digital mentah hingga ia muncul sebagai grafik rekomendasi ramah pengguna yang siap dibaca oleh analis investasi manusia [15], [16]. Proses kerangka ini sangat lazim diaplikasikan pada proyeksi komputasi tersebar [17], [18].</p>

    <h2>A. Lapisan 1: Pangkalan Ingestion Data (Source Hub)</h2>
    <p>Prosedur pencarian data dimulai secara real-time dengan menghubungkan skrip modul *Python* menuju Endpoint *Binance Spot API* secara resmi. Data ekstraksi dikumpulkan sepanjang jendela pergerakan 5 tahun berturut-turut (meliputi periode bulan Maret 2021 hingga periode target simulasi 2026). Sebanyak *43.786 baris interval waktu (per-jam)* berhasil terkumpul dengan lengkap yang menampung poin pergerakan harga Buka, Tertinggi, Terendah, dan Tutup (OHLC). Besarnya akumulasi baris ini memastikan bahwa riset ini lolos mematuhi rukun fundamental *Volume* dan *Velocity* di dalam parameter kerangka Big Data [1], [19].</p>

    <h2>B. Lapisan 2: Rekayasa Engine ETL & Normalisasi Matematika</h2>
    <p>Demi menjaga rukun kejujuran integritas asal data (*Veracity*), data mentah ditransisikan perlahan ke tahap *Extraction, Transformation, and Load (ETL)*. Seluruh cacat angka bolong (*missing values* akibat keterlambatan respon server Binance) ditambal matematis menggunakan strategi *Linear Polynomial Interpolation*. Kemudian, karena input nilai harga kripto merentang luas puluhan ribu nominal mata uang dolar, algoritma pendeteksi di lapisan Neural Networks beresiko mengalami ledakan hitungan *gradient*. Antisipasi diaktifkan dengan melakukan pemampatan batas angka (*Min-Max Normalization*) guna mengecilkan persentase rasio matematis di rentang komputasi skala [0,1]:</p>
    
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}} \eqno{(1)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>

    <div class="figure">
        <img src="../04_Visualizations/btc_5year_trend.png" alt="Bitcoin 5-Year High Frequency Trend">
        <div class="figure-caption"><strong>Gambar 1.</strong> Lintasan Pergerakan Harga Aktual dan Volume Target Dataset Prediksi mencakup 43.786 Interval Observasi Jam (2021-2026).</div>
    </div>

    <h2>C. Lapisan 3: Komputasi Prediktivitas dan Operasional Node Tersembunyi</h2>
    <p>Sebagai instrumen kepatuhan kerangka hukum penyesuaian (*Variety* Big Data), data OHLC dimultiplikasi secara formula menjadi total lima belas (15) varian fitur teknikal pelacakan pasar. Seluruh ragam data tersebut kemudian ditugaskan masuk dalam barisan antrean kompilasi mesin pemroses grafis berakselerasi tinggi berbasis inti CUDA (*Hardware GPU Acceleration*). Langkah struktural ini sangat krusial mengingat pelatihan arsitektur Neural Network membutuhkan eksekusi simulasi perulangan waktu berurutan (*Epochs*) dalam matriks dimensi logaritma yang berkapasitas daya sangat besar.</p>

    <h2>D. Lapisan 4: BI Analytics & Platform Keputusan Bisnis</h2>
    <p>Tahapan puncak operasional ini berfungsi menerjemahkan nilai kuantitatif dari selisih simpangan prediksi (RMSE). Modul penyunting akan mengubah perhitungan murni matematis residu tersebut menjadi parameter dasbor eksekutif *Decision Support System* yang disuplai di kehidupan nyataseperti kalkulasi persentase probabilitas arah (*Win Rate*), simulasi keamanan modal korporasi (*Sharpe Ratio*), serta peringatan batasan risiko ambang batas tertinggi mitigasi nilai jatuh melalui parameter *Value at Risk* (VaR). Rangkuman desain aliran komprehensif lapisan kerangka ini diuraikan dengan presisi di visualisasi Gambar 4.</p>'''


new_text_2 = '''    <h1>REKAYASA PARAMETER (FEATURE ENGINEERING) & PERMUTASI SHAP</h1>
    <p>Penginputan murni dari titik harga historis secara langsung ke dalam jaringan logaritma sering kali membatasi ruang cakupan performa *deep learning*. Untuk memecahkan isolasi nilai nominal tersebut, dilakukan *Feature Engineering* (Rekayasa Fitur). Nilai harga mentah diproyeksikan dan dibelah menjadi lima (5) sub-kategori utama (seperti yang dijabarkan paralel pada Tabel III). Proses transformasi ini menciptakan kekayaan wawasan klasifikasi untuk pelacakan mesin cerdas (*Variety Principle*).</p>

    <div class="table-container">
        <div class="table-title">Tabel III. Parameter Pelacakan Lima Belas Fitur Tambahan (Prinsip Keberagaman Data)</div>
        <table>
            <tr><th>No</th><th>Fitur Teknikal / Parameter Analitik</th><th>Fungsi Observasi</th><th>Basis Rumusan Matematika</th></tr>
            <tr><td>1-5</td><td>Open, High, Low, Close, Volume</td><td>Penentuan Target Base (Raw)</td><td>\(O_t, H_t, L_t, P_t, V_t\)</td></tr>
            <tr><td>6-7</td><td>Moving Average-7, MA-21</td><td>Estimasi Titik Rata-rata Tren</td><td>\(avg(P_t, n)\)</td></tr>
            <tr><td>8</td><td>Relative Strength Index (RSI)</td><td>Deteksi Perputaran Momentum</td><td>Persamaan. (3)</td></tr>
            <tr><td>9-10</td><td>MACD & Batas Sinyal MACD</td><td>Kalkulasi Akselerasi Tren</td><td>Persamaan. (2)</td></tr>
            <tr><td>11-13</td><td>Bollinger Upper, Lower, Width</td><td>Dimensi Kurungan Lebar Volatilitas</td><td>\(MA_{20} \pm 2\sigma\) dan Persamaan. (4)</td></tr>
            <tr><td>14</td><td>Logarithm Returns</td><td>Harmonisasi Nilai Stasioner</td><td>\(ln(P_t/P_{t-1})\)</td></tr>
            <tr><td>15</td><td>Rolling Volatility 24-Jam</td><td>Kuantifikasi Titik Risiko Simpangan</td><td>\(\sigma_{24h}\)</td></tr>
        </table>
    </div>

    <h2>A. Perhitungan Matematis Tren Linear (MACD & RSI)</h2>
    <p>Akselerasi cepat mengenai percepatan fluktuasi (*trend reversals*) difasilitasi rumusan hitung eksponensial dalam rumusan *Moving Average Convergence Divergence* (MACD):</p>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports MACD = EMA_{12}(P) - EMA_{26}(P) \eqno{(2)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>
    <p>Sedangkan untuk merumuskan klasifikasi titik jenuh di mana investasi dirasa sudah terlalu mahal (Overbought) atau terlalu murah (Oversold), indeks diukur ke dalam limit paksa 0 hingga 100 dengan rasio *Relative Strength Index* (RSI):</p>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports RSI = 100 - \left(\frac{100}{1 + \frac{EMA(\text{Gain})}{EMA(\text{Loss})}}\right) \eqno{(3)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>

    <h2>B. Stabilisator Siklus Stasioner Varians (Volatilitas Terukur)</h2>
    <p>Model neural acapkali kewalahan membaca guncangan tak wajar. Pembatasan lonjakan fluktuasi menggunakan perhitungan Lebar Logaritmik pita deviasi menempatkan perlindungan terhadap batas error berlebih (mempertahankan stasioneritas):</p>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports \sigma_t = \sqrt{\frac{1}{n} \sum (\Delta P_i - \bar{P})^2} \eqno{(4)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>

    <h2>C. Analitika Transparansi Kontribusi Fitur (Koefisien SHAP)</h2>
    <p>Penggunaan ke-15 deret fitur baru tersebut berpotensi menjebak model ke dalam beban bias (*overloading*). Untuk merangkai *Explainable AI* (Sistem AI yang dapat dijelaskan pola kerjanya), kontribusi bobot metrik tidak dilakukan lewat uji coba tebakan bebas murni, melainkan diuji probabilitasnya menggunakan instrumen <em>SHapley Additive exPlanations (SHAP)</em>. Evaluasi mekanis modul SHAP memastikan dan menjabarkan transparansi; seperti mengungkapkan bahwa sinyal <em>MACD</em> atau deviasi <em>Rolling Volatility</em> memberikan porsi bobot paling relevan selama tahapan prediksi algoritmik berjalan dibandingkan fitur dasar lainnya [20], [21], [22].</p>

    <h1>METODOLOGI PELATIHAN DEEP ARCHITECTURE (HYPERPARAMETER)</h1>
    <p>Risiko terbesar dalam memprediksi komputasi waktu runtut adalah fenomena <em>Data-Leaks</em> (yakni bocornya data pengujian dari kurun waktu masa depan yang tertaut tanpa sengaja ke data pelatihan lampau). Penghancuran celah kesalahan ini dieksekusi menggunakan modul sinkronisasi validasi berantai khusus: <strong>Walk-Forward Validation</strong>. Modus pengujian tumpang-tindih (*sliding window*) ini memastikan model dinilai kemampuannya pada batasan sisa rentang absolut 168 jam ke depan (sepekan), murni menelusuri data yang benar-benar belum pernah terekspos sebelumnya (*Look-ahead Mismatch Prevention*).</p>

    <h2>A. Optimalisasi Kalibrasi Variabel Jaringan (Grid Search)</h2>
    <p>Untuk menciptakan tatanan persaingan perbandingan model yang seimbang, diperlukan pencarian pengaturan titik parameter optimal <em>(Hyperparameters tuning)</em>. Evaluasi pencarian struktural (dengan menjauhi perangkap jebakan *over-fitting*) mengungkap efisiensi arsitektur yang diratakan pada susunan: <strong>2 Lapisan Node Jaringan Tersembunyi (Hidden Layers) paralel berkapasitas ruang simpan 50 Neuron per lapis.</strong> Penyelarasan komputasi penambahan tingkat nilai adaptif mengerahkan pengoptimalisasi <em>Stochastic Gradient Descent algoritma 'Adam'</em> yang beroperasi stabil pada laju penyerapan (*Learning Rate*) konstan di 0.001 [23]. Sistem turut menyematkan barikade perontok tegangan jaring (*Dropout Rate*) di poin 20%, memastikan model memodifikasi dan memotong simpul secara acak untuk melatih kepekaan selama 10 gelombang pelacakan penuh (*Epochs*) [24], [25].</p>

    <h2>B. Penguncian Ambang Batas Logaritma Rujukan (Baseline XGBoost)</h2>
    <p>Difungsikan sebagai metode rujukan statis komparatif, algoritma susunan <em>Extreme Gradient Boosting (XGBoost)</em> ditempatkan demi membuktikan keunggulan metodologi AI sekuensial. Mesin ini didikte untuk memperhitungkan gabungan kesimpulan lebih dari 100 estimasi pohon probabilitas bercabang <em>(Decision Trees)</em>. Algoritma dasar ini menjamin pembaruan nilai akurasi berulang untuk menderivikasi kesalahan residu murni, kendati tidak dibekali unit ingatan memori pergerakan waktu di masa lalu layaknya topologi LSTM dan GRU.</p>

    <h2>C. Anatomi Gerbang Long Short-Term Memory (LSTM)</h2>
    <p>Superioritas mendasar arsitektur rekayasa memori matriks kontrol LSTM mengandalkan struktur penjagaan informasi berantai di modul logaritma gerbangnya *(*Gating Mechanics*)*. Pendelegasian instruksi penolakan memori jangka-panjang disalurkan melalui persilangan fungsi Gerbang Pembuang Jejak <em>(Forget Gate - \(f_t\))</em> dan Pemasukan Penyerapan Baru <em>(Input Gate - \(i_t\))</em>:</p>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \eqno{(5)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) \eqno{(6)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>
    <p>Logika fungsi penahanan blok matematis ini menjamin memori rentang temporal harga tren makro dapat diteruskan sepanjang ratusan perulangan baris ke depan, sambil tetap mempertahankan elastisitas untuk mengabaikan gangguan transaksional (*market-noise*) sesaat di detik tertentu.</p>

    <h2>D. Efisiensi Reduksi Topologi Gated Recurrent Unit (GRU)</h2>
    <p>Hadir sebagai penyempurnaan evaluatif arsitektur ganda klasik LSTM yang konvensional tebal dan rakus daya komputator, skema evolusi arsitektur GRU menyatukan sekat penyaring parameternya. Peleburan tingkat memori masa lalu direngkuh dan diaktifkan melalui pintu hibrida <em>(Update Gate - \(z_t\))</em> yang merangkai seketika kesatuan proses parameter alokasi temporal masa lalu:</p>
    <div class="equation">
        e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z) \eqno{(7)} e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports
    </div>
    <p>Aglomerasi dari *Update-Gate* tersebut berdampak masif menekan rumitnya siklus alur *Backpropagation through Time*. Mengorbankan ruang dimensi kompleks yang tidak terlalu berpengaruh, langkah *training* iterasi model sekunsial varian algoritma ini terbukti menjadi jauh lebih gesit, ringkas, dan menghemat waktu kalkulasi tanpa perlu melebarkan tingkat kerugian rasio keakuratan *forecast* secara mutlak.</p>'''

with io.open('Proposal_Tesis_Bitcoin_BI_Indo.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Splitting securely matching known stable HTML structure bounds
start_1 = text.find('<div class="abstract-section">')
end_1 = text.find('<div class="svg-figure">')

start_2 = text.find('<h1>REKAYASA PARAMETER')
if start_2 == -1: 
    start_2 = text.find('<h1>REKAYASA PARAMETER FEATURE ENGINEERING')
end_2 = text.find('<h2 style="text-align:center; text-transform:uppercase;">Daftar Pustaka')

final_text = text[:start_1] + new_text_1 + '\n    ' + text[end_1:start_2] + new_text_2 + '\n\n    ' + text[end_2:]

with io.open('Proposal_Tesis_Bitcoin_BI_Indo.html', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Done string replacement accurately!")
