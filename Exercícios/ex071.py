print('\033[1;31m-='*20)
print(f"{'Banking Account':^37}")
print('-='*20, '\033[m')

n50 = n20 = n10 = n1 = 0
# n = int(input('How much do you want to withdraw: '))
n = 987654321
while n != 0:
    if n >= 50:
        n50 = n // 50
        n -= n50 * 50
    if n >= 20:
        n20 = n // 20
        n -= n20 * 20
    if n >= 10:
        n10 = n // 10
        n -= n10 * 10
    if n >= 1:
        n1 = n
        n -= n1

print('\033[1;31m-='*20, '\033[m')
print(f"""You will receive...
{n50} $50 bills
{n20} $20 bills
{n10} $10 bills
{n1} $1 bills""")
print('\033[1;31m-='*20, '\033[m')