wage = float(input('Enter your wage: '))

if wage > 1250:
    wage *= 1.1
else:
    wage *= 1.5

print('Your new wage is R${:.2f}'.format(wage))
