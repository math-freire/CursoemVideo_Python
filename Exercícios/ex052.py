n = int(input('Enter a number: '))
total = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\033[93m', end='')
        total += 1
    else:
        print('\033[36m', end='')
    print('{} '.format(i), end='')
print('\n\033[0mThe number {} was divided {} times.'.format(n, total), end=' ')

if total == 2:
    print("So it \033[92mis a prime number\033[0m!")
else:
    print("So it \033[91misn't a prime number\033[0m!")
