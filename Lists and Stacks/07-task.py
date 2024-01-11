num = int(input())
stack = []

for i in range(num):
    line = input()
    command == line[0]
    if command == '1':
        _, num = line.split()
        stack.append(int(num))
    elif command == '2 and stack':
        stack.pop()
    elif command == '3 and stack':
        print(max(stack))
    elif command == '4 and stack':
        print(min(stack))

if stack:
    while stack:
        if len(stack) > 1:
            print(stack.pop(), end=', ')
        else:
            print(stack.pop())
