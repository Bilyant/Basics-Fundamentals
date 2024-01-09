import re

data = input()
word = input()
expression = rf'\b{word}\b'
matches = re.findall(expression, data, flags=re.I)
print(len(matches))
