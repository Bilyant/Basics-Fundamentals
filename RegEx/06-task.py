import re

data = input()
expression = r'\b_([a-zA-Z0-9]+)\b'
matches = re.findall(expression, data)
print(','.join(matches))
