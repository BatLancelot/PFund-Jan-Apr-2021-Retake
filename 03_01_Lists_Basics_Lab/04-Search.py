n = int(input())
word = input()

source_list = []
target_list = []

for _ in range(n):
    string = input()
    source_list.append(string)
    if word in string:
        target_list.append(word)

print(f'{source_list}\n{target_list}')
