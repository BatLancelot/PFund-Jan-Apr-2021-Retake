line_1 = input().split()
line_2 = input().split()
line_3 = input().split()
win_positions = ['012', '345', '678', '036', '147', '258', '048', '246']
game_string = list(map(int, line_1 + line_2 + line_3))
ones = ''
twos = ''

for i in range(len(game_string)):
    if game_string[i] == 1:
        ones += str(i)
    if game_string[i] == 2:
        twos += str(i)

if ones in win_positions:
    print('First player won')
elif twos in win_positions:
    print('Second player won')
else:
    print('Draw!')
