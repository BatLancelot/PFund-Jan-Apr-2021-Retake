words_list = input().split(', ')
string = input()

unique_words_list = [word for word in words_list if word in string]

print(unique_words_list)
