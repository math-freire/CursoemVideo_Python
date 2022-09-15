from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
for i in range(1, 5):
    jogadas[f'Jogador {i}'] = randint(1, 6)

ranking = []
for k, v in jogadas.items():
    print(f"{k} rodou {v}")
    sleep(0.3)
print('-='*30)
sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1))
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.3)
