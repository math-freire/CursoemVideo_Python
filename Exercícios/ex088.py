from random import randint
from time import sleep

print('-'*30)
print(f"{'MEGA SENA':^30}")
print('-'*30)
n = int(input('How many do you want to do: '))
print('^'*30)


for i in range(n):
    bet = []
    for j in range(6):
        x = randint(0, 100)
        if j == 0: bet.append(x)
        else:
            if x not in bet:
                bet.append(x)
            else:
                while x in bet:
                    x = randint(0, 100)
                bet.append(x)
    sleep(.5)
    print(f'Play #{i+1}: {bet}')
    print('-' * 30)


