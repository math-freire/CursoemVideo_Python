nums = []
for i in range(0, 3):
    for j in range(0, 3):
        nums.append(int(input(f'Valor para [{i}, {j}]: ')))

for flag, i in enumerate(nums):
    print(f'[ {i:^10} ]', end='')
    if (flag + 1) % 3 == 0:
        print()
