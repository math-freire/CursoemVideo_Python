print('='*30)
print('\033[31mREGISTRATION PROGRAM')
print('Enter age 0 to end the program.\033[m')
print('='*30)


plus18 = men = under20w = 0
while True:
    while True:
        try:
            age = float(input('Age: '))
            break
        except ValueError:
            print('\033[31mYou need to enter a number. Please, try again.\033[m')
    if age == 0:
        break
    while True:
        sex = input('Sex [M/F]: ').strip().upper()
        if sex != 'M' and sex != 'F':
            print('\033[31mInvalid input.\033[m')
        else:
            break

    if age > 18:
        plus18 += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 20:
        under20w += 1

print('='*30)
print(f'{plus18} people over 18, {men} men registered and {under20w} women under 20.')
print('\033[32mThank you for using our services.')
