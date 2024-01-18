def operate(operator, *args):
    result = 0
    if operator == '+':
        result = sum([n for n in args])
    else:
        num = args[0]
        if operator == '-':
            for n in args[1:]:
                num -= n
        if operator == '*':
            for n in args[1:]:
                num *= n
        if operator == '/':
            for n in args[1:]:
                num /= n
        result = num
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
