import time


def titulo(st, x):
    print('\033[1;33m-' * x)
    print(f'{st:^{x}}')
    print('-' * x, '\033[m')


def end_program():
    print()
    time.sleep(1)
    start_red()
    time.sleep(.5)
    print(f"{'SHUTTING DOWN':-^40}")
    time.sleep(.5)
    end_color()
    time.sleep(1)


def start_red():
    print('\033[1;31m', end='')


def start_yellow():
    print('\033[1;33m', end='')


def end_color():
    print('\033[m', end='')
