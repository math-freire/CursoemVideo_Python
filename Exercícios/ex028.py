import random
from time import sleep

rn = random.randrange(0, 5)
num = int(input('State a number between 0 and 5: '))

# print('PC Number: {}'.format(rn))

print("PROCESSANDO...")
sleep(2)
if rn == num:
    print('Congrats! You are right.')
else:
    print('You are not that smart, huh?')
