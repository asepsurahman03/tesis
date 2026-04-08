import re

file_path = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the temporary 41, 42, 43 we added at the bottom
bibliography_to_remove = r'''<p>\[41\] E\. Bouri, C\. K\. M\. Lau, B\. Lucey, and D\. Roubaud, "Trading volume and the predictability\s+of return and volatility in the cryptocurrency market," <i>Finance Res\. Lett\.</i>, vol\. 29,\s+pp\. 340&ndash;346, Jun\. 2019, doi: 10\.1016/j\.frl\.2018\.08\.015\.</p>\s*<p>\[42\] S\. Ben Nouir and H\. Ben Haj Hamida, "How do economic policy uncertainty and geopolitical\s+risk drive Bitcoin volatility\?" <i>Res\. Int\. Bus\. Finance</i>, vol\. 64, p\. 101881, Apr\. 2023,\s+doi: 10\.1016/j\.ribaf\.2023\.101881\.</p>\s*<p>\[43\] Antara News, "Bitcoin terkoreksi ke USD 66\.824 di tengah eskalasi konflik AS-Iran-Israel,\s+Fear and Greed Index 8/100," Antara News, Apr\. 3, 2026\. \[Online\]\. Available:\s+https://www\.antaranews\.com\. \[Accessed: Apr\. 3, 2026\]\.</p>\s*'''
# Copied exactly from the prompt? No, maybe regex is safer. Let's just seek the patterns.

# Let's cleanly pop everything from [40] onwards temporarily
match = re.search(r'(<p>\[40\].*?</p>\s*)(<p>\[41\].*?</p>\s*<p>\[42\].*?</p>\s*<p>\[43\].*?</p>\s*)?</div>', html, flags=re.DOTALL)
if match:
    # Just cut it off after [40]
    html = html[:match.end(1)] + "</div>\n\n</body>\n\n</html>"

# We first shift [3]..[40] to [6]..[43] in the body and bibliography.
# NOTE: Need to be careful not to shift equation numbers, e.g. Eq [1] is not used, but [0,1] is.
# Let's only shift citations `[number]` or `[number], [number]`.
# We'll find all `[digits]` and if it's <p>[digits] in bibliography, shift it.

def shift_match(m):
    num = int(m.group(1))
    if 3 <= num <= 40:
        return f"[{num+3}]"
    return m.group(0)

# Replace in citations [X] where X is between 3 and 40
# Only replace if preceded by space or bracket, so we don't hit math like `[0, 1]` -> `[0, 4]` ? 
# Well 1 is not between 3 and 40. [4, 5] ? Let's use a targeted approach.
html = re.sub(r'\[(\d+)\]', shift_match, html)

# Now in the text, we have [44], [45], [46] because the [41], [42], [43] got shifted! Wait!
# If I do `shift_match`, 41 is NOT shifted. It remains 41.
# So I can just replace [41] -> [3], [42] -> [4], [43] -> [5].
html = html.replace('[41]', '[3]')
html = html.replace('[42]', '[4]')
html = html.replace('[43]', '[5]')

# Now construct the new bibliography items for [3], [4], [5]
new_bib = '''<p>[3] A. F. Aysan, E. Demir, G. Gozgor, and C. K. M. Lau, "Effects of the geopolitical risks on Bitcoin returns and volatility," <i>Res. Int. Bus. Finance</i>, vol. 47, pp. 511–518, Jan. 2019, doi: 10.1016/j.ribaf.2018.09.011.</p>
        <p>[4] S. Ben Nouir and H. Ben Haj Hamida, "How do economic policy uncertainty and geopolitical risk drive Bitcoin volatility?" <i>Res. Int. Bus. Finance</i>, vol. 64, p. 101809, Apr. 2023, doi: 10.1016/j.ribaf.2022.101809.</p>
        <p>[5] Antara News, "Bitcoin terkoreksi ke USD 66.824 di tengah eskalasi konflik AS-Iran-Israel, Fear and Greed Index 8/100," Antara News, Apr. 3, 2026. [Online]. Available: https://www.antaranews.com. [Accessed: Apr. 3, 2026].</p>
        '''

# We need to insert these before [6] in the bibliography.
# [6] is what used to be [3].
# The start of bibliography is `<h2>Daftar Pustaka...</h2>... <p>[1]...<p>[2]...<p>[6] (originally [3]) `
# Let's find `<p>[6]` and insert `new_bib` right before it.
html = html.replace('<p>[6]', new_bib + '<p>[6]')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Renumbering complete.")
