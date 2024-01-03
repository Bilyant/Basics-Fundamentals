def calculate(first_num, second_num, operation):
    resul = None
    if operation == 'multiply':
        result = first_num * second_num
    elif operation == 'divide':
        result = first_num // second_num
    elif operation == 'add':
        result = first_num + second_num
    elif operation == 'subtract':
        result = first_num - second_num
    return result


operation = input()
first_num = int(input())
second_num = int(input())
print(calculate(first_num, second_num, operation))
