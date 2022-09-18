from Exercicios import my_codes
from Exercicios.my_codes import yellow, endc, red, green
from time import sleep


def menu(lista):
    my_codes.titulo('MENU PRINCIPAL', 40)
    c = 1
    for item in lista:
        print(f'{yellow()}{c} - {green()}{item}{endc()}')
        c += 1
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
        sleep(.3)
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
        sleep(.2)
        print(f'{green()}Cadastrando {nome}...{endc()}')
        sleep(1)
        print(f'{green()}Cadastro de {nome} efetuado com sucesso!{endc()}')
