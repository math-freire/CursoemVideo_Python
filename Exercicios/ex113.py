from my_codes import red, endc, titulo, end_program


def r_int(p='Enter an integer: '):
    while True:
        try:
            x = int(input(p))
            return x
        except ValueError as error:
            print(f'{red()}Invalid input! Please enter an integer number.{endc()}')
        except KeyboardInterrupt:
            print(f'\n{red()}User choose to skip this entry!{endc()}')
            break


def r_float(p='Enter a real number: '):
    while True:
        try:
            x = float(input(p))
            return x
        except ValueError as error:
            print(f'{red()}Invalid input! Please enter a real number.{endc()}')
        except KeyboardInterrupt:
            print(f'\n{red()}User choose to skip this entry!{endc()}')
            break


titulo('Treating erros', 50)
i = r_int('Integer: ')
f = r_float('Float: ')
print('Teste')
print(f'The integer number is {i}')
print(f'The float number is {f}')
