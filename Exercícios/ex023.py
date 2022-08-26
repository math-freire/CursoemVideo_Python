number = 'abcde'
while len(number) > 4:  # If greater than 9999
    number = input('Enter a number between 1 and 9999: ')

print(""" 
Unit: {}
Ten: {}
Hundred: {}
Thousand: {}""".format(number[3], number[2], number[1], number[0]))
