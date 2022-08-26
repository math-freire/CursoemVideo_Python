name = input('Enter your full name: ')
fn = name.split()
print('The first name is {}.'.format(fn[0]))
ln = fn[::-1]
print('The last name is {}.'.format(ln[0]))

# we could just use print('The first name is {}.'.format(fn[-1]))
