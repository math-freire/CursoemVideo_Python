from math import sin, cos, tan, radians

ang = radians(float(input('Enter an angle: ')))
print('The sin of {:.2f} is {:.2f}\nThe cos is {:.2f}\nand the tan is {:.2f}'.format(ang, sin(ang), cos(ang), tan(ang)))

# We need to read in radians so the result in the print be in angular (like sin(30) = 0.5