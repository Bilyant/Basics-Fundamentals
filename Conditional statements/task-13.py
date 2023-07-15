""" Code for calculating if Ivan has managed to 
beat the current world swimming records """

import math

current_world_record_seconds = float(input())
total_distance_meters = float(input())
ivan_seconds_per_meter = float(input())

time_without_slowing = total_distance_meters * ivan_seconds_per_meter
current_slow = math.floor(total_distance_meters // 15) * 12.5
final_time_ivan = time_without_slowing + current_slow
difference = final_time_ivan - current_world_record_seconds

if final_time_ivan < current_world_record_seconds:
    print(f"Yes, he succeeded! The new world record is {final_time_ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
