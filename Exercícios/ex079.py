count = int(input('\033[32mHow many numbers do you want to enter?\n\033[m'))
nums = []
for i in range(1, count+1):
    n = int(input(f'Please, enter number \033[31m#{i}\033[m: '))
    if n not in nums:
        nums.append(n)
print(f'In ascending order, the numbers are {sorted(nums)}')
