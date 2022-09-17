from time import sleep
from my_codes import red, titulo, end_program, endc


def my_help():
    while True:
        sleep(.5)
        print(f'{red()}To end the program, type "END".{endc()}')
        func = input(f'{red()}Function or Library ➤➤➤ {endc()}').strip()
        if func.upper().strip() == 'END':
            break
        titulo(f'HELP MANUAL FOR {func.upper()}', (len(f'HELP MANUAL FOR {func.upper()}')+6))
        sleep(1.5)
        print('\033[32m', end='')
        help(func)
        print('\033[m', end='')


titulo('HELP PROGRAM FUNCTION', 50)
my_help()
end_program()
