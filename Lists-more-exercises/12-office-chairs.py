rooms = int(input())
free_chairs = 0
game_on = True

for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    chairs, visitors = len(chairs), int(visitors)
    if visitors > chairs:
        chairs_needed = visitors - chairs
        game_on = False
        print(f'{chairs_needed} more chairs needed in room {room}')
    elif chairs > visitors:
        free_chairs += chairs - visitors

if game_on:
    print(f'Game On, {free_chairs} free chairs left')
