""" How quick the internet speed is based on the provided number """

speed_net = float(input())
if speed_net <= 10:
    print("slow")
elif speed_net > 10 and speed_net <= 50:
    print("average")
elif speed_net > 50 and speed_net <= 150:
    print("fast")
elif speed_net > 150 and speed_net <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
