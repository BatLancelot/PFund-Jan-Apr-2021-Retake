storage = {}
shop = {}
total_money = 0

while True:
    command = input().split()
    if "End" in command:
        for key, value in sorted(shop.items()):
            print(f'{key}: {value:.2f}')
        print('-----------')
        if len(storage) == 0:
            print()
        else:
            for key, value in sorted(storage.items()):
                print(f'{key}: {abs(value):.2f}')
        print('-----------')
        print(f'Total Income: {total_money:.2f}')
        break

    if command[0] == 'Deliver':
        dist_name, cost_of_deliv = command[1], float(command[2])
        if dist_name not in storage:
            storage[dist_name] = cost_of_deliv
        else:
            storage[dist_name] += cost_of_deliv

    elif command[0] == 'Return':
        dist_name, cost_of_return = command[1], float(command[2])
        if dist_name not in storage:
            continue
        else:
            if storage[dist_name] < cost_of_return:
                continue
            storage[dist_name] -= cost_of_return
            if storage[dist_name] == 0:
                del storage[dist_name]

    elif command[0] == 'Sell':
        client_name, money_spend = command[1], float(command[2])
        if client_name in shop:
            shop[client_name] += money_spend
        else:
            shop[client_name] = money_spend
        total_money += money_spend
