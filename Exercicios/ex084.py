nomepeso, pessoas = [], []
while True:
    nomepeso.append(input('Digite o nome: '))
    nomepeso.append(int(input('Digite o peso: ')))
    pessoas.append(nomepeso[:])
    nomepeso.clear()

    flag = input('Continue [Y/N]? ')
    while flag not in 'YyNn':
        flag = input('\033[31mInvalid input.\033[m Continue [Y/N]? ')
    if flag in 'Nn': break

print(f'Temos {len(pessoas)} pessoas na lista.')
print(pessoas)

maior = max(pessoas, key=lambda x: x[1])
maiores = []
for pessoa in pessoas:
    if pessoa[1] == maior[1]:
        maiores.append(pessoa)
print(maiores)

menor = min(pessoas, key=lambda x: x[1])
menores = []
for pessoa in pessoas:
    if pessoa[1] == menor[1]:
        menores.append(pessoa)
print(menores)
