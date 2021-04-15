data_dict = {}

while True:
    resource = input()

    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in data_dict:
        data_dict[resource] = 0
    data_dict[resource] += quantity

    # elif data.isalpha():
    #     if data not in data_dict:
    #         data_dict[data] = 0
    #     current_key = data
    # elif data.isdigit():
    #     data_dict[current_key] += int(data)
    # else:
    #     print('Wrong data')

for resource, quantity in data_dict.items():
    print(f'{resource} -> {quantity}')
