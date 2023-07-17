product_type = input()
day_of_the_week = input()
quantity = float(input())
is_Valid = False
price = 0
if day_of_the_week == "Monday" or \
        day_of_the_week == "Tuesday" or \
        day_of_the_week == "Wednesday" or \
        day_of_the_week == "Thursday" or \
        day_of_the_week == "Friday":
    is_Valid = True
    if product_type == "banana":
        price = quantity * 2.5
    elif product_type == "apple":
        price = quantity * 1.2
    elif product_type == "orange":
        price = quantity * 0.85
    elif product_type == "grapefruit":
        price = quantity * 1.45
    elif product_type == "kiwi":
        price = quantity * 2.7
    elif product_type == "pineapple":
        price = quantity * 5.5
    elif product_type == "grapes":
        price = quantity * 3.85
elif day_of_the_week == "Saturday" or \
        day_of_the_week == "Sunday":
    is_Valid = True
    if product_type == "banana":
        price = quantity * 2.7
    elif product_type == "apple":
        price = quantity * 1.25
    elif product_type == "orange":
        price = quantity * 0.9
    elif product_type == "grapefruit":
        price = quantity * 1.6
    elif product_type == "kiwi":
        price = quantity * 3
    elif product_type == "pineapple":
        price = quantity * 5.6
    elif product_type == "grapes":
        price = quantity * 4.2
if is_Valid and product_type != "tomato" and product_type != "beer":
    print(f"{price:.2f}")
else:
    print("error")
    