import my_codes


def write(phrase):
    print('~' * (len(phrase)+4))
    print(f'  {phrase}  ')
    print('~' * (len(phrase)+4))


my_codes.titulo('ADAPTABLE TITLE', 30)
n = int(input('How many phrases? '))
p = []
for i in range(0, n):
    p.append(input(f'Phrase #{i}: '))
for each in p:
    write(each)

my_codes.end_program()
