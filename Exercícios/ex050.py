soma = 0
for i in range(0, 6):
    x = int(input('Enter number {}: '.format(i+1)))
    if x % 2 == 0:
        soma += x
print('The sum of the even elements entered is', soma)
