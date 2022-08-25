name = input('Enter your full name: ')
print(name.upper())
print(name.lower())

n2 = ''.join(name.split())
print('{} letters in your name without spaces.'.format(len(n2)))

n2 = (name.split())
print('{} letters in your first name.'.format(len(n2[0])))

