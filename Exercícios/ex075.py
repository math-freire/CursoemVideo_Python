a, b, c, d = map(int, input('Enter four numbers separated by space:\n').split())
nums = (a, b, c, d)

print(f'The number 9 appears {nums.count(9)} times.')

if 3 in nums:
    print(f'The number 3 appears at the #{nums.index(3)+1} position.')
else:
    print("\033[31mThe number 3 was not entered.\033[m")

print('The even numbers entered was: ', end='')

even_nums = ()
for i in nums:
    if i % 2 == 0:
        even_nums += i,
if even_nums != ():
    print(f'The even numbers were {even_nums}.')
else:
    print('You did not give me any even numbers.')
