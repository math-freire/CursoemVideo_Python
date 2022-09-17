smt = input('Type something: ')
print('Is numeric: {}'.format((smt.isnumeric())))
print('Is alphanumeric: {}'.format(smt.isalnum()))
print('Is decimal: {}'.format(smt.isdecimal()))
print('The primitive type: {}'.format(type(smt)))  # Will be str 'cause of the input method
print('Is alphabetic: {}'.format(smt.isalpha()))
print('Is uppercase: {}'.format(smt.isupper()))
print('Is lowercase: {}'.format(smt.islower()))
print('Is capitalized: {}'.format(smt.istitle()))

# Or just use it right away with the variable
print('Is lowercase:', smt.islower())
