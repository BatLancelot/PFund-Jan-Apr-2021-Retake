word = input()
reversed_word = ''

for letter in reversed(word):
    reversed_word += letter

print(reversed_word)

""" Same functionality in less code: Iterrate the STR backwards 
    using '-1' step argument"""
print(word[::-1])
