from random import randint
jogadas = {}
for i in range(1, 5):
    jogadas[f'Jogador {i}'] = randint(1, 6)

for k, v in jogadas.items():
    print(f"{k} rodou {v}")
print('-='*20)
sorted_jogadas = sorted(jogadas.items(), key=lambda dado: dado[1])
for c, i in enumerate(sorted_jogadas):
    print(f"{i[0]} ficou em #{c+1} rodando {i[1]}")
