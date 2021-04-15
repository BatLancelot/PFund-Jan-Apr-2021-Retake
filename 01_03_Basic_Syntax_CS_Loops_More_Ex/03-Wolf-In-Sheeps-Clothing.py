herd = input().split(', ')

for i in reversed(range(len(herd))):
    if herd[i] == 'wolf':
        if herd[i] == herd[-1]:
            print("Please go away and stop eating my sheep")
            break
        else:
            sheep = abs(i - (len(herd) - 1))
            print(
                f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
            break
