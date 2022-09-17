from datetime import date

y = date.today().year
offage, underage = 0, 0
for i in range(0, 7):
    birth = int(input('Enter person {} birth year: '.format(i+1)))
    if y - birth >= 18:
        offage += 1
    else:
        underage += 1

print('\033[92mOff age: {}\n\033[91mUnderage: {}'.format(offage, underage))
