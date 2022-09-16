from time import sleep

import my_codes


def maior(*num):
    numbers = num
    my_codes.start_red()
    print('Analyzing...')
    my_codes.end_color()
    sleep(.2)
    print('You entered: ', end='')
    for number in numbers: print(f'{number} ', end='')
    print(f'\nThere were {len(numbers)} values.')
    try:
        print(f'The greatest value is {max(numbers)}.')
    except ValueError:
        print('The are no max.')
    print('-'*30)
    sleep(1)


my_codes.titulo('DESEMPACOTAMENTO - MAIOR', 40)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

my_codes.end_program()
