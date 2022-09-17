nums = []
evens = []
odds = []
count = 1
while True:
    n = int(input(f'Enter number #{count}: '))
    nums.append(n)
    if n % 2 == 0: evens.append(n)
    else: odds.append(n)
    flag = '.'
    while flag not in 'YyNn':
        flag = input('Continue [Y/N]?')
    if flag in 'Nn':
        break
    count += 1

print(f'Your numbers are {nums}.')
print(f'The even numbers are {evens}.')
print(f'The odd numbers are {odds}.')
