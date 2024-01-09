import re

data = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, data)
result = [m.group() for m in matches]
print(' '.join(result))
