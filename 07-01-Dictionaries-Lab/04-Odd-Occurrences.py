words = input().split(' ')

words_count = {}

for word in words:
    if word.lower() not in words_count:
        words_count[word.lower()] = 0
    words_count[word.lower()] += 1

odd_words = []

for word, count in words_count.items():
    if count % 2 != 0:
        odd_words.append(word)

print(' '.join(odd_words))
