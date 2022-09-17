from modulos import moeda
import my_codes

my_codes.titulo('MODULARIZAÇÃO', 30)
p = my_codes.r_float('Digite o preço (R$): ')
moeda.dobro(p, show=True)
moeda.metade(p, show=True)
moeda.aumentar(p, show=True)
moeda.diminuir(p, show=True)
my_codes.end_program()
