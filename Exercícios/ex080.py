nums = []
for i in range(1, 6):
    n = int(input(f'Please, enter number \033[31m#{i}\033[m: '))
    if i == 1:
        print(f'\033[32m{n} is the first value added in the list.\033[m')
        nums.append(n)
    elif max(nums) <= n:
        nums.append(n)
        print(f'\033[32m{n} was added at the end of the list.\033[m')
    elif min(nums) >= n:
        nums.insert(0, n)
        print(f'\033[32m{n} was added in the beginning of the list.\033[m')
    else:
        for j in range(1, 6):
            if nums[j] >= n:
                nums.insert(j, n)
                print(f'\033[32m{n} was added at position #{j}\033[m')
                break
print(f'The list you entered was {nums}.')
