from math import pow, sqrt

co = float(input('Enter the opposite side: '))
ca = float(input('Enter the adjacent side: '))
hip = sqrt(pow(co, 2) + pow(ca, 2))

print('The hypotenuse of the triangle with the OS {} and AS {} is {:.2f}'.format(co, ca, hip))
