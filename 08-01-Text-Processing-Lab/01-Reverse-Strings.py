reversed_words = {}

while True:
    word = input()
    if word == 'end':
        for key, value in reversed_words.items():
            print(f'{key} = {value}')
        break

    if word not in reversed_words:
        reversed_words[word] = word[::-1]
