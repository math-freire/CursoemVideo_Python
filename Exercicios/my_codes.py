import time


def titulo(st, x):
    print('\033[1;33m-' * x)
    print(f'{st:^{x}}')
    print('-' * x, '\033[m')


def end_program():
    print()
    time.sleep(1)
    print(f"{red()}{'SHUTTING DOWN':-^40}{endc()}")
    time.sleep(1)


def red():
    return '\033[1;31m'


def yellow():
    return '\033[1;33m'


def green():
    return '\033[1;32m'


def endc():
    return '\033[m'


def r_int(frase='Enter an integer: '):
    while True:
        try:
            x = int(input(frase))
            break
        except ValueError:
            print(f'{red()}Invalid input! Please, enter an integer value.{endc()}')
    return x


def r_float(frase='Enter a number: '):
    while True:
        try:
            x = int(input(frase))
            break
        except ValueError:
            print(f'{red()}Invalid input! Please, enter a number.{endc()}')
    return x
