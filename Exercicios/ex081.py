nums = []
count = 1
while True:
    while True:
        try:
            n = int(input(f'Please, enter number \033[31m#{count}\033[m: '))
            nums.append(n)
            break
        except ValueError:
            print('\033[31mInvalid input, please enter a number.\033[m')

    flag = '.'
    while flag not in 'YyNn':
        flag = input('Continue [Y/N]? ')
    if flag in 'Nn': break
    else: count += 1

print(f'You entered \033[31m{len(nums)} numbers.\033[m')
print(f'In \033[31mdescending order\033[m, the numbers are \033[31m{sorted(nums, reverse=True)}\033[m.')
if 5 in nums:
    print(f'The number \033[31m5 is in the list\033[m at \033[31mposition {nums.index(5)+1}\033[m.')
else:
    print('\033[31mThe number 5 is not in the list!\033[m')
