def add_and_subtract(a, b, c):

    def sum_numbers(a, b):
        return a + b

    def subtract(sum_numbers, c):
        return sum_numbers - c

    return subtract(sum_numbers(a, b), c)


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
