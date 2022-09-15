# Se aposenta depois de 35 anos de contribuição
from datetime import datetime
pessoa = {'nome': input('Nome: '),
          'idade': int(input('Ano de nascimento: ')),
          'CTPS': int(input('CTPS (0 se não tiver): '))}
ano = datetime.today().year
pessoa['idade'] = 2022 - pessoa['idade']

if pessoa['CTPS'] == 0:
    print(f"Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nCTPS: -")
else:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = 35 - (ano - pessoa['contratacao']) + pessoa['idade']

print('\033[1;31-'*20, '\033[m')
print(f"""Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
CTPS: {pessoa['CTPS']}
Data de contratação: {pessoa['contratacao']}
Salário: {pessoa['salario']}
Idade de aposentadoria: {pessoa['aposentadoria']}""")

