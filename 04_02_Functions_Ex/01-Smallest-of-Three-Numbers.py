a = int(input())
b = int(input())
c = int(input())


def find_the_smallest_num(a, b, c):
    if b > a < c:
        return a
    if a > b < c:
        return b
    if a > c < b:
        return c


print(find_the_smallest_num(a, b, c))
