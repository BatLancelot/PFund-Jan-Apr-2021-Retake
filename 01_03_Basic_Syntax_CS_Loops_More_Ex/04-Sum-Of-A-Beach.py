string_to_search = input().lower()

list_of_words = ['sand', 'water', 'fish', 'sun']
word_count = 0

for word in list_of_words:
    if word in string_to_search:
        word_count += string_to_search.count(word)

print(word_count)
