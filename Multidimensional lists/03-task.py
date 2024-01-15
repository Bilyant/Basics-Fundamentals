number = int(input())
even_matrix = []

for _ in range(number):
    line = [int(n) for n in input().split(', ')]
    even_matrix.extend(line)

print(even_matrix)
