number = int(input())

for more in range(number + 1):
    print('*' * more)

for less in range(number - 1, 0, -1):
    print('*' * less)
