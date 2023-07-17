movie_type = input()
rows_count = int(input())
columns_count = int(input())
total_sets = rows_count * columns_count
single_price_ticket = 0
total_profit = 0
if movie_type == "Premiere":
    single_price_ticket = 12
    total_profit = single_price_ticket * total_sets
elif movie_type == "Normal":
    single_price_ticket = 7.5
    total_profit = single_price_ticket * total_sets
elif movie_type == "Discount":
    single_price_ticket = 5
    total_profit = single_price_ticket * total_sets
print(f"{total_profit:.2f} leva")
