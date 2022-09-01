g1 = float(input('Grade 1: '))
g2 = float(input('Grade 2: '))
m = (g1+g2)/2

if m < 5:
    print('Held back')
elif 5 <= m < 7:
    print('Recuperation')
else:
    print('Approved')
