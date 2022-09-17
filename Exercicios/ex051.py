t1 = int(input('Enter the first number: '))
rate = int(input('Enter the rate of the AP: '))
for i in range(0, 10):
    print('\033[34mPosition \033[35m#{}\033[0m = \033[36m{}'.format(i+1, t1))
    t1 += rate
