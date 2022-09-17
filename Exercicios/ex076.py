shopping_list = ('Ladder', '50', 'Stair', '100', 'Staircase', '23234475', 'Escalator', '2135', 'Bucket', '25')

space = 50
print('\033[1;31m-'*space)
print(f"{'Shopping List':^{space}}")
print('-'*space, '\033[m')

for i in range(0, len(shopping_list), 2):
    print(f'{shopping_list[i]}' + '.' * (space-len(shopping_list[i]) - (len(shopping_list[i+1])+5)), end='')
    print(f'R${int(shopping_list[i+1]):.2f}')

print('\033[1;31m-'*space, '\033[m')
