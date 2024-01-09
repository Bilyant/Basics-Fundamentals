import re

text = input()
pattern = r'\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b'
matches = re.findall(pattern, text)
print(' '.join(matches))
