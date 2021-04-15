string_list = input().split(', ')
num_of_beggars = int(input())
digit_list = []
sum_of_beggars_income = []

for num in string_list:
    digit = int(num)
    digit_list.append(digit)

for i in range(num_of_beggars):
    sum_of_beggars_income.append(0)

index = 0
for digit in digit_list:
    sum_of_beggars_income[index] += digit
    index += 1
    if index == len(sum_of_beggars_income):
        index = 0

print(sum_of_beggars_income)
