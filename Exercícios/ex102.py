from my_codes import titulo, end_program

def fatorial(n, process=False):
    """
    Prints the results of n! (n factorial) and has no return.
    :param n: Number for factorial calculation;
    :param process: True for printing the calculation and False to show only the result. It's False by default;
    :return: None.
    """

    if process is True:
        print(f'{n}! -> {n} x ', end='')
        for i in range(n - 1, 1, -1):
            print(f'{i} x ', end='')
            n *= i
        print(f'1 = {n}')
    else:
        aux = n
        for i in range(n, 0, -1): aux *= i
        print(f'{n}! = {aux}')


titulo('FATORIAL - PARAM OPCIONAL E DOCSTRING', (len('FATORIAL - PARAM OPCIONAL E DOCSTRING')+5))
fatorial(5, True)
fatorial(5, False)
fatorial(10, True)
fatorial(10, False)

print('~'*30)
help(fatorial)

end_program()

