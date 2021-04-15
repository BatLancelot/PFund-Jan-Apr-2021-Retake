a = int(input())
b = int(input())
c = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    total = subtract(result, c)
    return total


print(add_and_subtract(a, b, c))
