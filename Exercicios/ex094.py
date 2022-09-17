from time import sleep

i = 0  # Total of persons
people = []
while True:
    i += 1
    print(f'#{i} person')
    temp_dict_person = {'name': input('Name: '),
                        'sex': input('Sex: '),
                        'age': int(input('Age: '))}
    people.append(temp_dict_person)

    flag = input('Continue [Y/N]? ')
    while flag not in 'YyNn':
        flag = input('\033[31mInvalid input! Continue [Y/N]? \033[m')
    if flag in 'Nn':
        sleep(1)
        print('\033[31m- Shutting down -\033[m')
        sleep(1)
        break

sum_age = 0
women = []
for person in people:
    sum_age += person['age']
    if person['sex'] in 'Ff':
        women.append(person['name'])

above_av = []
for person in people:
    if person['age'] > (sum_age/len(people)):
        above_av.append(person['name'])

print(f'There are {len(people)} people in the list.')
print(f'The average age is {sum_age/len(people):.1f}')
print(f"The women in the list are: ", end='')
for name in women: print(f'{name} ', end='')
print()
print(f"The person(s) above the age average are: ", end='')
for name in above_av: print(f'{name} ', end='')
print()
