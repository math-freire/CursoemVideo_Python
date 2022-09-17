par, impar, nums = [], [], []
for i in range(0, 7):
    n = int(input(f'Digite o #{i+1} número: '))
    if n % 2 == 0: par.append(n)
    else: impar.append(n)
nums.append(sorted(par))
nums.append(sorted(impar))
print(f'Os valores pares são {nums[0]} e os ímpares são {nums[1]}.')
