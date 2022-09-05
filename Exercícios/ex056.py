names, ageM, ages = [], [], []
under20w = 0

totalPeople = int(input('How many people: '))
for i in range(0, totalPeople):
    name = input('Enter name #{}: '.format(i+1)).strip()
    age = int(input('Enter age #{}: '.format(i + 1)))
    ages.append(age)
    sex = input('Enter sex #{} (M or F): '.format(i + 1)).strip().upper()

    # Women with less than 20 years old
    if sex == 'F' and age < 20:
        under20w += 1

    elif sex == 'M':
        names.append(name)
        ageM.append(age)

# Age average
averageAge, sumAge = 0, 0
for someAge in ages:
    sumAge += someAge
averageAge = sumAge // totalPeople

# Older man
older = max(ageM)
olderIndex = ageM.index(older)
olderManName = names[olderIndex]

# Exit
print('The \033[91maverage age\033[0m for the mentioned group is \033[91m{}\033[0m, \033[93m{}\033[0m women have '
      '\033[93mless than 20 years old\033[0m and \033[94m{}\033[0m is the \033[94moldest man\033[0m with \033[94m{} '
      'years old\033[0m.'.format(averageAge, under20w, olderManName, older))
