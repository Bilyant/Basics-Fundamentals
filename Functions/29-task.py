def even_odd(*args):
    command = args[-1]
    criteria = 1 if command == 'odd' else 0
    return [n for n in args[:-1] if n % 2 == criteria]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
