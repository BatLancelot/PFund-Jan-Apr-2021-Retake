string = input()

list_of_indices = []

for i in range(len(string)):
    if string[i].isupper():
        list_of_indices.append(i)

print(list_of_indices)
