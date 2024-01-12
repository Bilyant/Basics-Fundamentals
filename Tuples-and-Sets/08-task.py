number = int(input())
elements = set()

for _ in range(number):
    line = input().split()
    for el in line:
        elements.add(el)

print(*elements, sep='\n')
