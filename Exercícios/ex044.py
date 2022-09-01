price = float(input('Price: '))
pay = input('1- Dinheiro\n2- Cartão a vista\n3- Cartão em 2x\n4- Cartão em 3x ou mais\n')

if pay == 1:
    print('Price: {:.2f}'.format(price * 0.9))
elif pay == 2:
    print('Price: {:.2f}'.format(price * 0.95))
elif pay == 3:
    print('Price: {:.2f}'.format(price))
else:
    print('Price: {:.2f}'.format(price * 0.8))

