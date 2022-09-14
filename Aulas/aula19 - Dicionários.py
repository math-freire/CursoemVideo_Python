dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade']
print(dados)
dados['sexo'] = 'F'  # Redefiniu o 'M', não adicionou o 'F'
print(dados)

print(dados.values())  # Pedro, M
print(dados.keys())  # nome, idade, sexo
print(dados.items())  # values e keys

print('-=' * 50)
print('-=' * 50)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print('filme.items() é -->', filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
    # Pode colocar dicionarios dentro de uma lista, como lista locadora, por exemplo
print('\033[31m-=' * 50)
print('-=' * 50, '\033[m')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.values(), '\n', pessoas.items(), '\n', pessoas.keys())

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 50)  # MUDA E APAGA AS COISAS
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 66
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('\033[31m-=' * 50)
print('-=' * 50, '\033[m')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])  # Rio de Janeiro
print(brasil[0]['sigla'])  # RJ

print('\033[31m-=' * 50)
print('-=' * 50, '\033[m')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
