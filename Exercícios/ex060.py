n = int(input('State a number: '))
res = 1
print_aux = n

while n != 0:
    res *= n
    n -= 1

print(print_aux, end='')
while print_aux != 1:
    print_aux -= 1
    print(' \033[36m*\033[0m {}'.format(print_aux), end='')
print(' =\033[1;33m', res)
