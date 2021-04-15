number = int(input())

synonyms = {}

for word in range(number):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)
# V1 joinint in a new varible
for word, synonym in synonyms.items():
    word_synonyms = ', '.join(synonym)
    print(f'{word} - {word_synonyms}')
# V2 joining in the print
# for word in synonyms:
#     print(f"{word} - {', '.join(synonyms[word])}")
