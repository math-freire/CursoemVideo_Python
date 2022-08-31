def any2dec(num_original, base_original):
    num_original = str(num_original)
    base_original = int(base_original)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x, i in enumerate(dec_temp):
        dec += dic.index(i) * base_original ** (x)
    return str(dec)


def dec2any(dec, base_final):
    base_final = int(base_final)
    dec = int(dec)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numero_final_temp = []
    numero_final = ''
    while True:
        temp_numero_final = dec % base_final
        numero_final_temp.append(temp_numero_final)
        if int(dec / base_final) == 0:
            break
        dec = int(dec / base_final)
    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]
    return numero_final


def any2any(num_original, base_original, base_final):
    num_dec = any2dec(num_original, base_original)
    num_final = dec2any(num_dec, base_final)
    return num_final


number = int(input('Enter an integer: '))
key = int(input('1 - Binary, 2 - octal, 3 hexadecimal\n'))

if key == 1:
    print('->', dec2any(number, 2))
elif key == 2:
    print('->', dec2any(number, 8))
else:
    print('->', hex(number))
