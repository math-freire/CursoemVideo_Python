from math import sqrt, ceil
import random

# num = int(input("Enter a number: "))
num = 34.2
sqrt = sqrt(num)
# If we just import math without from, we need to use math.sqrt(num)

print('Square root of {} is {}'.format(num, sqrt))
print('Square root ceil of {} is {}'.format(num, ceil(sqrt)))

# About random
num2 = random.randint(1, 10)
print('\nRandom int from 1 to 10: {}'.format(num2))
