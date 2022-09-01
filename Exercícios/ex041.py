age = int(input('Age: '))

if age <= 9:
    print("Categoria Mirim")
elif age <= 14:
    print('Categoria Infantil')
elif age <= 19:
    print('Junior')
elif age <= 20:
    print('Senior')
else:
    print('Master')
