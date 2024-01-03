def sort_ascending(numbers: list):
    return sorted(numbers)


numbers = [int(x) for x in input().split(' ')]
print(sort_ascending(numbers))
