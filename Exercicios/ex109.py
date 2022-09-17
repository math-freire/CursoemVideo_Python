from modulos import moeda
import my_codes

my_codes.titulo('MODULARIZAÇÃO - PARAM FORMATAÇÃO', 50)
p = my_codes.r_float('Digite o preço (R$): ')
moeda.dobro(p, show=True)
moeda.metade(p, show=True)
moeda.aumentar(p, show=True)
moeda.diminuir(p, show=True)

my_codes.titulo('SEM IMPRIMIR PELA FUNÇÃO', (len('SEM IMPRIMIR PELA FUNÇÃO')+6))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, f=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, f=True)}')
print(f'O valor atualizado é de {moeda.aumentar(p, f=True)}')
print(f'O valor atualizado é de {moeda.diminuir(p, f=True)}')
my_codes.end_program()
