""" This code calculates the total expenses for the pet's food expenses
based on the price of each packet
of food and the total number of animals  """

dogs_food_count = int(input())
cats_food_count = int(input())
dogs_food_cost = dogs_food_count * 2.5
cats_food_cost = cats_food_count * 4
total_food_cost = dogs_food_cost + cats_food_cost
print(f"{total_food_cost} lv.")
