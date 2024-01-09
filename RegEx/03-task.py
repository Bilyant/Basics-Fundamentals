import re

data = input()
pattern = r'\d{2}(?P<separator>[./-])[A-Z][a-z]{2}\1\d{4}'
matches = re.finditer(pattern, data)

for match in matches:
    group = match.group()
    separator = match.group('separator')
    date, month, year = group.split(str(separator))
    print(f'Day: {date}, Month: {month}, Year: {year}')