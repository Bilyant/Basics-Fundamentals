def get_factorial_number(n, numbers: list):
    result = n

    for num in numbers:
        result *= num

    return result

def get_factorials_division(a, b):
    numbers_a = [x for x in range(1, a)]
    numbers_b = [x for x in range(1, b)]

    first_factorial = get_factorial_number(a, numbers_a)
    second_factorial = get_factorial_number(b, numbers_b)
    result = first_factorial / second_factorial
    return f'{result:.2f}'



first_number = int(input())
second_number = int(input())
print(get_factorials_division(first_number, second_number))
