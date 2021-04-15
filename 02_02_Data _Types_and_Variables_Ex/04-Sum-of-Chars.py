n_num_of_lines = int(input())
total_sum = 0

for i in range(n_num_of_lines):
    letter = input()
    total_sum += ord(letter)

print(f'The sum equals: {total_sum}')
