from collections import deque

rows, cols = [int(num) for num in input().split()]
text = input()
data = deque(text * rows)

for row_idx in range(rows):
    result = ''
    for col_idx in range(cols):
        result += data.popleft()
    if row_idx % 2 == 0:
        print(result)
    else:
        print(result[::-1])
