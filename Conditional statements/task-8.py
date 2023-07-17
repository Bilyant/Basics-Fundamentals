first_score = int(input())
second_score = int(input())
third_score = int(input())
total_time = first_score + second_score + third_score
minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
