import my_codes


def area(x, y):
    a = x * y
    print(f'The area is {a:.2f}m²')


my_codes.titulo('FUNÇÃO PARA CALCULAR ÁREA', 30)
x = float(input('Enter the lenght (m): '))
y = float(input('Enter the width (m): '))
area(x, y)
my_codes.end_program()
