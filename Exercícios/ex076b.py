shopping_list = ('Ladder', 50, 'Stair', 100, 'Staircase', 234, 'Escalator', 31, 'Bucket', 25)

print('\033[1;31m-'*40)
print(f"{'Shopping List':^40}")
print('-'*40, '\033[m')
for pos in range(0, len(shopping_list)):
    if pos % 2 == 0:
        print(f'{shopping_list[pos]:.<30}', end='')
    else:
        print(f'R${shopping_list[pos]:>7.2f}')
print('\033[1;31m-'*40, '\033[m')
