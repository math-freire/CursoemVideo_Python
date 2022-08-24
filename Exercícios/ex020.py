from random import shuffle

a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Forth student: ')

# Lists
group = [a1, a2, a3, a4]
shuffle(group)

print('The chosen student is {}.'.format(group))
