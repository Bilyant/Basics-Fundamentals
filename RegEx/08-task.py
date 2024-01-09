import re

data = input()
expression = r'(^|(?<=\s))[a-zA-Z]+[\._-]*[a-zA-Z]+@[a-z]+-?[a-z]*\.([a-z]+-?[a-z]\.?)*\b'
matches = re.finditer(expression, data)

for match in matches:
    print(match.group())
