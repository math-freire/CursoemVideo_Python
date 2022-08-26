import random

rn = random.randrange(0, 6)
num = int(input('State a number between 0 and 5: '))

print('PC Number: {}'.format(rn))
if rn == num:
    print('Congrats! You are right.')
else:
    print('You are not that smart, huh?')
