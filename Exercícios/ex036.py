vc = float(input('Enter the house price: '))
wage = float(input('Enter your wage: '))
time = float(input('How many years to pay: '))

cost = vc/(time*12)

if cost <= wage * 0.3:
    print('Your home loan was accepted!')
    print('Installments: {:.2f}'.format(cost))
else:
    print('Your home loan was denied!')

