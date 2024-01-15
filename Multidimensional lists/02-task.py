number = int(input())
even_matrix = []

for _ in range(number):
    line = [int(n) for n in input().split(', ')]
    even_numbers = [n for n in line if n % 2 == 0]
    even_matrix.append(even_numbers)

print(even_matrix)
