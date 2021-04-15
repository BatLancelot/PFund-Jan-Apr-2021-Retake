year = int(input())

next_happy_year = False
while not next_happy_year:
    year += 1
    if len(set(str(year))) == len(str(year)):
        print(year)
        next_happy_year = True
