""" Calculating the cost for a food delivery  """

price_for_chicken_menu = 10.35
price_for_fish_menu = 12.4
price_for_vegetarian_menu = 8.15
price_delivery = 2.5

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegetarian_menus = int(input())

cost_food_order = (count_chicken_menus * price_for_chicken_menu) + (count_fish_menus * price_for_fish_menu) + (
            count_vegetarian_menus * price_for_vegetarian_menu)
cost_dessert = cost_food_order * 0.2
final_cost = cost_food_order + cost_dessert + price_delivery
print(final_cost)
