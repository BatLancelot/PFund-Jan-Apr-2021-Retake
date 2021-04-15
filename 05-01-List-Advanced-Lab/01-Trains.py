num_of_wagons = int(input())
train = []

for wagon in range(num_of_wagons):
    train.append(0)

while True:
    command = input().split(' ')
    if command[0] == 'End':
        break

    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        train[int(command[1])] -= int(command[2])

print(train)
