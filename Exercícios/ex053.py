p = input('Enter a phrase: ').strip().lower().split()
p = "".join(p)

if p == p[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
