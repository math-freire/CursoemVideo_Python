import datetime
# atual = date.today().year retornará o ano
y = int(input('Age: '))

date = datetime.date.today()  # Dia atual
year = int(date.strftime("%Y"))  # Ano atual

age = year - y
if age < 18:
    print('Safe')
elif age == 18:
    print('USA needs you, Bro')
else:
    print("Bad news... you should've served")
