string_of_chars = input()

chars = {}

for char in string_of_chars:
    if char == ' ':
        continue
    if char not in chars:
        chars[char] = 0
    chars[char] += 1


for char, quantity in chars.items():
    print(f'{char} -> {quantity}')
