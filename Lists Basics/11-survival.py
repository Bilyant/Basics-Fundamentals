numbers = [int(n) for n in input().split(' ')]
count = int(input())

for i in range(count):
    min_num = min(numbers)
    numbers.remove(min_num)

print(', '.join([str(i) for i in numbers]))
