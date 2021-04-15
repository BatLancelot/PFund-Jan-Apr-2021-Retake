def string_checker(text):
    digits = ''
    chars = ''
    other = ''

    for char in text:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            chars += char
        else:
            other += char
    return digits, chars, other


string_to_check = input()

print('\n'.join(string_checker(string_to_check)))
