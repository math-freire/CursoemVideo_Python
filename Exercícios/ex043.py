w = float(input('Weight (Kg): '))
h = float(input('Height (m): '))
imc = w / pow(h, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('You good, bro')
elif 25 <= imc < 30:
    print('Calm down... um pouco acima')
elif 30 <= imc < 40:
    print('Dude... you are a little fat (obesity')
else:
    print('You are a large individual (over fat)')
