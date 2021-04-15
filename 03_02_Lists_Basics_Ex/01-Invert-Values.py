# string_list = input().split() or

string = input()

string_list = string.split()
invert_numbers = []

for digit in string_list:
    invert_number = -int(digit)
    invert_numbers.append(invert_number)

print(invert_numbers)
