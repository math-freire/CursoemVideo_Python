dias = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        try:
            n = int(input('Which number do you want (1-20): '))
            if n > 20 or n < 1:
                print('\033[31mNumber out of bounds. Please, try again.\033[m')
            else:
                break
        except ValueError:
            print('\033[31mInvalid input. Please, enter a number.\033[m')
    print(f'\033[34m{n} in full in portuguese is {dias[n - 1]}.\033[m')

    if (input('Type N to end the program or just enter to continue\n')).upper() == 'N':
        break
