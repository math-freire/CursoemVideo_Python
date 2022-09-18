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
