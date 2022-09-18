from Exercicios import ex115
from time import sleep

while True:
    key = ex115.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    sleep(.5)
    if key == 1:
        ex115.ler_cadastro()
    elif key == 2:
        ex115.criar_cadastro()
        sleep(1)
    elif key == 3:
        print(f'\033[31mSaindo do sistema. Até breve!\033[m')
        sleep(1)
        break