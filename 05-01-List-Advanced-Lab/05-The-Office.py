employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

improved_employees_happiness = []

for i in range(len(employees_happiness)):
    improved_employees_happiness.append(
        employees_happiness[i] * improvement_factor)

average_employees_happiness = sum(
    improved_employees_happiness) / len(improved_employees_happiness)

list_of_happy_ones = []

for i in range((len(improved_employees_happiness))):
    if improved_employees_happiness[i] >= average_employees_happiness:
        list_of_happy_ones.append(improved_employees_happiness[i])

if len(list_of_happy_ones) >= (len(improved_employees_happiness) / 2):
    print(
        f'Score: {len(list_of_happy_ones)}/{len(improved_employees_happiness)}. Employees are happy!')
else:
    print(
        f'Score: {len(list_of_happy_ones)}/{len(improved_employees_happiness)}. Employees are not happy!')
