def calc_odd_and_even_numbers(number: list):
    odd_sum = sum([x for x in number if x % 2 != 0])
    even_sum = sum([x for x in number if x % 2 == 0])
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


numbers = [int(x) for x in input()]
print(calc_odd_and_even_numbers(numbers))
