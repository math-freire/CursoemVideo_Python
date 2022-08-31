vc = float(input('Enter the house price: '))
wage = float(input('Enter your wage: '))
time = float(input('How many years to pay: '))

cost = vc / 12 * time

if cost > wage * 0.3:
    print('Your home loan was denied!')
else:
    print('Your home loan was accepted!')