import sys


def menu():
    print("""\033[35m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\033[0m""")


print('\033[1;32m=-' * 10)
print('C A L C U L A T O R')
print('=-' * 10, end='\033[0m\n')

n1 = float(input('\033[35mNumber 1: '))
n2 = float(input('Number 2: \033[0m'))
print('\033[1;32m=-\033[0m' * 10)

key = None
result = None
while key != 0:
    menu()
    key = int(input('\033[1;32mOption: \033[0m'))
    print('\033[1;32m', end='')  # Green
    if key == 1:
        print('The sum of {} and {} is equals to {}'.format(n1, n2, n1+n2))
    elif key == 2:
        print('The multiplication of {} and {} is equals to {}'.format(n1, n2, n1 * n2))
    elif key == 3:
        if n1 > n2:
            print('{} is greater than {}'.format(n1, n2))
        else:
            print('{} is greater than {}'.format(n2, n1))
    elif key == 4:
        n1 = float(input('\033[35mNumber 1: '))
        n2 = float(input('Number 2: \033[0m'))
    elif key == 5:
        print('Thank you for using our services!')
        sys.exit()
    else:
        print('\033[31mPlease enter a valid input.\033[0m')
