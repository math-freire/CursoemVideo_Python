vel = int(input('Tell me the speed (Km/h): '))
if vel > 80:
    price = (vel - 80) * 7
    print('FINED, YOU OWN ME ${}'.format(price))
else:
    print('KEEP GOING')
