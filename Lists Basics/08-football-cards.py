team_A = 11
team_B = 11
sent_off_players_A_team = []
sent_off_players_B_team = []

data = input().split(' ')
game_is_terminated = False

for item in data:
    team, player = item.split('-')
    if team == 'A' and player not in sent_off_players_A_team:
        team_A -= 1
        sent_off_players_A_team.append(player)
    elif team == 'B' and player not in sent_off_players_B_team:
        team_B -= 1
        sent_off_players_B_team.append(player)

    if team_A < 7 or team_B < 7:
        game_is_terminated = True
        break

print(f"Team A - {team_A}; Team B - {team_B}")
if game_is_terminated:
    print("Game was terminated")
