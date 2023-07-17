number_one = int(input())
number_two = int(input())
operator_type = input()
if operator_type == "+":
    if (number_one + number_two) % 2 == 0:
        print(f"{number_one} {operator_type} {number_two} = {number_one + number_two} - even")
    else:
        print(f"{number_one} {operator_type} {number_two} = {number_one + number_two} - odd")
elif operator_type == "-":
    if (number_one - number_two) % 2 == 0:
        print(f"{number_one} {operator_type} {number_two} = {number_one - number_two} - even")
    else:
        print(f"{number_one} {operator_type} {number_two} = {number_one - number_two} - odd")
elif operator_type == "*":
    if (number_one * number_two) % 2 == 0:
        print(f"{number_one} {operator_type} {number_two} = {number_one * number_two} - even")
    else:
        print(f"{number_one} {operator_type} {number_two} = {number_one * number_two} - odd")
elif operator_type == "%":
    if number_two != 0:
        print(f"{number_one} {operator_type} {number_two} = {number_one % number_two}")
    else:
        print(f"Cannot divide {number_one} by zero")
elif operator_type == "/":
    if number_two != 0:
        print(f"{number_one} {operator_type} {number_two} = {number_one / number_two}")
    else:
        print(f"Cannot divide {number_one} by zero")
