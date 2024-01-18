from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque([int(n) for n in args])
    while numbers:
        for key, value in kwargs.items():
            if not numbers:
                break
            number = numbers.popleft()
            if key == 'a':
                kwargs['a'] += number
            elif key == 's':
                kwargs['s'] -= number
            elif key == 'd':
                try:
                    kwargs['d'] /= number
                except ZeroDivisionError:
                    continue
            elif key == 'm':
                kwargs['m'] *= number

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
