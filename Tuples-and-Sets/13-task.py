import math
from collections import deque

expression = deque(input().split())
result = []

while expression:

    char = expression.popleft()
    if (char.lstrip('-')).isdigit():
        result.append(int(char))
    else:
        if len(result) > 1:
            current_result = result[0]
            if char == '-':
                for i in range(1, len(result)):
                    current_result -= result[i]
            elif char == '+':
                for i in range(1, len(result)):
                    current_result += result[i]
            elif char == '/':
                for i in range(1, len(result)):
                    current_result = math.floor(current_result / result[i])
            elif char == '*':
                for i in range(1, len(result)):
                    current_result *= result[i]

            result.clear()
            result.append(current_result)

print(*result)
