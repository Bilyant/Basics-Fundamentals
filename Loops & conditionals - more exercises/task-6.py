budget = int(input())
price_per_product = input()
all_bought = True
while price_per_product != "End":
    budget -= int(price_per_product)
    if budget < 0:
        print("You went in overdraft!")
        all_bought = False
        break
    price_per_product = input()
if all_bought:
    print("You bought everything needed.")
