name = input('Enter your full name: ').strip().split()
print('The first name is {}.'.format(name[0]))
ln = name[::-1]
print('The last name is {}.'.format(ln[0]))

# we could just use print('The first name is {}.'.format(fn[-1]))
