def repeat_by_length(word):
    return word * len(word)


words: list = (input().split(' '))

print(f"{''.join(repeat_by_length(word) for word in words)}")
