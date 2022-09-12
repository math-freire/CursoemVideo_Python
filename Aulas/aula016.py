# Tuplas nome = ('a','b','c','d') ou nome = 'a','b','c','d'
# TUPLAS SÃO IMUTÁVEIS
lanche = 'hamburguer', 'pudim', 'suco', 'pizza'
# ou lanche = ('hamburguer', 'pudim', 'suco', 'pizza')
print(lanche[-3])
print(lanche)

print('-='*30)
for comida in lanche:
    print(f'Irei comer {comida}')
print('-='*30)

for pos, comida in enumerate(lanche):
    print(f'Irei comer {comida} na posição {pos}')
print('-=' * 30)

for cont in range(0, len(lanche)):
    print(f'Comerei {lanche[cont]} na posição {cont}')
print('-=' * 30)

print(sorted(lanche)) # Deixa em ordem mas não altera a Tupla
print(lanche)
print('-=' * 30)

a = (2,4,6)
b = (5,6,7,8)
c = a + b # Concatena
print(c)
print(c.index(8)) # Onde está o 8