dist = int(input('Enter the total distance for the travel: '))
if dist <= 200:
    price = dist * 0.5
else:
    price = dist * 0.45

print('The full price is R${}'.format(price))
