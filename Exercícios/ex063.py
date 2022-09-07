n = int(input('How many terms of the Fibonacci sequence do you want to see?\n'))

x0, x1 = 0, 1
print('0 → ', end='')
count = 1

while count != n:
    if count == 1:
        print('1 → ', end='')
    elif count == n - 1:
        print('{}'.format(x0 + x1))
    else:
        print('{} → '.format(x0 + x1), end='')
        z = x1
        x1 = x0 + x1
        x0 = z
    count += 1
