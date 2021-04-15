import math

num_of_people = int(input())
capacity = int(input())

print(f'{math.ceil(num_of_people / capacity)}')
""" V2 without importing modules:

if num_of_people % capacity == 0:
    result = num_of_people // capacity
else:
    result = num_of_people // capacity + 1

    V3 for fun, output with some textexplanation:

if num_of_people > capacity and part_cources == 0:
    print(f'{full_cources} courses * {capacity} people')
elif num_of_people > capacity and part_cources > 0:
    print(f'{full_cources} courses * {capacity} people + 1 cource * {part_cources} persons')
elif num_of_people < capacity:
    print('All the persons fit inside in the elevator. Only one course is needed.')
 """
