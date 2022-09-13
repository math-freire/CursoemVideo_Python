expression = list(input('Enter an expression:\n'))
print('-='*30)
a = b = 0  # a = opened, b = closed
for item in expression:
    if item == '(': a += 1
    elif item == ')': b += 1
    if b > a:
        break
if a != b: print('\033[31mSomething is wrong!\033[m')
else: print('\033[32mEverything is working fine!\033[m')