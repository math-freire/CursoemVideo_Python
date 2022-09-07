entry = None
count, soma = 0, 0
while entry != 999:
    entry = int(input('Enter a number: '))
    if entry != 999:
        soma += entry
        count += 1
print('You entered {} numbers and the sum between them is {}'.format(count, soma))
