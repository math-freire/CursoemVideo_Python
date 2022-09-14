nums = []
for i in range(0, 3):
    nums.append([])
    for j in range(0, 3):
        nums[i].append(int(input(f'Valor para [{i}, {j}]: ')))

# Para imprimir no formato pedido em aula, mas for linha in nums print linha já resolveria
soma_par = soma_col3 = 0
for linha in nums:
    for flag, numero in enumerate(linha):
        print(f'[{numero:^5}]', end='')
        if numero % 2 == 0:
            soma_par += numero
        if flag == 2:
            soma_col3 += numero
    print()

print(f'Soma dos pares: {soma_par}')
print(f'Maior valor da segunda linha: {max(nums[1])}')
print(f'Soma da terceira coluna: {soma_col3}')
