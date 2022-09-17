from my_codes import titulo, end_program, endc, red


def leiaint():
    while True:
        try:
            n = int(input('Digite um número: '))
            break
        except ValueError:
            print(f'{red()}Erro! Digite um número inteiro!{endc()}')
    return n


titulo('VALIDA INT', 20)
n = leiaint()
print(f'O número inteiro digitado foi {n}.')
end_program()
