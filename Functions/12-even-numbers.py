def get_even_numbers(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))


numbers = [int(x) for x in input().split(' ')]
print(get_even_numbers(numbers))
