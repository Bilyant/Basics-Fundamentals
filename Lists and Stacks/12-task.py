from collections import deque


def add_time(time, seconds_to_add):
    hours, minutes, seconds = time[0], time[1], time[2]

    seconds += seconds_to_add
    if seconds > 59:
        seconds = 0
        minutes += 1
        if minutes > 59:
            minutes = 0
            hours += 1
            if hours > 23:
                hours = 0
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def get_robot(robots_in_production):
    available_robot = False
    for r in robots_assembly_line:
        if robots_in_production[r] == 0:
            robots_in_production[r] += robots_processing_time[r]
            available_robot = True
            break

    if available_robot:
        return r
    else:
        return False


def reduce_robot_time(robots_time):
    for robot in robots_in_production:
        if robots_in_production[robot] > 0:
            robots_in_production[robot] -= 1


data = deque(r for r in input().split(';'))
running_time = [int(x) for x in input().split(':')]
robots = deque([])
line = input()
seconds_count = 0
robots_processing_time = {}
robots_in_production = {}
products = deque()
robots_assembly_line = deque()

for i in range(len(data)):
    info = data[i].split('-')
    name, time = info[0], int(info[1])
    robots_processing_time[name] = time
    robots_in_production[name] = 0
    robots_assembly_line.append(name)

while line != 'End':
    products.append(line)
    line = input()

while products:
    product = products.popleft()
    seconds_count += 1
    running_time = add_time(running_time, 1)
    robot = get_robot(robots_in_production)
    if robot:
        print(f'{robot} - {product} [{running_time}]')
    else:
        products.append(product)

    running_time = [int(x) for x in running_time.split(':')]
    reduce_robot_time(1)

tets101()
