number = [int(n) for n in input()]

biggest_num = sorted(number, reverse=True)

print(''.join(str(n) for n in biggest_num))
