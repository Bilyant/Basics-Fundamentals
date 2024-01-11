from collections import deque

parentheses = deque(list(input()))
opening_parentheses = deque()
are_balanced = True

while parentheses:
    char = parentheses.popleft()
    if char in '{[(':
        opening_parentheses.append(char)
    elif not opening_parentheses:
        are_balanced = False
        break
    else:
        if f'{opening_parentheses.pop()}{char}' not in '{}[]()':
            are_balanced = False
            break

are_balanced = False if opening_parentheses else True
print('YES' if are_balanced else 'NO')