larger, smaller = 0, 0
for i in range(0, 5):
    w = float(input('Weight #{}: '.format(i + 1)))
    if i == 0:
        larger = w
        smaller = w
    else:
        if w > larger:
            larger = w
        elif w < smaller:
            smaller = w
print('The \033[91mlarger one weighs {}\033[0m and \033[92mthe smaller {}\033[0m.'.format(larger, smaller))
#  We could use a list = [] and keep the weights values so after the for loop we use list.sort() to sort in ascending
#  order, then we print the position #0 and #n-1


