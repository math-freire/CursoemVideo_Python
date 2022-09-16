import time


def titulo(st, x):
    print('\033[1;33m-' * x)
    print(f'{st:^{x}}')
    print('-' * x, '\033[m')


def end_program():
    print()
    time.sleep(1)
    red()
    time.sleep(.5)
    print(f"{'SHUTTING DOWN':-^40}")
    time.sleep(.5)
    endc()
    time.sleep(1)


def red():
    return '\033[1;31m'


def yellow():
    return '\033[1;33m'


def endc():
    return '\033[m'
