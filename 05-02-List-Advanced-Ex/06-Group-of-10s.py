import math

list_of_numbers = [int(num) for num in input().split(', ')]

bigest_num = max(list_of_numbers)
number_of_groups = math.ceil(bigest_num / 10)

for i in range(1, number_of_groups + 1):
    upper_edge = i * 10
    lower_edge = upper_edge - 10

    current_range = [
        n for n in list_of_numbers if lower_edge < n <= upper_edge]

    print(f"Group of {i * 10}'s: {current_range}")
