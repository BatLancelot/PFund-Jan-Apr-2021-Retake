key = int(input())
n_lines = int(input())

message = ''

for _ in range(n_lines):
    char = input()
    ascii_pos = ord(char)
    new_char = chr(ascii_pos + key)
    message += new_char

print(message)
