# number = 'abcde'
# while len(number) > 4:  # If greater than 9999
#     number = input('Enter a number between 1 and 9999: ')
#
# print("""
# Unit: {}
# Ten: {}
# Hundred: {}
# Thousand: {}""".format(number[3], number[2], number[1], number[0]))
# The method above open a large window for errors, it's best to do with int values.

num = int(input('Enter a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""
Unit: {}
Ten: {}
Hundred: {}
Thousand: {}""".format(u, d, c, m))
