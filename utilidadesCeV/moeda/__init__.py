from Exercicios import my_codes


def moeda(x, show=False):
    """
    Retorna o número em formatação contábil
    :param x: Valor a ser formatado
    :param show: False para somente retornar e True para imprimir
    :return: Valor formatado
    """
    if show:
        print(f'R${x:.2f}')
    return f'R${x:.2f}'


def aumentar(x, show=False, f=False, perc=0):
    """
    Retorna o valor passado acrescido pelo percentual desejado. Se todos os parâmetros opcionais forem False, a função
    retorna somente o resultado da operação (float)
    :param x: Valor base
    :param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    :param f: True para retornar o valor literal formatado em contábil
    :param perc: Se o usuário quiser entrar a porcentagem de aumento
    :return: Total atualizado
    """
    if perc == 0:
        perc = my_codes.r_float('Digite o percentual de acréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Aumentando o valor de {moeda(x)} por {perc}% temos {moeda(x * (1 + (perc / 100)))}'
              f'{my_codes.endc()}')
    if f:
        return f'{moeda(x * (1 + (perc / 100)))}'
    else:
        return x * (1 + (perc / 100))


def diminuir(x, show=False, f=False, perc=0):
    """
    Retorna o valor passado diminuído pelo percentual desejado. Se todos os parâmetros opcionais forem False, a função
    retorna somente o resultado da operação (float)
    :param x: Valor base
    :param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    :param f: True para retornar o valor literal formatado em contábil
    :param perc: Se o usuário quiser entrar a porcentagem de aumento
    :return: Total atualizado
    """
    if perc == 0:
        perc = my_codes.r_float('Digite o percentual de decréscimo: ')
    if show:
        print(f'{my_codes.yellow()}Diminuindo o valor de {moeda(x)} por {perc}% temos {moeda((x * (1 - (perc / 100))))}'
              f'{my_codes.endc()}')
    if f:
        return f'{moeda(x * (1 - (perc / 100)))}'
    else:
        return x * (1 - (perc / 100))


def metade(x, show=False, f=False):
    """
    Retorna a metade do valor informado
    :param x: Valor inicial passado pelo usuário
    :param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    :param f: True para retornar o valor literal formatado em contábil
    :return: Metade do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}A metade de {moeda(x)} é {moeda(x / 2)}{my_codes.endc()}')
    if f:
        return f'{moeda(x / 2)}'
    else:
        return x / 2


def dobro(x, show=False, f=False):
    """
    Retorna o dobro do valor informado
    :param x: Valor inicial passado pelo usuário
    :param show: True para printar o valor de acréscimo e False para somente retornar o resultado (já formatado)
    :param f: True para retornar o valor literal formatado em contábil
    :return: Dobro do valor passado na variável x
    """
    if show:
        print(f'{my_codes.yellow()}O dobro de {x} é {x * 2}{my_codes.endc()}')
    if f:
        return f'{moeda(x * 2)}'
    else:
        return x * 2


def resumo(x, a, r):
    title = 'RESUMO DO VALOR'
    my_codes.titulo(f'{title}', 50)
    print(f"""{'Preço analisado:':<30}{moeda(x)}
{'Dobro do preço:':<30}{dobro(x, f=True)}
{'Metade do preço:':<30}{metade(x, f=True)}
{f'{a}% de aumento:':<30}{aumentar(x, f=True, perc=a)}
{f'{r}% de redução:':<30}{diminuir(x, f=True, perc=r)}""")
    print('\033[1;33m-' * 50, '\033[m')
