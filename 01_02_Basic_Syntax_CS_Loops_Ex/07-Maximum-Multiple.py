divisor = int(input())
bound = int(input())

for i in range(bound, -1, -1):
    if i % divisor == 0 and bound >= 1:
        print(i)
        break
