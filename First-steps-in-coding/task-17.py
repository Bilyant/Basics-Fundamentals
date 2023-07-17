annual_fee = int(input())
price_shoes = annual_fee * 0.6
price_uniform = price_shoes * 0.8
price_ball = price_uniform / 4
price_accessories = price_ball / 5
total_expenses = annual_fee + price_shoes + price_uniform + price_ball + price_accessories
print(total_expenses)
