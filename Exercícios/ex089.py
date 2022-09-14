def my_media(x):
    return (x[0] + x[1])/2


boletim = []
while True:
    nome = []
    notas = []
    nome.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    boletim.append(nome[:])
    boletim.append(notas[:])
    nome.clear()
    notas.clear()

    flag = input('\033[33mContinuar [S/N]? \033[m')
    while flag not in 'SsNn':
        flag = input('\033[31mEntrada incorreta.\nContinuar [S/N]? \033[m')
    if flag in 'Nn': break

print('-='*35)
print(f"{'No.':<5}{'NOME':<15}{'MEDIA':>10}")
print('_'*35)
for flag, i in enumerate(range(0, len(boletim), 2)):
    print(f"{flag:<5}{boletim[i][0]:<15}{my_media(boletim[i+1]):>10.2f}")
print('_'*35)
while True:
    a = int(input('\033[31m[999 encerra]\033[m Mostrar notas de qual aluno? '))
    if a == 999:
        print('\033[32mAté breve!\033[m')
        break
    while True:
        try:
            print(f'As notas de {boletim[a*2][0]} são {boletim[a*2+1]}')
            break
        except IndexError:
            print('\033[31mPor favor, digite um valor válido!\033[m')
            a = int(input('\033[31m[-1 encerra]\033[m Mostrar notas de qual aluno? '))
    print('_'*35)
