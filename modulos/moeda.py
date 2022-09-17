from Exercicios import my_codes


def moeda(x, show=False):
    """
    Retorna o número em formatação contábil
    param x: Valor a ser formatado
    return: Valor formatado
    param show: False para somente retornar e True para imprimir
    """
    if show:
        print(f'R${x:.2f}')
    return f'R${x:.2f}'


def aumentar(x, show=False, f=False):
    """
    Retorna o valor passado acrescido pelo percentual desejado. Se todos os parâmetros opcionais forem False, a função
    retorna somente o resultado da operação (float)
    param x: Valor base
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    param f: True para retornar o valor literal formatado em contábil
    return: Total atualizado
    """
    y = my_codes.r_float('Digite o percentual de acréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Aumentando o valor de {moeda(x)} por {y}% temos {moeda(x * (1 + (y / 100)))}'
              f'{my_codes.endc()}')
    if f:
        return f'{moeda(x * (1 + (y / 100)))}'
    else:
        return x * (1 + (y / 100))


def diminuir(x, show=False, f=False):
    """
    Retorna o valor passado diminuído pelo percentual desejado. Se todos os parâmetros opcionais forem False, a função
    retorna somente o resultado da operação (float)
    param x: Valor base
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    param f: True para retornar o valor literal formatado em contábil
    return: Total atualizado
    """
    y = my_codes.r_float('Digite o percentual de decréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Diminuindo o valor de {moeda(x)} por {y}% temos {moeda((x * (1 - (y / 100))))}'
              f'{my_codes.endc()}')
    if f:
        return f'{moeda(x * (1 - (y / 100)))}'
    else:
        return x * (1 - (y / 100))


def metade(x, show=False, f=False):
    """
    Retorna a metade do valor informado
    param x: Valor inicial passado pelo usuário
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    param f: True para retornar o valor literal formatado em contábil
    return: Metade do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}A metade de {moeda(x)} é {moeda(x/2)}{my_codes.endc()}')
    if f:
        return f'{moeda(x/2)}'
    else:
        return x / 2


def dobro(x, show=False, f=False):
    """
    Retorna o dobro do valor informado
    param x: Valor inicial passado pelo usuário
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    param f: True para retornar o valor literal formatado em contábil
    return: Dobro do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}O dobro de {x} é {x * 2}{my_codes.endc()}')
    if f:
        return f'{moeda(x*2)}'
    else:
        return x * 2
