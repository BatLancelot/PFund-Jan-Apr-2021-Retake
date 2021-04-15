string = list(map(int, input().split(', ')))
numbers_found = []
zeros_found = []

for i in range(len(string)):
    digit = string[i]
    if digit == 0:
        zeros_found.append(string[i])
    else:
        numbers_found.append(string[i])

print(numbers_found + zeros_found)
