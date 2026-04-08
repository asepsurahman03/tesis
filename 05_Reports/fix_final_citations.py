import re

file_path = r'e:\Nusa Putra\S2\Semester 2\Business Intellegence\Penelitian\Analisis Bit Coin\05_Reports\Proposal_Tesis_Bitcoin_BI_Indo.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Swap the text citations in paragraph 2
text = text.replace('dan sangat sulit diprediksi [6], [7].</p>', 'dan sangat sulit diprediksi [3], [4].</p>')

# 2. Swap the text citations in paragraph 3 and 4
text = text.replace('(Februari 2022) [3].', '(Februari 2022) [5].')
text = text.replace('Timur Tengah [4].', 'Timur Tengah [6].')
text = text.replace('volatilitas Bitcoin [3], [4].', 'volatilitas Bitcoin [5], [6].')
text = text.replace('Fear&rdquo;) [5].', 'Fear&rdquo;) [7].')
text = text.replace('konvensional [3].</p>', 'konvensional [5].</p>')

# 3. Swap the bibliography entries
# Extract the entries
bib_3 = re.search(r'<p>\[3\] A. F. Aysan.*?</p>', text, re.DOTALL).group(0)
bib_4 = re.search(r'<p>\[4\] S. Ben Nouir.*?</p>', text, re.DOTALL).group(0)
bib_5 = re.search(r'<p>\[5\] Antara News.*?</p>', text, re.DOTALL).group(0)
bib_6 = re.search(r'<p>\[6\] S. Lahmiri.*?</p>', text, re.DOTALL).group(0)
bib_7 = re.search(r'<p>\[7\] H. Sebastião.*?</p>', text, re.DOTALL).group(0)

# Replace their markers temporarily
bib_3_new = bib_6.replace('[6]', '[3]')
bib_4_new = bib_7.replace('[7]', '[4]')
bib_5_new = bib_3.replace('[3]', '[5]')
bib_6_new = bib_4.replace('[4]', '[6]')
bib_7_new = bib_5.replace('[5]', '[7]')

# Now substitute them back in place
# To do this safely, we will assemble the new block of 5
new_block = f"{bib_3_new}\n        {bib_4_new}\n        {bib_5_new}\n        {bib_6_new}\n        {bib_7_new}"

# Find the entire original block
old_block_pattern = re.compile(
    re.escape(bib_3) + r'\s*' + 
    re.escape(bib_4) + r'\s*' + 
    re.escape(bib_5) + r'\s*' + 
    re.escape(bib_6) + r'\s*' + 
    re.escape(bib_7), 
    re.DOTALL
)

text =  re.sub(old_block_pattern, new_block, text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Final citation order fixed successfully!")
