number = input()


def sum_odd_and_even_digits(number):
    even = 0
    odd = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
    return print(f'Odd sum = {odd}, Even sum = {even}')


sum_odd_and_even_digits(number)
