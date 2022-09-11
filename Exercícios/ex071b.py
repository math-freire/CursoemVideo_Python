print('\033[1;31m-='*20)
print(f"{'Banking Account':^37}")
print('-='*20, '\033[m')

# value = int(input('How much do you want to withdraw: '))
value = 987654321
bill, n_bills = 50, 0
while True:
    if value >= bill:
        value -= bill
        n_bills += 1
    else:
        if n_bills > 0:
            print(f'{n_bills} ${bill} bills')
        if bill == 50:
            bill = 20
        if bill == 20:
            bill = 10
        if bill == 10:
            bill = 1
        n_bills = 0
        if value == 0:
            break
print('\033[1;31m-='*20, '\033[m')
print('Thank you for using our services. See you later.')
