actor_name = input()
starting_points = float(input())
jury_count = int(input())
points_awarded = 0
total_points_awarded = 0
points_awarded = 0
for number in range(jury_count):
    current_judge_name = input()
    current_points_award = float(input())
    points_awarded = (len(current_judge_name) * current_points_award) / 2
    total_points_awarded += points_awarded
    if total_points_awarded + starting_points > 1250.5:
        final_points = total_points_awarded + starting_points
        print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
        break
if total_points_awarded + starting_points <= 1250.5:
    points_needed = 1250.5 - (total_points_awarded + starting_points)
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
