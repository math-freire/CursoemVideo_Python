r = int(input('Enter the arithmetic progression rate: '))
t1 = int(input('Enter the first term: '))
soma = 1
terms, termsCount = None, 0

while terms != 0:
    terms = int(input('How many terms do you want? '))
    termsCount += terms
    count = 0
    while count < terms:
        print('{} → '.format(t1) if count != terms-1 else '{} → Pause\n'.format(t1), end='')
        soma += t1
        t1 += r
        count += 1
print('\n\033[32mSum:\033[0m {}\n\033[32mNumber of terms:\033[0m {}'.format(soma, termsCount))
