import re

with open("Proposal_Tesis_Bitcoin_BI_Indo.html", "r", encoding="utf-8") as f:
    content = f.read()

# Check refs in daftar pustaka
refs = re.findall(r"<p>\[(\d+)\]", content)
print("Refs found:", refs[:25])

# Check citation first-appearance order in body (before references div)
body = content[:content.find('<div class="references">')]
cits = re.findall(r"\[(\d+)\]", body)
seen = []
for c in cits:
    if c not in seen:
        seen.append(c)
print("First appearance order:", seen[:22])
