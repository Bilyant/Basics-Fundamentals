command = input()
data = [int(n) for n in input().split()]
odd_or_even = 1 if command == 'Odd' else 0
result = sum([int(n) for n in data if n % 2 == odd_or_even]) * len(data)
print(result)
