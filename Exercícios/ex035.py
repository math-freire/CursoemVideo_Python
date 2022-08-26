a = float(input('Line 1: '))
b = float(input('Line 2: '))
c = float(input('Line 3: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('It can be a triangle!')
else:
    print('Not a triangle!')
