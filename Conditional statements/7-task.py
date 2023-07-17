figure_type = input()
side_a = float(input())
area = 0
import math

if figure_type == "square":
    area = side_a * side_a
elif figure_type == "rectangle":
    side_b = float(input())
    area = side_a * side_b
elif figure_type == "circle":
    area = math.pi * side_a * side_a
elif figure_type == "triangle":
    side_b = float(input())
    area = side_a * side_b / 2
print(f"{area:.3f}")
