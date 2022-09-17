n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
n3 = int(input('Number 3: '))

if n1 > n2:
    if n1 > n3:
        print('{} is the largest number.'.format(n1))
        if n2 < n3:
            print('{} is the smallest number.'.format(n2))
        elif n3 < n2:
            print('{} is the smallest number.'.format(n3))
    else:
        print('{} is the largest number.'.format(n3))
        if n1 < n2:
            print('{} is the smallest number.'.format(n1))
        elif n2 < n1:
            print('{} is the smallest number.'.format(n2))
elif n3 > n2:
    print('{} is the largest number.'.format(n3))
    if n1 < n2:
        print('{} is the smallest number.'.format(n1))
    elif n2 < n1:
        print('{} is the smallest number.'.format(n2))
else:
    print('{} is the largest number.'.format(n2))
    if n1 < n3:
        print('{} is the smallest number.'.format(n1))
    elif n3 < n1:
        print('{} is the smallest number.'.format(n3))
