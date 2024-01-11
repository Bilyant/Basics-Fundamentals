expression = input()
stack_indices = []

for idx in range(len(expression)):
    char = expression[idx]
    if char == '(':
        stack_indices.append(idx)
    elif char == ')':
        start = stack_indices.pop()
        print(expression[start: idx + 1])
