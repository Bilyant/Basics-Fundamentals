number = int(input())
positives = []
negatives = []

for i in range(number):
    num = int(input())
    positives.append(num) if num > 0 else negatives.append(num)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')
