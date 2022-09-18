from Exercicios import ex115

key = None
while key != 3:
    key = ex115.menu()
    if key == 1:
        print('-'*40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-' * 40)
        with open('cadastro.txt', 'r') as arquivo:
            teste = arquivo.readlines()
        for linha in teste:
            nome, idade = linha.strip().split(',')
            print(f'{nome:30}{idade} anos')

    elif key == 2:
        print('-' * 40)
        print('NOVO CADASTRO'.center(40))
        print('-' * 40)
        with open('cadastro.txt', 'a') as arquivo:
            nome = input('Digite o novo nome: ')
            idade = ex115.my_codes.r_int('Digite a idade: ')
            arquivo.write(f'\n{nome}, {idade}')
    elif key == 3:
        arquivo.close()
