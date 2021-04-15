budget = float(input())
flour = float(input())

cozonacs = 0
colored_eggs = 0

egg_price = flour * .75
milk_price = flour * 1.25
cozonac_price = egg_price + flour + (milk_price / 4)

while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= (cozonacs - 2)

print(
    f'You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
