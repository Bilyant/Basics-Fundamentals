product_type = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if product_type == "coffee":
        price = quantity * 0.5
    elif product_type == "water":
        price = quantity * 0.8
    elif product_type == "beer":
        price = quantity * 1.2
    elif product_type == "sweets":
        price = quantity * 1.45
    elif product_type == "peanuts":
        price = quantity * 1.6
if city == "Plovdiv":
    if product_type == "coffee":
        price = quantity * 0.4
    elif product_type == "water":
        price = quantity * 0.7
    elif product_type == "beer":
        price = quantity * 1.15
    elif product_type == "sweets":
        price = quantity * 1.3
    elif product_type == "peanuts":
        price = quantity * 1.5
if city == "Varna":
    if product_type == "coffee":
        price = quantity * 0.45
    elif product_type == "water":
        price = quantity * 0.7
    elif product_type == "beer":
        price = quantity * 1.10
    elif product_type == "sweets":
        price = quantity * 1.35
    elif product_type == "peanuts":
        price = quantity * 1.55
print(price)
