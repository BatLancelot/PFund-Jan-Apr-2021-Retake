team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

red_cards = input().split()
if red_cards != 0:
    for card in red_cards:
        current_card = card.split('-')
        team = current_card[0]
        player_number = int(current_card[1])
        if team == 'A':
            if player_number not in team_a:
                continue
            team_a.remove(player_number)
            if len(team_a) < 7:
                break
        elif team == 'B':
            if player_number not in team_b:
                continue
            team_b.remove(player_number)
            if len(team_a) < 7:
                break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if len(team_a) < 7 or len(team_b) < 7:
    print('Game was terminated')
