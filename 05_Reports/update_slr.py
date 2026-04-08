import re
import os

file_path_1 = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\Proposal_Tesis_Bitcoin_BI_Indo.html'

file_path_2 = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

new_tbody = '''            <tbody>
                <tr>
                    <td>1</td>
                    <td><em>Forecasting and trading cryptocurrencies with machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Sebastião &amp; Godinho (2021) [4]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Perbandingan model <em>Machine Learning</em> (Random Forest, SVM, Regresi Linier) untuk memprediksi arah pergerakan tiga mata uang kripto utama.<br><strong>Algoritma:</strong> Random Forest, SVM, Logistik Regresi.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Random Forest secara konsisten menghasilkan rasio <em>Directional Accuracy</em> tertinggi, mengungguli strategi <em>Buy-and-Hold</em> konvensional selama periode pengujian di berbagai rezim pasar kriptografis.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Model yang dihasilkan bersifat absolut <em>Black-Box</em> tanpa ada lapisan transparansi (XAI). Selain itu, tidak mengintegrasikan sistem prediksi dengan metrik manajemen risiko praktis perbankan (VaR, Sharpe Ratio) bagi pengguna tingkat manajerial.</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><em>Applications of deep learning in stock market prediction: Recent progress</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Jiang (2021) [21]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Tinjauan literatur analitis mengenai implementasi masif model <em>Deep Learning</em> pada perburuan volatilitas pasar sekuritas dan komoditas digital kripto.<br><strong>Algoritma:</strong> Skema JST, RNN, LSTM, CNN.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Arsitektur gerbang memori LSTM tervalidasi secara akademis sebagai model dominan dalam memroses sekuensi runtutan harga berkat proteksi ingatan jangka panjang melintasi waktu (<em>Long-Memory effects</em>), mengatasi cacat fatal hilangnya gradien pada RNN.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Beban berat kompleksitas memori selLSTM memperlambat laju iterasi komputasi kompilatif harian. Tidak dieksplorasi pula perbandingan simetris variasi arsitekturnya menghadapi saudara efisiennya, algoritma GRU, di medan laga pasar berfrekuensi ketat.</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><em>Short-term bitcoin market prediction via machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Jaquart dkk. (2021) [8]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Pemodelan prediksi nilai Bitcoin frekuensi interval mikro per jam yang mengombinasikan pelacakan rasio teknikal fundamental dengan arus sentimen eksternal.<br><strong>Algoritma:</strong> Model Multidiskriminan, <em>Ensemble Learning</em> Regresi.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Observasi per-24 jam menyingkap rentang momentum harga yang sangat asimetris. Model arsitektur ensembel membuktikan efisiensinya menekan <em>Root Mean Square Error</em> (RMSE) meredam lonjakan fluktuasi tanpa terjebak linieritas usang.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Riset semata usai di garis akhir perhitungan kalkulus galat. Nihil ada jembatan implementasi praktikal memproyeksikan rentetan probabilitas dingin tersebut memandu aksi taktis terpusat seorang analis (ketidakadaan <em>Decision Support System</em>).</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><em>Prediction of cryptocurrency returns using machine learning</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Akyildirim dkk. (2021) [29]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Kalkulasi prediktif kelas ekstrim pencilan volatilitas mata uang harian menyortir margin tingkat imbal hasil acak yang dimonitor sepanjang gelombang pasar liar.<br><strong>Algoritma:</strong> XGBoost (<em>Extreme Gradient Boosting</em>).</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Arsitektur pendorong pohon (XGBoost) meredam ledakan kebisingan harga berkat mekanisme dinamisnya menyaring kelonggaran variabel dan memberikan sanksi tegas pembatasan kerugian, memenangkan presisi nilai ketimbang logistik tradisional.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Meskipun ketepatan perhitungannya nyaris tidak tercela, formulanya mengunci tertutup akses nalar manusia di dalam logika keputusannya. Tidak ada penyertaan struktur XAI pelacak sebab mengapa satu koefisien diutamakan ketimbang atribut lain.</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><em>How do economic policy uncertainty and geopolitical risk drive Bitcoin volatility?</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Ben Nouir dkk. (2023) [6]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Mengkaji determinan rambatan efek kegelisahan makro atas lonjakan risiko ketegangan geopolitik lintas negara dan dampaknya ke impulsivitas gejolak Bitcoin.<br><strong>Algoritma:</strong> Regresi Ekonometrika dan Analisis Deret Spasial Klasik.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Kejut berita invasi maupun kebijakan geopolitik asimetris memicu gelombang aksi jual-beli reaktif massal mementahkan postulat wacana Ekuilibrium Teori Pasar Efisien. Bitcoin resmi merespons laiknya barometer tegang skala internasional terkini.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Terpenjara di dalam metodologi kausal uji t statistik konvensional ekonometrika statis. Eksperimen sama sekali tidak meretas kemampuan pemrosesan multidimensi berdimensi tinggi dari teknologi kognitif saraf <em>Deep Learning</em> kekinian.</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><em>Forecasting cryptocurrency prices using LSTM, GRU, and bi-directional LSTM</em><br><span style="color: #f39c12; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q2)</span></td>
                    <td>Seabe dkk. (2023) [13]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Eksperimen murni adu kehandalan absolut dari trio dinasti komputasional berbasis riwayat (gerbang saraf) spesifik dalam menaklukan tebing Bitcoin interval harian.<br><strong>Algoritma:</strong> Saraf Tiruan LSTM murni, Modifikasi Sel GRU, Bi-LSTM ganda.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Terbantahkannya hegemoni kompleksitas LSTM. Struktur gerbang penyaring ringkas inovasi GRU sukses meliuk melewati lautan iterasi logaritma komputasi memperkecil simpangan eror secara agresif mendepak durasi lamanya waktu perhitungan saudaranya.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Pertarungan mandek merekonstruksi pemecahan deret kesalahan numerik belaka persentase tanpa orientasi finansial (MSE/MAE). Pembongkaran fenomena imbal hasil tukar antara Presisi Ketepatan Angka vs Akurasi Taruhan Arah nihil didiskusikan sistem pembacaan.</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><em>Explainable artificial intelligence modeling to forecast bitcoin prices</em><br><span style="color: #e53935; font-size: 0.9em; font-weight: bold;">(Terindeks: Scopus Q1)</span></td>
                    <td>Goodell dkk. (2023) [16]</td>
                    <td style="text-align: justify;"><strong>Objek:</strong> Penetapan lensa pengungkap kerahasiaan pembobotan matematis jaringan (transparansi algoritma) demi menerjemahkan kausalitas prioritas di tengah gelapnya hutan pohon keputusan probabilitas prediksi deret waktu kripto.<br><strong>Algoritma:</strong> Metode <em>Explainable AI</em> SHAP.</td>
                    <td style="text-align: justify;"><strong>Temuan Utama:</strong> Aplikasi distribusi sumbangsih agregat logika permainan nilai kooperasi SHAP terbukti membedah rasio prioritas setiap fitur indikator teknikal (RSI, Volatilitas Per Jam). Menyajikan rasionalitas ilmiah gamblang pada <em>Output Deep Learning</em> tanpa hambatan distorsi.</td>
                    <td style="text-align: justify;"><strong>Keterbatasan:</strong> Kerangka XAI terhitung hanya diemban statis pada model tunggal. Potensi pelacakan transendental analitika pembedahannya belum ditarik keluar menjadi perantara pihak ketiga penengah di dalam adu tinju kapabilitas arsitektur komparatif ekstrim (LSTM &amp; GRU).</td>
                </tr>
            </tbody>'''

pattern = re.compile(r'<tbody>.*?</tbody>', re.DOTALL)

for file_path in [file_path_1, file_path_2]:
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
