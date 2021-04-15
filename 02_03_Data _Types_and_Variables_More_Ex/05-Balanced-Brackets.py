n_lines = int(input())

opened = False
closed = False

for _ in range(n_lines):
    string = input()
    if string == '(' or string == ')':
        if string == '(' and not opened:
            opened = True
            closed = False
        elif string == ')' and opened:
            closed = True
            opened = False
        else:
            print('UNBALANCED')
            break
    else:
        continue
else:
    print('BALANCED')
