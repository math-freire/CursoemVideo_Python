import time


def titulo(st, x):
    print('\033[1;33m-' * x)
    print(f'{st:^{x}}')
    print('-' * x, '\033[m')


def end_program():
    print()
    time.sleep(1)
    print('\033[1;33m-' * 40)
    time.sleep(.5)
    print(f"{'SHUTTING DOWN':-^40}")
    time.sleep(.5)
    print('-' * 40, '\033[m')
    time.sleep(1)


