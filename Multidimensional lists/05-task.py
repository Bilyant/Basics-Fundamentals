number = int(input())
matrix = []
result = 0

for _ in range(number):
    line = [int(n) for n in input().split()]
    matrix.append(line)

for i in range(number):
    result += matrix[i][i]

print(result)
