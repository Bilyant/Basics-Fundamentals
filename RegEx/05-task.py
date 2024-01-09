import re

data = []
line = input()

while line:
    data.append(line)
    line = input()

data = ' '.join(data)
expression = r'\d+'
matches = re.findall(expression, data)
print(' '.join(matches))
