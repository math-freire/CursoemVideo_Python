r = int(input('Enter the arithmetic progression rate: '))
t1 = int(input('Enter the first term: '))
count, soma = 1, 0

while count <= 10:
    if count == 10:
        print('{}'.format(t1))
    else:
        print('{} → '.format(t1), end='')
    soma += t1
    t1 += r
    count += 1
print('Soma:', soma)
