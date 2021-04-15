electrons = int(input())

result = []

shell_index = 1

while electrons > 0:
    shell_electrons = 2 * shell_index ** 2

    if electrons > shell_electrons:
        result.append(shell_electrons)
    else:
        result.append(electrons)

    electrons -= shell_electrons
    shell_index += 1

print(result)
