from Exercicios import ex115

key = None
while key != 3:
    key = ex115.menu()
    if key == 1:
        ex115.ler_cadastro()
    elif key == 2:
        ex115.criar_cadastro()

