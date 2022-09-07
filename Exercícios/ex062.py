r = int(input('Enter the arithmetic progression rate: '))
t1 = int(input('Enter the first term: '))
soma = 1
terms = None

while terms != 0:
    terms = int(input('How many terms do you want?'))
    count = 0
    while count < terms:
        if count == terms-1:
            print('{}'.format(t1))
        else:
            print('{} → '.format(t1), end='')
        soma += t1
        t1 += r
        count += 1
print('Soma:', soma)
