from time import sleep

players = []
while True:
    single_player = {'name': input('Name: ')}
    games = int(input('How many games did you play? '))
    goals = []
    [goals.append(int(input(f'Goals in the #{i+1} game: '))) for i in range(0, games)]
    single_player['score'] = goals
    single_player['total'] = sum(goals)
    players.append(single_player)

    flag = input('Continue [Y/N]? ')
    while flag not in 'YyNn':
        flag = input('\033[31mInvalid input! Continue [Y/N]? \033[m')
    if flag in 'Nn':
        # sleep(1)
        print('\033[31m- Shutting down -\033[m')
        # sleep(1)
        break

print(players, end='\n\n')
print('\033[1;31m-'*70, '\033[m')
print(f"{'Cod.':<5}{'Nome':<15}{'Goals':<30}{'Total':>10}")
print('\033[1;31m-'*70, '\033[m')

for flag, player in enumerate(players):
    print(f"{flag:<5}{player['name']:<15}{str(player['score']):<30}{player['total']:>10}")
print('\033[1;31m-'*70, '\033[m')

while True:
    n = int(input('\033[31m[999 to end]\033[m Wanna see about which one?'))
    if n == 999:
        break
    if n > len(players) or n < 0:
        print('\033[31mInvalid input\033[m')
    else:
        print('\033[1;31m-' * 70, '\033[m')
        print(f"\033[1;32m-- Details about {players[n]['name']} --\033[m")
        for i in range(0, len(players[n]['score'])):
            print(f"In the #{i+1} game scored {players[n]['score'][i]} goals")
        print('\033[1;31m-' * 70, '\033[m')

print('\033[32mThank you, see you later!\033[m')
# print(single_player)
# print(f"{single_player['name']} played {games} games and scored {single_player['total']} goals.")
# [print(f"    => In game {i+1}, did {single_player['score'][i]} goals.") for i in range(0, games)]
