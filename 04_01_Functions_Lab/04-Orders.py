COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

product = input()
quantity = int(input())


def calculate_order(product, quantity):
    if product == 'coffee':
        return COFFEE_PRICE * quantity
    if product == 'water':
        return WATER_PRICE * quantity
    if product == 'coke':
        return COKE_PRICE * quantity
    if product == 'snacks':
        return SNACKS_PRICE * quantity


print(f'{calculate_order(product, quantity):.2f}')
