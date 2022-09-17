from my_codes import titulo, end_program


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


titulo('PARAM OPCIONAL - JOGADOR E GOLS', (len('PARAM OPCIONAL - JOGADOR E GOLS')+5))
nome = input('Nome: ')
gols = input('Gols: ')

gols = int(gols) if gols.isnumeric() else 0

if nome:
    ficha(nome, gols)
else:
    ficha(gols=gols)

end_program()
