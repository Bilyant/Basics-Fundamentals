def fill_the_box(height, length, width, *args):
    h, l, w = int(height), int(length), int(width)
    capacity = h * l * w
    cubes_left = 0
    for arg in args:
        if arg != 'Finish':
            if capacity - int(arg) >= 0:
                capacity -= int(arg)
            else:
                cubes_left += int(arg)
        else:
            break

    if not cubes_left:
        return f'There is free space in the box. You could put {capacity} more cubes.'
    else:
        result = abs(capacity - cubes_left)
        return f'No more free space! You have {result} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
