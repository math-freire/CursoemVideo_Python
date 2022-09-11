def getPrice():
    while True:
        try:
            x = float(input('Price: '))
            break
        except ValueError:
            print('\033[31mYou need to enter a number. Please, try again.\033[m')
    return x


print('\033[1;31m-='*20)
print(f"{'Lojas Kudossi':^35}")
print('-='*20, '\033[m')
print('\033[31mEnter a negative value to end the program')
print('-'*40, '\033[m')

total = plus1k = 0
cheaper_name = cheaper_price = None
while True:
    name = input('What product is this?\n').strip().upper()
    price = getPrice()
    if price < 0:
        break

    total += price
    if total > 1000:
        plus1k += 1
    if cheaper_price is None:
        cheaper_name = name
        cheaper_price = price
    else:
        if price < cheaper_price:
            cheaper_name = name
            cheaper_price = price

print(f'The total is \033[31m{total:.2f}\033[m, \033[31m{plus1k}\033[m product(s) costs more than 1k and '
      f'\033[31m{cheaper_name}\033[m was the cheaper product, costing R$\033[31m{cheaper_price:.2f}\033[m')

