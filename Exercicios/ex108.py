from modulos import moeda
import my_codes

my_codes.titulo('MODULARIZAÇÃO - FORMATAÇÃO MOEDA', 50)
p = my_codes.r_float('Digite o preço (R$): ')
moeda.dobro(p, show=True)
moeda.metade(p, show=True)
moeda.aumentar(p, show=True)
moeda.diminuir(p, show=True)

my_codes.titulo('SEM IMPRIMIR PELA FUNÇÃO', (len('SEM IMPRIMIR PELA FUNÇÃO')+6))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O valor atualizado é de {moeda.moeda(moeda.aumentar(p))}')
my_codes.end_program()
