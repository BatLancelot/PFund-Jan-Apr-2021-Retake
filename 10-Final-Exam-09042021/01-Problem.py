scrable_bag = input()

while True:
    commands = input().split()

    if ('Exchange' in commands[0] and 'Tiles' in commands[1]) or 'Play' in commands or 'Pass' in commands:
        if 'Exchange' in commands[0] and 'Tiles' in commands[1]:
            letters = commands[2]
            scrable_bag = letters + scrable_bag[len(letters):]
            print(f'{" ".join(scrable_bag)}')
            break

        elif 'Pass' in commands[0] and len(commands[1]) == 0:
            print(f'{" ".join(scrable_bag)}')
            break

        elif 'Play' in commands:
            for i in range(len(scrable_bag)):
                if scrable_bag[i] == ' ':
                    print(f'You are playing with the word {scrable_bag[:i]}.')
                    break
                print(f'You are playing with the word {scrable_bag}.')
            break

    elif 'Move' in commands:
        index = int(commands[1])
        if index <= len(scrable_bag):
            letter = scrable_bag[index]
            scrable_bag = scrable_bag[:index] + '' + scrable_bag[index + 1:]
            scrable_bag += letter
        # continue
    elif 'Insert' in commands[0] and 'Space' in commands[1]:
        index = int(commands[2])
        scrable_bag = scrable_bag[:index] + ' ' + scrable_bag[index:]

    elif 'Reverse' in commands:
        substring = commands[1]
        scrable_bag = scrable_bag.replace(substring, '', 1)
        scrable_bag += substring[::-1]
