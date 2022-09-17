from time import sleep


def print_table(lista):
    print('\033[1;31m-' * 70, '\033[m')
    print(f"{'Cod.':<5}{'Nome':<15}{'Goals':<30}{'Total':>10}")
    print('\033[1;31m-' * 70, '\033[m')

    for count, x in enumerate(lista):
        print(f"{count:<5}{x['name']:<15}{str(x['score']):<30}{x['total']:>10}")
    print('\033[1;31m-' * 70, '\033[m')

print('\033[1;33mREGISTRATION OF PLAYERS AND GOALS SCORED\033[m')
players = []
while True:
    single_player = {'name': input('Name: ')}
    games = int(input('How many games did you play? '))
    goals = []
    [goals.append(int(input(f'Goals in the #{i + 1} game: '))) for i in range(0, games)]
    single_player['score'] = goals
    single_player['total'] = sum(goals)
    players.append(single_player)

    flag = input('Continue [Y/N]? ')
    while flag not in 'YyNn':
        flag = input('\033[31mInvalid input! Continue [Y/N]? \033[m')
    if flag in 'Nn':
        sleep(0.5)
        print('\033[31m- ...Loading... -\033[m')
        sleep(1)
        break

print_table(players)

while True:
    n = int(input('\033[31m[999 to end]\033[m Wanna see about which one? '))
    if n == 999:
        break
    if n > len(players)-1 or n < 0:
        print('\033[31mInvalid input\033[m')
    else:
        print('\033[1;32m-' * 70)
        print(f"-- Details about {players[n]['name']} --")
        for i in range(0, len(players[n]['score'])):
            print(f"In the #{i + 1} game scored {players[n]['score'][i]} goals")
        print('-' * 70, '\033[m')
        print_table(players)

print('\033[32mThank you, see you later!\033[m')
