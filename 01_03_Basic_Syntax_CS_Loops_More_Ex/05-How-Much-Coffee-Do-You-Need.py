command = input()

list_of_comands = ['coding', 'dog', 'cat', 'movie']
coffee_counter = 0

while command != 'END':
    if command.lower() in list_of_comands:
        if command.islower():
            coffee_counter += 1
        elif command.isupper():
            coffee_counter += 2

    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
