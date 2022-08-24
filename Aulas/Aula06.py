n1 = int(input('Enter a value: '))
n2 = int(input('Enter another value: '))
s = n1 + n2

print('A soma entre {} e {} vale {}!'.format(n1, n2, s))

# Bool has to be True or False (capitalized)
print(type(n1))

# n0 = input('This number will not be casted: ')
# print(type(n0))

smt = input('Type something: ')
print('Is numeric: {}'.format((smt.isnumeric())))
print('Is alphanumeric: {}'.format(smt.isalnum()))
print('Is decimal: {}'.format(smt.isdecimal()))
print('Is a lot of other things (or it is not')


