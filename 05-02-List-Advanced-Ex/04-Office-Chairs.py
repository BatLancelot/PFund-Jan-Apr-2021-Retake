rooms = int(input())
free_chairs = 0
enough_chairs = True

for i in range(1, rooms + 1):
    room_data = input().split()
    chairs = len(room_data[0])
    people = int(room_data[1])

    if chairs >= people:
        free_chairs += chairs - people
    else:
        enough_chairs = False
        chainrs_needed = people - chairs
        print(f'{chainrs_needed} more chairs needed in room {i}')

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
