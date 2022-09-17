def leiaDinheiro(p='Digite um valor: '):
    while True:
        n = input(p).replace(',', '.').strip()
        if n.isalpha() or n.strip() == '':
            print(f'\033[1;31mERRO! <{n}> não é válido!')
        else:
            n = float(n)
            break
    return n