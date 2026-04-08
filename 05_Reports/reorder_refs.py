import re

filepath = "Proposal_Tesis_Bitcoin_BI_Indo.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# New reference entries in correct order (by first appearance in text)
new_refs = [
    (7,  '[7] S. Hochreiter and J. Schmidhuber, "Long short-term memory," <i>Neural Comput.</i>, vol. 9, no. 8, pp. 1735\u20131780, Nov. 1997, doi: 10.1162/neco.1997.9.8.1735.'),
    (8,  '[8] K. Cho, B. Van Merrienboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio, "Learning phrase representations using RNN encoder-decoder for statistical machine translation," in <i>Proc. 2014 Conf. Empir. Methods Nat. Lang. Process. (EMNLP)</i>, Doha, Qatar, Oct. 2014, pp. 1724\u20131734, doi: 10.3115/v1/D14-1179.'),
    (9,  '[9] P. L. Seabe, C. R. Moutsinga, and E. Pindza, "Forecasting cryptocurrency prices using LSTM, GRU, and bi-directional LSTM: A deep learning approach," <i>Fractal Fract.</i>, vol. 7, no. 2, p. 188, Feb. 2023, doi: 10.3390/fractalfract7020188.'),
    (10, '[10] T. Fischer and C. Krauss, "Deep learning with long short-term memory networks for financial market predictions," <i>Eur. J. Oper. Res.</i>, vol. 270, no. 2, pp. 654\u2013669, Oct. 2018, doi: 10.1016/j.ejor.2017.11.054.'),
    (11, '[11] S. Nakamoto, "Bitcoin: A peer-to-peer electronic cash system," White Paper, Oct. 2008. [Online]. Available: https://bitcoin.org/bitcoin.pdf.'),
    (12, '[12] E. F. Fama, "Efficient capital markets: A review of theory and empirical work," <i>J. Finance</i>, vol. 25, no. 2, pp. 383\u2013417, May 1970, doi: 10.2307/2325486.'),
    (13, '[13] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in <i>Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining</i>, San Francisco, CA, USA, Aug. 2016, pp. 785\u2013794, doi: 10.1145/2939672.2939785.'),
    (14, '[14] I. E. Livieris, E. Pintelas, and P. Pintelas, "A CNN\u2013LSTM model for gold price time-series forecasting," <i>Neural Comput. Appl.</i>, vol. 32, no. 23, pp. 17351\u201317360, Dec. 2020, doi: 10.1007/s00521-020-04867-x.'),
    (15, '[15] Y. Bengio, P. Simard, and P. Frasconi, "Learning long-term dependencies with gradient descent is difficult," <i>IEEE Trans. Neural Netw.</i>, vol. 5, no. 2, pp. 157\u2013166, Mar. 1994, doi: 10.1109/72.279181.'),
    (16, '[16] W. Jiang, "Applications of deep learning in stock market prediction: Recent progress," <i>Expert Syst. Appl.</i>, vol. 184, p. 115537, Dec. 2021, doi: 10.1016/j.eswa.2021.115537.'),
    (17, '[17] B. M. Henrique, V. A. Sobreiro, and H. Kimura, "Literature review: Machine learning techniques applied to financial market prediction," <i>Expert Syst. Appl.</i>, vol. 124, pp. 226\u2013251, Jun. 2019, doi: 10.1016/j.eswa.2019.01.012.'),
    (18, '[18] S. Siami-Namini, N. Tavakoli, and A. S. Namin, "A comparison of ARIMA and LSTM in forecasting time series," in <i>Proc. 17th IEEE Int. Conf. Mach. Learn. Appl. (ICMLA)</i>, Orlando, FL, USA, Dec. 2018, pp. 1394\u20131401, doi: 10.1109/ICMLA.2018.00227.'),
    (19, '[19] A. Thakkar and K. Chaudhari, "Fusion in stock market prediction: A decade survey on the necessity, recent developments, and potential future directions," <i>Inf. Fusion</i>, vol. 65, pp. 95\u2013107, Jan. 2021, doi: 10.1016/j.inffus.2020.08.019.'),
]

# Find references div
refs_start = content.find('<div class="references">')
refs_end   = content.find('</div>', refs_start) + len('</div>')
refs_block = content[refs_start:refs_end]

# Extract refs [1]-[6] (keep as-is, strip garbled encoding artifacts)
kept_paras = []
for m in re.finditer(r'<p>\[([1-6])\](.*?)</p>', refs_block, re.DOTALL):
    kept_paras.append((int(m.group(1)), m.group(0).strip()))
kept_paras.sort()

# Extract refs [20]-[40]
tail_paras = []
for m in re.finditer(r'<p>\[([2-9][0-9]|[3-9][0-9])\](.*?)</p>', refs_block, re.DOTALL):
    tail_paras.append((int(m.group(1)), m.group(0).strip()))
tail_paras.sort()

# Build new references block
lines = ['<div class="references">', '']
for _, para in kept_paras:
    lines.append('        ' + para)
for num, text in new_refs:
    lines.append('        <p>' + text + '</p>')
for _, para in tail_paras:
    lines.append('        ' + para)
lines.append('    </div>')

new_refs_block = '\n'.join(lines)

# Replace in content
new_content = content[:refs_start] + new_refs_block + content[refs_end:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: Reference list [7]-[19] reordered correctly.")
print(f"Total file size: {len(new_content)} bytes")
