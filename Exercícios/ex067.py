while True:
    print('~' * 20)
    n = int(input('Which multiplication table do you want? '))
    print('~'*20)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} * {i} = {n*i}')
