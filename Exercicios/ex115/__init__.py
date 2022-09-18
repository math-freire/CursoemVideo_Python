from Exercicios import my_codes
from Exercicios.my_codes import yellow, endc, red, green


def menu():
    my_codes.titulo('MENU PRINCIPAL', 40)
    print(f'{yellow()}1 - {green()}Ver pessoas cadastradas{endc()}')
    print(f'{yellow()}2 - {green()}Cadastrar novas pessoas{endc()}')
    print(f'{yellow()}3 - {green()}Sair do sistema{endc()}')
    print(f'{yellow()}-' * 40, f'{endc()}')
    while True:
        try:
            x = int(input(f'{yellow()}Sua opção: {endc()}'))
            if x < 1 or x > 3:
                print(f'{red()}Entrada inválida! Favor digitar uma opção válida!{endc()}')
            else:
                break
        except ValueError:
            print(f'{red()}Entrada inválida! Favor digitar uma opção válida!{endc()}')
    return x


def ler_cadastro():
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    with open('cadastro.txt', 'r') as arquivo:
        teste = arquivo.readlines()
    for linha in teste:
        nome, idade = linha.strip().split(',')
        print(f'{nome:30}{idade} anos')


def criar_cadastro():
    print('-' * 40)
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    with open('cadastro.txt', 'a') as arquivo:
        nome = input('Digite o novo nome: ')
        idade = my_codes.r_int('Digite a idade: ')
        arquivo.write(f'\n{nome}, {idade}')
        print(f'{green()}Cadastro de {nome} efetuado com sucesso!{endc()}')
