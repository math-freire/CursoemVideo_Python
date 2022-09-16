from random import randint
from time import sleep
from my_codes import titulo, red, endc


def sorteia():
    list = []
    print('Sorteando 5 valores na lista: ', end='')
    for i in range(0, 5):
        x = randint(0, 10)
        print(f'{x} ', end='')
        list.append(x)
        sleep(.5)
    print('-> Pronto!')
    return list


def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de {red()}{lista}{endc()} obtemos {red()}{soma}{endc()}.")


titulo('FUNÇÃO SORTEIA E SOMA PAR', 40)
list_x = sorteia()
soma_par(list_x)
