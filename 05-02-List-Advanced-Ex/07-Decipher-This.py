message = input().split()
digit_replaced_mes = []


for word in message:
    temp_digit = ''

    for digit in word:
        if not digit.isdigit():
            break

        temp_digit += digit

    digit = int(temp_digit)
    char = chr(digit)
    new_word = word.replace(temp_digit, char)
    digit_replaced_mes.append(new_word)

final_message = []
for word in digit_replaced_mes:
    temp_word = [l for l in word]
    temp_word[1], temp_word[-1] = temp_word[-1], temp_word[1]
    final_word = ''.join(temp_word)
    final_message.append(final_word)

print(' '.join(final_message))
