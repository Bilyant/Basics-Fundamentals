def get_min(numbers: list):
    return min(numbers)


def get_max(numbers: list):
    return max(numbers)


def get_sum(numbers: list):
    return sum(numbers)

def get_min_max_sum(min_num, max_num, sum_num):
    result = [
        f'The minimum number is {min_num}',
        f'The maximum number is {max_num}',
        f'The sum number is: {sum_num}',
    ]
    return '\n'.join(result)


numbers = [int(x) for x in input().split()]
print(get_min_max_sum(
    get_min(numbers),
    get_max(numbers),
    get_sum(numbers)
))
