puzzle_single_price = 2.6
doll_single_price = 3
teddy_bear_single_price = 4.1
minion_single_price = 8.2
truck_single_price = 2

excursion = float(input())
puzzles_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_count = puzzles_count + doll_count + teddy_bear_count + minion_count + truck_count
profit = (puzzles_count * puzzle_single_price) + (doll_count * doll_single_price) + (
        teddy_bear_count * teddy_bear_single_price) + (minion_count * minion_single_price) + (
                 truck_count * truck_single_price)

if total_count > 49:
    profit = profit * 0.75
rent = profit * 0.1
final_profit = profit - rent

if final_profit >= excursion:
    print(f"Yes! {final_profit - excursion:.2f} lv left.")
else:
    print(f"Not enough money! {excursion - final_profit:.2f} lv needed.")
