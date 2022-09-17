import random
count = 0
while True:
    print('\033[34m=\033[m' * 30)
    pc = random.randint(0, 100)
    print("Let's play even or odd!")
    n = int(input('Enter a number: '))
    while True:
        choice = input('Choose even or odd [E/O]: ').strip().upper()
        if choice == 'E' or choice == 'O':
            break
        else:
            print('\033[31mInvalid input, please try again.\033[m')

    print('\033[34m=\033[m'*30)

    if (n + pc) % 2 == 0:
        res = 'E'
        print(f'You chose {n} and the computer chose {pc}, the total is {n + pc}, which is even.')
    else:
        res = 'O'
        print(f'You chose {n} and the computer chose {pc}, the total is {n + pc}, which is odd.')

    if res != choice:
        print('\033[31mYou lost!\033[m')
        break
    else:
        print("\033[32mCongrats! You won.\033[m2\nLet's play again.")
        count += 1

print(f'\n\033[35mThe game is over and you won {count} times.')
