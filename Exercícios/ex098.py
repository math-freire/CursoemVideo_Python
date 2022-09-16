import my_codes
from time import sleep


def counter(start, end, step):
    my_codes.start_red()
    print(f'Couting from {start} to {end} with step {step}')
    my_codes.end_color()
    if step == 0: step = 1
    if start > end and step > 0: step = -step

    if end < 0: end += -1
    else: end += 1
    for i in range(start, end, step):
        sleep(.3)
        print(f'{i}', end=' ')
    sleep(.3)
    print('-> Done.')


my_codes.titulo('CONTADOR', 20)
counter(1, 10, 1)
counter(10, 0, 2)
my_codes.start_yellow()
print("Now it's your time to choose how it's done!")
a = int(input('Start: '))
b = int(input('End: '))
c = int(input('Step: '))
my_codes.end_color()
counter(a, b, c)
