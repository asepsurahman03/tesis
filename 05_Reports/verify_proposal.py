import re
filepath = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f'Ukuran file: {len(content):,} chars')

checks_bad = [
    ('0.1058', r'0\.1058'),
    ('0.1145', r'0\.1145'),
    ('0.1524', r'0\.1524'),
    ('72.3%', r'72\.3\s*%'),
    ('69.8%', r'69\.8\s*%'),
    ('58.4%', r'58\.4\s*%'),
    ('VaR -2.34', r'-2\.34'),
    ('VaR -4.10', r'-4\.10'),
    ('Sharpe 1.45', r'LSTM.*?1\.45'),
]
print('\n=== CEK ANGKA HASIL (tidak boleh ada) ===')
clean = True
for label, pattern in checks_bad:
    m = re.search(pattern, content)
    if m:
        ctx = content[max(0,m.start()-40):m.end()+40].replace('\n',' ')
        print(f'  [MASIH ADA] {label}: ...{ctx[:80]}...')
        clean = False
    else:
        print(f'  [BERSIH] {label}')

print('\n=== CEK STRUKTUR BAB I ===')
for s in ['1.1 Latar Belakang','1.2 Identifikasi Masalah','1.3 Rumusan Masalah',
          '1.4 Tujuan Penelitian','1.5 Manfaat Penelitian','1.6 Batasan Penelitian',
          '1.7 Sistematika Penulisan']:
    print(f'  [{"ADA" if s in content else "HILANG!"}] {s}')

print('\n=== CEK ABSTRAK PROSPEKTIF ===')
ai = content.find('abstract-section')
ae = content.find('</div>', ai) + 6
abstrak = content[ai:ae]
for kw in ['akan', 'diharapkan', 'direncanakan']:
    print(f'  [{"OK" if kw in abstrak else "TIDAK ADA"}] kata kunci: "{kw}"')

print()
if clean:
    print('>>> FILE SUDAH BERSIH - Sesuai format PROPOSAL TESIS <<<')
else:
    print('>>> MASIH ADA ANGKA HASIL yang perlu dihapus <<<')
