words_string = input().split(' ')
palindrome_to_search = input()

palindrome_found = []

for word in words_string:
    if word == word[::-1]:
        palindrome_found.append(word)

print(palindrome_found)
print(f'Found palindrome {palindrome_found.count(palindrome_to_search)} times')
