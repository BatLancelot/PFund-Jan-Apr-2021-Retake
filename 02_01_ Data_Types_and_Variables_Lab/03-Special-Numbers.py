n = int(input())

# for num in range(1, n + 1):
#     sum_of_digits = 0
#     num_copy = num
#     while num_copy > 0:
#         digit = num_copy % 10
#         sum_of_digits += digit
#         num_copy = int(num_copy / 10) # or num_copy = num_copy // 10

#     is_special = sum_of_digits in (5, 7, 11)

#     print(f'{num} -> {is_special}')


""" V2 with FOR LOOP """
SPECIAL_NUMBERS = (5, 7, 11)

for num in range(1, n + 1):
    sum_of_digits = 0
    for c in str(num):
        sum_of_digits += int(c)

    is_special = sum_of_digits in SPECIAL_NUMBERS

    print(f'{num} -> {is_special}')
