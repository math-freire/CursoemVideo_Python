n = int(input('Enter a number: '))

key = 0
for i in range(2, n):
    if n % i == 0:
        print("It's not a prime number!")
        key = -1
        break

if key == 0:
    print("It's a prime number!")
