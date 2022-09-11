n = soma = 0
while n != 999:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    soma += n
print(f'The sum is {soma}.')
