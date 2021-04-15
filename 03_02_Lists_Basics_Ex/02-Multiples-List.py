factor = int(input())
count = int(input())

numbers_list = []

for mult in range(1, count + 1):
    number = mult * factor
    numbers_list.append(number)

print(numbers_list)
