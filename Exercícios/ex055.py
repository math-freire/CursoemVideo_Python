larger, smaller = 0, 999
for i in range(0, 5):
    w = float(input('Weight #{}: '.format(i + 1)))
    if w > larger:
        larger = w
    elif w < smaller:
        smaller = w
print('The larger one weighs {} and the smaller {}.'.format(larger, smaller))
#  We could use a list = [] and keep the weights values so after the for loop we use list.sort() to sort in ascending
#  order, then we print the position #0 and #n-1


