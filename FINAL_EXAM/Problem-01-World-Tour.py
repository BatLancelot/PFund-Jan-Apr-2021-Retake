def add_stop(stops, index, string):
    if index <= len(stops):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stop(stops, start_index, end_index):
    if start_index <= len(stops) and end_index + 1 <= len(stops):
        stops = stops[:start_index] + '' + stops[end_index + 1:]
    return stops


def switch(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops = input()

while True:
    command = input().split(':')
    if 'Travel' in command:
        print(f'Ready for world tour! Planned stops: {stops}')
        break

    elif command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        stops = add_stop(stops, index, string)
        print(stops)

    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
        print(stops)

    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
        print(stops)
