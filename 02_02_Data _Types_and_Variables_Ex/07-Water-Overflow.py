TANK_CAPACITY = 255

n_number_of_lines = int(input())
current_tank_filling = 0

for num in range(n_number_of_lines):
    quantities_of_water = int(input())
    if (current_tank_filling + quantities_of_water) <= TANK_CAPACITY:
        current_tank_filling += quantities_of_water
    else:
        print('Insufficient capacity!')
print(f'{current_tank_filling}')
