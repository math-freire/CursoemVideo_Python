scoreboard = 'Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico PR', 'Atlético-MG', \
             'Atlético-MG', 'América-MG', 'Goiás', 'Santos', 'Red Bull Bragantino', 'Botafogo', 'São Paulo', 'Ceará', \
             'Fortaleza', 'Coritiba', 'Cuiabá-MT', 'Avaí', 'Atlético-GO', 'Juventude'

print('\033[32mPrimeiros colocados: \033[m', end='')
for i in range(0, 4):
    print(f'{scoreboard[i]}, ' if i < 3 else f'{scoreboard[i]}.\n', end='')

print('\033[31mÚltimos colocados: \033[m', end='')
for i in range(-4, 0):
    print(f'{scoreboard[i]}, ' if i < -1 else f'{scoreboard[i]}.\n', end='')

print('\033[33mOrdem alfabética: \033[m', end='')
for flag, time in enumerate(sorted(scoreboard)):
    if flag == len(scoreboard)-1:
        print(f'{time}.')
    else:
        print(time, end=', ')

print('\033[34mPosição do Red Bull Bragantino: \033[m', end='')
print(scoreboard.index('Red Bull Bragantino'))

print('\033[35mF chapecoense...\033[m')
