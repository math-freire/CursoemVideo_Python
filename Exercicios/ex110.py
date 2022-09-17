from utilidadesCeV import moeda
import my_codes

my_codes.titulo('MODULARIZAÇÃO - TABELA RESUMO', 50)
p = my_codes.r_float('Digite o preço: R$')
moeda.resumo(p, 80, 35)
my_codes.end_program()
