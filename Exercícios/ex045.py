import random

choice = int(input('1- Pedra\n2- Papel\n3- Tesoura\n'))

pc_choice = random.randrange(1, 4)
print(pc_choice)
if choice == 1 and pc_choice == 3 or choice == 2 and pc_choice == 1 or choice == 3 and pc_choice == 2:
    print('You won')
elif choice == pc_choice:
    print('Draw')
else:
    print('You lost')
