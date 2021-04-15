string_of_numbers = list(map(int, input().split(', ')))
list_of_indexes = []

for i in range(len(string_of_numbers)):
    if string_of_numbers[i] % 2 == 0:
        list_of_indexes.append(i)

print(list_of_indexes)
