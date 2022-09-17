from random import randint
nums = tuple(randint(0, 100) for _ in range(5))
print(f'The generated numbers are {nums}.')
print(f'The greatest value is {max(nums)}.')
print(f'The lowest value is {min(nums)}.')
