nums = []
for flag, i in enumerate(range(0, 5)):
    nums.append(int(input(f'Enter number #{flag+1}: ')))
print('~'*30)
print(f'You entered {nums}.')

if nums.count(max(nums)) == 1:
    print(f'The greatest value is {max(nums)} at position {nums.index(max(nums))+1}')
else:
    print(f'The greatest value is {max(nums)} at positions', end=' ')
    for flag, number in enumerate(nums):
        if number == max(nums):
            print(f'{flag+1}...', end='')
    print('')

if nums.count(min(nums)) == 1:
    print(f'The lowest value is {min(nums)} at position {nums.index(min(nums))+1}')
else:
    print(f'The lowest value is {min(nums)} at positions', end=' ')
    for flag, number in enumerate(nums):
        if number == min(nums):
            print(f'{flag+1}...', end='')
