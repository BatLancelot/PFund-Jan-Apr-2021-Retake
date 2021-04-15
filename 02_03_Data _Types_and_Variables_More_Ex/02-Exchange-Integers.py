num_1 = int(input())
num_2 = int(input())

print(f'Before:\na = {num_1}\nb = {num_2}')

num_1, num_2 = num_2, num_1

print(f'After:\na = {num_1}\nb = {num_2}')
