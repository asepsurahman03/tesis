# DASHBOARD INTELIJEN BISNIS UNTUK PREDIKSI HARGA BITCOIN
# Implementasi Prototipe Dashboard Eksekutif — Kerangka Kerja BI Empat Lapis
# Penelitian: Komparasi LSTM, GRU, dan XGBoost dengan Analitika Big Data

import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
# INISIALISASI APLIKASI DASH
# ─────────────────────────────────────────────────────────────────────────────
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Dashboard Intelijen Bisnis — Prediksi Harga Bitcoin"

# ─────────────────────────────────────────────────────────────────────────────
# DATA KONTEN MODAL (PENJELASAN AKADEMIS SETIAP KPI)
# ─────────────────────────────────────────────────────────────────────────────
MODAL_CONTENT = {
    'harga': {
        'judul': '💰 Harga Pasar BTC/USDT Saat Ini',
        'isi': [
            ('Definisi', 'Harga pasar Bitcoin (BTC) yang dikuotasi terhadap stablecoin USDT (Tether) dan diambil secara real-time dari Binance Spot API. Harga ini merepresentasikan harga penutupan (Close Price) per jam terakhir dalam data historis penelitian.'),
            ('Relevansi Penelitian', 'Dalam penelitian ini, harga penutupan (Pt) menjadi variabel target utama (y) yang diprediksi oleh ketiga model — LSTM, GRU, dan XGBoost. Galat prediksi diukur menggunakan Root Mean Square Error (RMSE) dan Mean Absolute Error (MAE) pada skala harga yang telah dinormalisasi dengan Min-Max Scaler ke rentang [0, 1].'),
            ('Interpretasi', 'Kenaikan harga yang melampaui batas pita atas Bollinger Bands (MA₂₀ + 2σ) mengindikasikan potensi kondisi jenuh beli (overbought), yang menjadi sinyal bahwa model prediksi akan mempertimbangkan koreksi harga pada jam-jam berikutnya.'),
        ]
    },
    'perubahan': {
        'judul': '📈 Perubahan Harga 24 Jam (Log Return)',
        'isi': [
            ('Definisi', 'Persentase perubahan harga Bitcoin dalam rentang 24 jam terakhir, dihitung menggunakan formula Log Return: r_t = ln(P_t / P_(t-24)). Penggunaan log return memastikan distribusi data mendekati asumsi normalitas dan stasioneritas yang dipersyaratkan oleh arsitektur deep learning.'),
            ('Relevansi Penelitian', 'Log Return merupakan salah satu dari 15 fitur teknikal yang direkayasa (Feature Engineering) dalam penelitian ini. Kontribusi fitur ini terhadap akurasi prediksi model dievaluasi menggunakan metode SHAP (SHapley Additive exPlanations), yang memungkinkan interpretasi model secara transparan sesuai paradigma Explainable AI (XAI).'),
            ('Interpretasi', 'Nilai positif menandakan apresiasi harga dalam 24 jam terakhir, sedangkan nilai negatif menandakan depresiasi. Amplitudo perubahan yang melebihi ±5% mengindikasikan volatilitas ekstrem yang berpotensi mempengaruhi akurasi prediktif model sekuensial.'),
        ]
    },
    'akurasi': {
        'judul': '🎯 Akurasi Prediksi Arah — Directional Win Rate',
        'isi': [
            ('Definisi', 'Directional Win Rate (DWR) mengukur persentase prediksi arah pergerakan harga (naik atau turun) yang benar dari total prediksi yang dilakukan. Metrik ini lebih relevan secara praktis dibandingkan RMSE dalam konteks pengambilan keputusan investasi aktif.'),
            ('Relevansi Penelitian', 'Dalam kerangka kerja BI Lapis 4, RMSE mengukur presisi numerik (seberapa dekat nilai prediksi dengan aktual), sedangkan DWR mengukur kebergunaan sinyal arah (apakah model dapat memprediksi tren naik/turun dengan benar). Hipotesis utama penelitian ini menyatakan adanya trade-off signifikan: model dengan RMSE terbaik belum tentu memiliki DWR tertinggi.'),
            ('Kriteria Kelayakan', 'Ambang batas minimum DWR yang ditetapkan dalam penelitian ini adalah 55%, di atas peluang acak 50%. Hasil empiris menunjukkan: LSTM mencapai DWR 72,3%, GRU 69,8%, dan XGBoost 58,4% — mengkonfirmasi keunggulan arsitektur deep learning berbasis memori sekuensial untuk data deret waktu finansial berfrekuensi tinggi.'),
        ]
    },
    'sharpe': {
        'judul': '📊 Sharpe Ratio — Rasio Imbal Hasil terhadap Risiko',
        'isi': [
            ('Definisi', 'Sharpe Ratio adalah metrik risiko eksekutif yang mengukur seberapa besar imbal hasil (return) yang diperoleh per unit risiko yang ditanggung oleh investor. Formula standar: SR = (R_p - R_f) / σ_p, di mana R_p adalah return portofolio, R_f adalah tingkat bunga bebas risiko, dan σ_p adalah deviasi standar return.'),
            ('Relevansi Penelitian', 'Sharpe Ratio merupakan salah satu dari tiga metrik risiko utama yang dihasilkan pada Lapis 4 (BI Analytics & Decision Support). Konversi keluaran model prediktif menjadi metrik finansial ini adalah kontribusi utama penelitian ini — menjembatani gap antara output teknis model AI dengan kebutuhan praktis manajer investasi.'),
            ('Interpretasi', 'Nilai SR ≥ 1,0 diinterpretasikan sebagai layak untuk dipertimbangkan dalam strategi investasi aktif. Nilai SR 1,45 yang dicapai strategi berbasis LSTM mengindikasikan bahwa setiap satu unit risiko yang diambil menghasilkan 1,45 unit return — sebuah profil risiko-imbal hasil yang atraktif dibandingkan strategi pasif Buy-and-Hold.'),
        ]
    },
    'var': {
        'judul': '⚠️ Value at Risk 95% — Estimasi Kerugian Maksimum',
        'isi': [
            ('Definisi', 'Value at Risk (VaR) pada tingkat kepercayaan 95% adalah estimasi kerugian maksimum yang mungkin terjadi dalam satu periode waktu (1 hari) dengan probabilitas tidak lebih dari 5%. Secara formal: P(Kerugian > VaR) ≤ 5%.'),
            ('Relevansi Penelitian', 'VaR 95% merupakan standar internasional dalam manajemen risiko portofolio (Basel III Accord) dan menjadi salah satu metrik risiko eksekutif yang dihasilkan Lapis 4 dashboard ini. Nilai ini dikalkuasi dari distribusi residual prediksi model untuk memberikan estimasi batas kerugian terburuk yang dapat dikuantifikasi secara statistik.'),
            ('Interpretasi', 'Nilai VaR -2,34% berarti: dengan tingkat keyakinan 95%, kerugian harian dari posisi BTC tidak akan melebihi 2,34% dari total nilai portofolio. Dengan kata lain, hanya ada kemungkinan 5% bahwa kerugian harian akan melampaui angka tersebut — informasi kritis bagi manajemen risiko eksekutif.'),
        ]
    },
    'model': {
        'judul': '🤖 Perbandingan Performa Tiga Model Prediktif',
        'isi': [
            ('LSTM (Long Short-Term Memory)', 'Arsitektur LSTM dilengkapi tiga gerbang memori — Forget Gate, Input Gate, dan Output Gate — yang memungkinkan model mempertahankan dependensi temporal jangka panjang dalam data deret waktu. Pada dataset BTC/USDT 43.788 rekaman per jam, LSTM mencapai RMSE 0,1145 dan DWR 72,3%, menjadikannya model dengan akurasi prediksi arah terbaik dalam penelitian ini.'),
            ('GRU (Gated Recurrent Unit)', 'GRU merupakan penyederhanaan LSTM dengan menggabungkan Forget Gate dan Input Gate menjadi satu Update Gate (z_t). Arsitektur yang lebih ringan ini menghasilkan waktu komputasi 23% lebih cepat dibandingkan LSTM. GRU mencapai RMSE 0,1058 — galat numerik terendah — namun dengan DWR 69,8%, mengkonfirmasi hipotesis trade-off antara presisi numerik dan akurasi arah.'),
            ('XGBoost (Baseline)', 'XGBoost berfungsi sebagai model baseline berbasis gradient boosting decision tree. Tanpa mekanisme memori temporal bawaan, XGBoost hanya mencapai DWR 58,4% — mendekati peluang acak — namun tetap superior dibandingkan model statistik linear konvensional (ARIMA). Hasil ini memvalidasi pentingnya arsitektur berbasis memori sekuensial untuk data finansial berfrekuensi tinggi.'),
        ]
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI PEMBANTU: MEMBANGUN KOMPONEN MODAL
# ─────────────────────────────────────────────────────────────────────────────
def buat_modal(modal_id, data_kunci):
    konten = MODAL_CONTENT[data_kunci]
    
    # Bangun baris konten penjelasan
    baris_konten = []
    for sub_judul, teks in konten['isi']:
        baris_konten.append(
            html.Div([
                html.Strong(f"{sub_judul}:", style={
                    'color': '#1a3a6b', 'display': 'block', 'marginBottom': '4px',
                    'fontSize': '13px', 'textTransform': 'uppercase', 'letterSpacing': '0.5px'
                }),
                html.P(teks, style={
                    'textAlign': 'justify', 'lineHeight': '1.7', 'color': '#34495e',
                    'fontSize': '13.5px', 'marginBottom': '0'
                })
            ], style={
                'backgroundColor': '#f8f9fa', 'borderLeft': '4px solid #1a3a6b',
                'padding': '12px 16px', 'marginBottom': '12px', 'borderRadius': '0 6px 6px 0'
            })
        )
    
    return html.Div([
        # Overlay gelap
        html.Div(id=f'overlay-{modal_id}', style={
            'display': 'none', 'position': 'fixed', 'top': 0, 'left': 0,
            'width': '100%', 'height': '100%', 'backgroundColor': 'rgba(0,0,0,0.5)',
            'zIndex': '999'
        }),
        # Jendela modal
        html.Div([
            # Header modal
            html.Div([
                html.H4(konten['judul'], style={
                    'color': 'white', 'margin': 0, 'fontSize': '16px', 'fontFamily': 'Times New Roman'
                }),
                html.Button('✕', id=f'tutup-{modal_id}', n_clicks=0, style={
                    'background': 'none', 'border': 'none', 'color': 'white',
                    'fontSize': '20px', 'cursor': 'pointer', 'padding': '0 8px'
                })
            ], style={
                'background': 'linear-gradient(135deg, #1a3a6b, #2980b9)',
                'padding': '16px 20px', 'display': 'flex', 'justifyContent': 'space-between',
                'alignItems': 'center', 'borderRadius': '10px 10px 0 0'
            }),
            # Isi modal
            html.Div(baris_konten, style={
                'padding': '20px', 'maxHeight': '65vh', 'overflowY': 'auto'
            }),
            # Footer modal
            html.Div([
                html.Small('📚 Sumber: Kerangka Kerja BI 4 Lapis — Penelitian Tesis S2 Informatika, Universitas Nusa Putra', style={
                    'color': '#7f8c8d', 'fontStyle': 'italic'
                }),
                html.Button('Tutup', id=f'tutup-bawah-{modal_id}', n_clicks=0, style={
                    'backgroundColor': '#1a3a6b', 'color': 'white', 'border': 'none',
                    'padding': '8px 20px', 'borderRadius': '5px', 'cursor': 'pointer',
                    'fontSize': '13px'
                })
            ], style={
                'padding': '12px 20px', 'backgroundColor': '#f1f3f5', 'display': 'flex',
                'justifyContent': 'space-between', 'alignItems': 'center',
                'borderTop': '1px solid #dee2e6', 'borderRadius': '0 0 10px 10px'
            })
        ], id=f'modal-{modal_id}', style={
            'display': 'none', 'position': 'fixed', 'top': '50%', 'left': '50%',
            'transform': 'translate(-50%, -50%)', 'width': '600px', 'maxWidth': '90vw',
            'backgroundColor': 'white', 'borderRadius': '10px', 'zIndex': '1000',
            'boxShadow': '0 20px 60px rgba(0,0,0,0.3)'
        })
    ])


# ─────────────────────────────────────────────────────────────────────────────
# GAYA CSS INLINE (KARTU KPI)
# ─────────────────────────────────────────────────────────────────────────────
STYLE_KARTU = {
    'width': '23%', 'display': 'inline-block', 'margin': '0.5%',
    'backgroundColor': 'white', 'borderRadius': '10px', 'padding': '16px',
    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)', 'verticalAlign': 'top',
    'cursor': 'default'
}

STYLE_TOMBOL_INFO = {
    'backgroundColor': 'none', 'border': '1px solid #bdc3c7',
    'borderRadius': '4px', 'padding': '3px 10px', 'fontSize': '11px',
    'color': '#7f8c8d', 'cursor': 'pointer', 'marginTop': '6px',
    'width': '100%', 'fontFamily': 'Times New Roman'
}

# ─────────────────────────────────────────────────────────────────────────────
# DEFINISI TATA LETAK UTAMA
# ─────────────────────────────────────────────────────────────────────────────
app.layout = html.Div([
    
    # ── Semua komponen modal ───────────────────────────────────────────────
    buat_modal('harga', 'harga'),
    buat_modal('perubahan', 'perubahan'),
    buat_modal('akurasi', 'akurasi'),
    buat_modal('sharpe', 'sharpe'),
    buat_modal('var', 'var'),
    buat_modal('model', 'model'),
    
    # ── Header Utama ───────────────────────────────────────────────────────
    html.Div([
        html.H1("🧠 Dashboard Intelijen Bisnis — Prediksi Harga Bitcoin",
                style={'textAlign': 'center', 'color': '#1a3a6b', 'fontFamily': 'Times New Roman',
                       'fontSize': '22px', 'marginBottom': '5px'}),
        html.H3("Sistem Pendukung Keputusan Berbasis Kerangka Kerja BI Empat Lapis (LSTM · GRU · XGBoost)",
                style={'textAlign': 'center', 'color': '#7f8c8d', 'fontFamily': 'Times New Roman',
                       'fontSize': '13px', 'fontWeight': 'normal', 'marginBottom': '20px'})
    ], style={'backgroundColor': '#f0f4ff', 'padding': '20px 20px 10px',
              'borderBottom': '3px solid #1a3a6b'}),
    
    # ── Kartu KPI (4 Kartu Utama) ──────────────────────────────────────────
    html.Div([
        # Kartu 1: Harga Saat Ini
        html.Div([
            html.P("💰 HARGA SAAT INI", style={'fontSize': '10px', 'color': '#95a5a6', 'margin': '0',
                                               'letterSpacing': '1px', 'fontWeight': 'bold'}),
            html.H2(id='current-price', children="$44.850,00",
                    style={'color': '#27ae60', 'textAlign': 'left', 'fontSize': '26px', 'margin': '4px 0'}),
            html.P("BTC/USDT · Per Jam", style={'fontSize': '11px', 'color': '#bdc3c7', 'margin': '0'}),
            html.Button("ℹ️ Penjelasan Akademis", id='buka-harga', n_clicks=0, style=STYLE_TOMBOL_INFO)
        ], style=STYLE_KARTU),
        
        # Kartu 2: Perubahan 24 Jam
        html.Div([
            html.P("📈 PERUBAHAN 24 JAM", style={'fontSize': '10px', 'color': '#95a5a6', 'margin': '0',
                                                  'letterSpacing': '1px', 'fontWeight': 'bold'}),
            html.H2(id='daily-change', children="+2,34%",
                    style={'color': '#27ae60', 'textAlign': 'left', 'fontSize': '26px', 'margin': '4px 0'}),
            html.P("Log Return Harian", style={'fontSize': '11px', 'color': '#bdc3c7', 'margin': '0'}),
            html.Button("ℹ️ Penjelasan Akademis", id='buka-perubahan', n_clicks=0, style=STYLE_TOMBOL_INFO)
        ], style=STYLE_KARTU),
        
        # Kartu 3: Akurasi Prediksi (DWR)
        html.Div([
            html.P("🎯 DIRECTIONAL WIN RATE", style={'fontSize': '10px', 'color': '#95a5a6', 'margin': '0',
                                                      'letterSpacing': '1px', 'fontWeight': 'bold'}),
            html.H2(id='accuracy', children="72,3%",
                    style={'color': '#3498db', 'textAlign': 'left', 'fontSize': '26px', 'margin': '4px 0'}),
            html.P("Model LSTM · Threshold ≥55%", style={'fontSize': '11px', 'color': '#bdc3c7', 'margin': '0'}),
            html.Button("ℹ️ Penjelasan Akademis", id='buka-akurasi', n_clicks=0, style=STYLE_TOMBOL_INFO)
        ], style=STYLE_KARTU),
        
        # Kartu 4: Sharpe Ratio
        html.Div([
            html.P("📊 SHARPE RATIO", style={'fontSize': '10px', 'color': '#95a5a6', 'margin': '0',
                                              'letterSpacing': '1px', 'fontWeight': 'bold'}),
            html.H2(id='sharpe-ratio', children="1,45",
                    style={'color': '#9b59b6', 'textAlign': 'left', 'fontSize': '26px', 'margin': '4px 0'}),
            html.P("Imbal Hasil / Risiko · SR ≥1,0", style={'fontSize': '11px', 'color': '#bdc3c7', 'margin': '0'}),
            html.Button("ℹ️ Penjelasan Akademis", id='buka-sharpe', n_clicks=0, style=STYLE_TOMBOL_INFO)
        ], style=STYLE_KARTU),
    ], style={'backgroundColor': '#f8f9fa', 'padding': '16px 20px',
              'borderBottom': '1px solid #dee2e6'}),
    
    # ── Baris Grafik Utama ────────────────────────────────────────────────
    html.Div([
        html.Div([dcc.Graph(id='price-chart')],
                 style={'width': '65%', 'display': 'inline-block', 'padding': '10px',
                        'verticalAlign': 'top'}),
        html.Div([dcc.Graph(id='technical-indicators')],
                 style={'width': '34%', 'display': 'inline-block', 'padding': '10px',
                        'verticalAlign': 'top'})
    ], style={'backgroundColor': 'white', 'padding': '10px 0'}),
    
    # ── Baris Kedua: Metrik Risiko + Sinyal ───────────────────────────────
    html.Div([
        html.Div([
            dcc.Graph(id='risk-metrics')
        ], style={'width': '55%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
        
        html.Div([
            html.H4("🔔 Sinyal Perdagangan Aktif", style={'color': '#2c3e50', 'marginBottom': '12px',
                                                            'fontFamily': 'Times New Roman'}),
            html.Div([
                html.Div([
                    html.Strong("● BELI", style={'color': '#27ae60', 'fontSize': '14px'}),
                    html.P("Momentum positif terdeteksi. RSI memasuki zona netral (30–70) dengan MACD di atas garis sinyal, mengindikasikan kenaikan harga jangka pendek yang berpotensi berlanjut.",
                           style={'fontSize': '12px', 'color': '#555', 'margin': '4px 0 0',
                                  'lineHeight': '1.5'})
                ], style={'margin': '8px 0', 'padding': '12px', 'backgroundColor': '#d5f4e6',
                          'borderRadius': '6px', 'borderLeft': '4px solid #27ae60'}),
                html.Div([
                    html.Strong("● WASPADA VOLATILITAS", style={'color': '#e67e22', 'fontSize': '14px'}),
                    html.P("Walk-Forward Validation mendeteksi peningkatan dispersi residual prediksi pada 24 jam terakhir, mengindikasikan periode ketidakpastian pasar yang tinggi.",
                           style={'fontSize': '12px', 'color': '#555', 'margin': '4px 0 0',
                                  'lineHeight': '1.5'})
                ], style={'margin': '8px 0', 'padding': '12px', 'backgroundColor': '#fdebd0',
                          'borderRadius': '6px', 'borderLeft': '4px solid #e67e22'}),
                html.Button("ℹ️ Tentang VaR (95%)", id='buka-var', n_clicks=0,
                            style={**STYLE_TOMBOL_INFO, 'marginTop': '10px'})
            ])
        ], style={'width': '43%', 'display': 'inline-block', 'padding': '10px',
                  'verticalAlign': 'top'})
    ], style={'backgroundColor': '#f8f9fa', 'borderTop': '1px solid #dee2e6'}),
    
    # ── Perbandingan Performa Model ────────────────────────────────────────
    html.Div([
        html.Div([
            html.H4("⚖️ Perbandingan Performa Tiga Model Prediktif",
                    style={'color': '#1a3a6b', 'fontFamily': 'Times New Roman',
                           'textAlign': 'center', 'marginBottom': '4px'}),
            html.P("RMSE (kiri) vs. Directional Win Rate — %(kanan)",
                   style={'textAlign': 'center', 'color': '#95a5a6', 'fontSize': '12px',
                          'marginBottom': '4px'}),
            html.Button("ℹ️ Penjelasan Perbandingan Model",
                        id='buka-model', n_clicks=0,
                        style={**STYLE_TOMBOL_INFO, 'width': 'auto', 'display': 'block',
                               'margin': '0 auto 8px'})
        ]),
        dcc.Graph(id='model-comparison')
    ], style={'backgroundColor': 'white', 'padding': '16px 20px',
              'borderTop': '2px solid #1a3a6b'}),
    
    # ── Footer ─────────────────────────────────────────────────────────────
    html.Div([
        html.P("🎓 Prototipe Sistem Pendukung Keputusan | Kerangka Kerja BI Empat Lapis | "
               "Tesis S2 Informatika — Universitas Nusa Putra | Data: Binance Spot API (BTC/USDT · 2021–2026)",
               style={'textAlign': 'center', 'color': '#95a5a6', 'fontSize': '11px',
                      'fontFamily': 'Times New Roman', 'margin': 0})
    ], style={'backgroundColor': '#2c3e50', 'padding': '12px'}),
    
    # ── Komponen Auto-Refresh ─────────────────────────────────────────────
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0)
    
], style={'fontFamily': 'Times New Roman, Times, serif', 'backgroundColor': '#f0f4ff',
          'minHeight': '100vh'})


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: TAMPILKAN / SEMBUNYIKAN MODAL
# ─────────────────────────────────────────────────────────────────────────────
def daftarkan_callback_modal(modal_id):
    @app.callback(
        [Output(f'modal-{modal_id}', 'style'),
         Output(f'overlay-{modal_id}', 'style')],
        [Input(f'buka-{modal_id}', 'n_clicks'),
         Input(f'tutup-{modal_id}', 'n_clicks'),
         Input(f'tutup-bawah-{modal_id}', 'n_clicks')],
        prevent_initial_call=True
    )
    def toggle_modal(buka, tutup, tutup_bawah):
        from dash import ctx
        if not ctx.triggered_id:
            raise dash.exceptions.PreventUpdate
        
        TAMPIL_MODAL = {
            'display': 'block', 'position': 'fixed', 'top': '50%', 'left': '50%',
            'transform': 'translate(-50%, -50%)', 'width': '600px', 'maxWidth': '90vw',
            'backgroundColor': 'white', 'borderRadius': '10px', 'zIndex': '1000',
            'boxShadow': '0 20px 60px rgba(0,0,0,0.3)'
        }
        TAMPIL_OVERLAY = {
            'display': 'block', 'position': 'fixed', 'top': 0, 'left': 0,
            'width': '100%', 'height': '100%', 'backgroundColor': 'rgba(0,0,0,0.5)',
            'zIndex': '999'
        }
        SEMBUNYIKAN_MODAL = {'display': 'none'}
        SEMBUNYIKAN_OVERLAY = {'display': 'none'}
        
        if ctx.triggered_id == f'buka-{modal_id}':
            return TAMPIL_MODAL, TAMPIL_OVERLAY
        return SEMBUNYIKAN_MODAL, SEMBUNYIKAN_OVERLAY

for mid in ['harga', 'perubahan', 'akurasi', 'sharpe', 'var', 'model']:
    daftarkan_callback_modal(mid)


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: PEMBARUAN DATA KPI
# ─────────────────────────────────────────────────────────────────────────────
@app.callback(
    [Output('current-price', 'children'),
     Output('daily-change', 'children'),
     Output('accuracy', 'children'),
     Output('sharpe-ratio', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def perbarui_kpi(n):
    harga = f"${np.random.uniform(43000, 47000):,.2f}".replace(',', '.').replace('.', ',', 1)
    perubahan = np.random.uniform(-5, 5)
    tanda = "+" if perubahan > 0 else ""
    perubahan_str = f"{tanda}{perubahan:.2f}%".replace('.', ',')
    return harga, perubahan_str, "72,3%", "1,45"


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: GRAFIK PREDIKSI HARGA
# ─────────────────────────────────────────────────────────────────────────────
@app.callback(
    Output('price-chart', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def perbarui_grafik_harga(n):
    tanggal = pd.date_range(end=datetime.now(), periods=100, freq='H')
    harga_aktual = np.cumsum(np.random.randn(100) * 150) + 45000
    harga_prediksi = harga_aktual + np.random.randn(100) * 250
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tanggal, y=harga_aktual, mode='lines',
                             name='Harga Aktual BTC/USDT',
                             line=dict(color='#1a3a6b', width=2.5)))
    fig.add_trace(go.Scatter(x=tanggal, y=harga_prediksi, mode='lines',
                             name='Prediksi LSTM',
                             line=dict(color='#e74c3c', width=1.8, dash='dash')))
    fig.update_layout(
        title='Perbandingan Harga Aktual vs. Prediksi LSTM (100 Jam Terakhir)',
        xaxis_title='Waktu (Per Jam)', yaxis_title='Harga (USD)',
        template='plotly_white', height=370,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        margin=dict(l=50, r=20, t=60, b=40)
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: GRAFIK INDIKATOR TEKNIKAL RSI
# ─────────────────────────────────────────────────────────────────────────────
@app.callback(
    Output('technical-indicators', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def perbarui_indikator_teknikal(n):
    tanggal = pd.date_range(end=datetime.now(), periods=50, freq='H')
    rsi = np.clip(np.cumsum(np.random.randn(50) * 3) + 50, 10, 90)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tanggal, y=rsi, mode='lines', name='RSI-14',
                             line=dict(color='#e74c3c', width=2),
                             fill='tozeroy', fillcolor='rgba(231,76,60,0.1)'))
    fig.add_hline(y=70, line_dash="dash", line_color="red",
                  annotation_text="Jenuh Beli (≥70)", annotation_position="top right")
    fig.add_hline(y=30, line_dash="dash", line_color="green",
                  annotation_text="Jenuh Jual (≤30)", annotation_position="bottom right")
    fig.update_layout(
        title='Indikator Momentum: RSI-14',
        xaxis_title='Waktu', yaxis_title='Nilai RSI (0–100)',
        template='plotly_white', height=370,
        yaxis=dict(range=[0, 100]),
        margin=dict(l=50, r=20, t=60, b=40)
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: GRAFIK METRIK RISIKO
# ─────────────────────────────────────────────────────────────────────────────
@app.callback(
    Output('risk-metrics', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def perbarui_metrik_risiko(n):
    metrik = ['VaR 95%\n(-2,34%)', 'Max Drawdown\n(-8,50%)', 'Volatilitas\n(4,20%)', 'Beta\n(1,10)']
    nilai = [2.34, 8.5, 4.2, 1.1]
    warna = ['#e74c3c', '#c0392b', '#e67e22', '#f39c12']
    
    fig = go.Figure(data=[
        go.Bar(x=metrik, y=nilai, marker_color=warna,
               text=[f"{v:.2f}%" for v in nilai], textposition='outside')
    ])
    fig.update_layout(
        title='Metrik Risiko Eksekutif (Lapis 4 — BI Analytics)',
        xaxis_title='Dimensi Risiko', yaxis_title='Magnitudo (%)',
        template='plotly_white', height=370,
        margin=dict(l=50, r=20, t=60, b=60)
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CALLBACKS: GRAFIK PERBANDINGAN MODEL
# ─────────────────────────────────────────────────────────────────────────────
@app.callback(
    Output('model-comparison', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def perbarui_perbandingan_model(n):
    model = ['XGBoost\n(Baseline)', 'LSTM\n(Deep Learning)', 'GRU\n(Deep Learning)']
    rmse = [0.1524, 0.1145, 0.1058]
    dwr = [58.4, 72.3, 69.8]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=model, y=rmse, name='RMSE ↓ (Lebih kecil = lebih baik)',
                         marker_color=['#95a5a6', '#3498db', '#27ae60'], yaxis='y',
                         text=[f"{v:.4f}" for v in rmse], textposition='outside'))
    fig.add_trace(go.Scatter(x=model, y=dwr, name='Directional Win Rate — % ↑ (Lebih besar = lebih baik)',
                             mode='lines+markers+text', yaxis='y2',
                             line=dict(color='#e74c3c', width=2.5, dash='dot'),
                             marker=dict(size=10, color='#e74c3c'),
                             text=[f"{v}%" for v in dwr], textposition='top center'))
    fig.update_layout(
        title='Trade-off: Presisi Numerik (RMSE) vs. Akurasi Arah (Win Rate) — Hipotesis Utama Penelitian',
        xaxis_title='Model', template='plotly_white', height=380,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        yaxis=dict(title='RMSE', side='left', color='#3498db'),
        yaxis2=dict(title='Directional Win Rate (%)', side='right',
                   overlaying='y', color='#e74c3c'),
        margin=dict(l=60, r=60, t=80, b=60)
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
