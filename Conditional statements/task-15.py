import math

series_name = input()
episode_length_minutes = int(input())
break_length_minutes = int(input())

lunch_break_minutes = break_length_minutes * 0.125
leisure_break_minutes = break_length_minutes * 0.25
spare_minutes_left = break_length_minutes - (lunch_break_minutes + leisure_break_minutes)
if episode_length_minutes <= spare_minutes_left:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(spare_minutes_left - episode_length_minutes)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_length_minutes - spare_minutes_left)} more minutes.")