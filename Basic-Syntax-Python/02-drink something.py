age = int(input())
output = ''

if age < 15:
    output = 'drink toddy'
elif age < 19:
    output = 'drink coke'
elif age < 22:
    output = 'drink beer'
else:
    output = 'drink whisky'

print(output)
