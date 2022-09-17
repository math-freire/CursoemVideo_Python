from Exercícios import my_codes


def aumentar(x, show=True):
    """
    Retorna o valor passado acrescido pelo percentual desejado
    param x: Valor base
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado
    return: Total atualizado
    """
    y = my_codes.r_float('Digite o percentual de acréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Aumentando o valor de {x} por {y}% temos {x * (1 + (y / 100))}{my_codes.endc()}')
    return x * (1 + (y / 100))


def diminuir(x, show=True):
    """
    Retorna o valor passado diminuído pelo percentual desejado
    param x: Valor base
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado
    return: Total atualizado
    """
    y = my_codes.r_float('Digite o percentual de decréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Diminuindo o valor de {x} por {y}% temos {(x * (1 - (y / 100)))}{my_codes.endc()}')
    return x * (1 - (y / 100))


def metade(x, show=True):
    """
    Retorna a metade do valor informado
    param x: Valor inicial passado pelo usuário
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado
    return: Metade do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}A metade de {x} é {x/2}{my_codes.endc()}')
    return x / 2


def dobro(x, show=True):
    """
    Retorna o dobro do valor informado
    param x: Valor inicial passado pelo usuário
    param show: True para printar o valor de acréscimo e False para somente retornar o resultado
    return: Dobro do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}O dobro de {x} é {x*2}{my_codes.endc()}')
    return x * 2

























