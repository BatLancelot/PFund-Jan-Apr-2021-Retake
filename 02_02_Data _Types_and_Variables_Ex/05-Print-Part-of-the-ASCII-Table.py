ascii_index_in = int(input())
ascii_index_out = int(input())

chars_in_range = []

for char in range(ascii_index_in, ascii_index_out + 1):
    chars_in_range.append(chr(char))

print(' '.join(chars_in_range))

""" V2 whitout using LIST, .append and ' '.join :
chars_in_range = ''

for char in range(ascii_index_in, ascii_index_out + 1):
    chars_in_range += chr(char)

print(chars_in_range)
"""
