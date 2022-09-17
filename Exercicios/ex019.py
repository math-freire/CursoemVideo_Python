from random import choice

a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Forth student: ')

# Lists
names = [a1, a2, a3, a4]

winner = choice(names)

print('The chosen student is {}.'.format(winner))
