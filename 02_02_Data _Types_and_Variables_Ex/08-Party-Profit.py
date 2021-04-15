companions_count = int(input())
days = int(input())

day = 1
coins = 0

while day != days + 1:
    if day % 10 == 0:
        companions_count -= 2

    if day % 15 == 0:
        companions_count += 5
        coins -= companions_count * 2

    coins += 50 - (companions_count * 2)

    if day % 3 == 0:
        coins -= companions_count * 3

    if day % 5 == 0:
        coins += companions_count * 20

    day += 1

coins = coins // companions_count

print(f'{companions_count} companions received {coins} coins each.')
