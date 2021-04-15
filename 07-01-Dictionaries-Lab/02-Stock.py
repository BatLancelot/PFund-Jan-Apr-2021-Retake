raw_data = input().split(' ')
data_dict = {raw_data[i]: raw_data[i + 1] for i in range(0, len(raw_data), 2)}
# for i in range(0, len(raw_data), 2):
#     key, val = raw_data[i], raw_data[i + 1]
#     data_dict = key, val

product_to_search = input().split(' ')

for key in product_to_search:
    if key in data_dict.keys():
        print(f'We have {data_dict[key]} of {key} left')
    else:
        print(f"Sorry, we don't have {key}")
