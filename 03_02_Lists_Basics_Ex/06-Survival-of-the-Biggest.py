import sys

string_of_integers = input().split()
n = int(input())

min_number = sys.maxsize
list_of_integers = []

for string in string_of_integers:
    digit = int(string)
    list_of_integers.append(digit)

for _ in range(n):
    for digit in list_of_integers:
        if digit < min_number:
            min_number = digit
    list_of_integers.remove(min_number)
    min_number = sys.maxsize

print(list_of_integers)
