raw_data = input().split()

products = {}

for index in range(0, len(raw_data), 2):
    key, value = raw_data[index], raw_data[index + 1]
    products[key] = int(value)

print(products)
