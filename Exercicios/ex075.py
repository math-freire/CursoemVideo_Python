a, b, c, d = map(int, input('Enter four numbers separated by space:\n').split())
nums = (a, b, c, d)

print(f'The number 9 appears {nums.count(9)} times.')
print(f'The number 3 appears at the #{nums.index(3)+1} position.' if 3 in nums else "\033[31mThe number 3 was not "
                                                                                    "entered.\033[m")
print('The even numbers entered was: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')

