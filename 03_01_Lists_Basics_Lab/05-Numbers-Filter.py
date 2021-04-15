n = int(input())

numbers_list = []

for _ in range(n):
    digit = int(input())
    numbers_list.append(digit)

command = input()
filtered_list = []

for digit in numbers_list:
    filter_passes = (
        (digit % 2 == 0 and command == 'even') or
        (digit % 2 != 0 and command == 'odd') or
        (digit >= 0 and command == 'positive') or
        (digit < 0 and command == 'negative')
    )
    if filter_passes:
        filtered_list.append(digit)

print(filtered_list)
