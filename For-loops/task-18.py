import math

total_tournaments = int(input())
starting_points = int(input())
points_sf = 0
points_w = 0
points_f = 0
games_w_count = 0
for number in range(total_tournaments):
    result = input()
    if result == "W":
        points_w += 2000
        games_w_count += 1
    elif result == "F":
        points_f += 1200
    elif result == "SF":
        points_sf += 720
total_points = points_w + points_f + points_sf + starting_points
print(f"Final points: {total_points}")
average_points = (total_points - starting_points) / total_tournaments
print(f"Average points: {math.floor(average_points)}")
percent_w = games_w_count / total_tournaments * 100
print(f"{percent_w:.2f}%")
