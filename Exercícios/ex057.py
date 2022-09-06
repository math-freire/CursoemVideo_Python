sexo = None
while sexo != 'M' and sexo != 'F':
    sexo = input('Enter your gender [M/F]: ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Invalid input!')

if sexo == 'M':
    print('\033[32mWelcome, sir!')
else:
    print('\033[35mWelcome, madam!')
