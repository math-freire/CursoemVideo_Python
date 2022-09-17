n1 = int(input('Integer 1: '))
n2 = int(input('Integer 2: '))

if n1 == n2:
    print('Equals')
elif n1 < n2:
    print('{} greater than {}'.format(n2, n1))
else:
    print('{} greater than {}'.format(n1, n2))
