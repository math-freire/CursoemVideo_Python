dias = int(input('How many days was the car rented? '))
km = int(input('How many kilometers was the car drove for? '))

total = dias * 60 + 0.15 * km

print('The total cost for the rent is {:.2f}.'.format(total))

print(type(total))

