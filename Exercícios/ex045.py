import random
import time

choice = int(input('\033[33m1- Pedra\033[m\n\033[34m2- Papel\033[m\n\033[35m3- Tesoura\033[m\n'))

pc_choice = random.randrange(1, 4)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)

print('=-'*15)
if pc_choice == 1:
    print('PC escolheu Pedra!')
elif pc_choice == 2:
    print('PC escolheu Papel!')
elif pc_choice == 3:
    print('PC escolheu Tesoura!')
print('=-'*15)

if choice == 1 and pc_choice == 3 or choice == 2 and pc_choice == 1 or choice == 3 and pc_choice == 2:
    print('You won')
elif choice == pc_choice:
    print('Draw')
else:
    print('You lost')

# Nice :)
