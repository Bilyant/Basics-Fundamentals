from collections import deque

petrol_pumps = int(input())
data = deque()
result = None

gas_tank = 0
circles = 0
petrol = 0

for stop in range(petrol_pumps):
    data.append([int(x) for x in input().split()])

for stop in range(len(data)):

    for refil, distance in data:
        refil = data[0][0]
        distance = data[0][1]
        gas_tank += refil
        if gas_tank < distance:
            gas_tank = 0
            data.append(data.popleft())
            continue
        else:
            gas_tank -= distance
            circles += 1
            if circles == petrol_pumps:
                result = stop
                break
            data.append(data.popleft())

print(result)
