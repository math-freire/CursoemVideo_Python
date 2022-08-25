frase = 'Curso em Video Python'  # 21 characters
frase[9]  # V
frase[9:13]  # Vide, pos 13 is 'o', but the last (the range) doesn't count
frase[9:21]  # It stops on the last value, pos 20 = 'Video Python'
frase[9:21:2]  # VdoPto, takes jumping 2 positions
frase[:5]  # starts from beginning until 5 = 'Curso'

# [ where it starts : where it stops (n-1) : the jump]

frase[9::3]  # Starts from 9 until the end, jumping from 3 to 3 = 'VePh'

# Analise
len(frase)  # length = 21
frase.count('o')  # How many times the character appears in the string
frase.count('o', 0, 13)  # From 0 to 13
frase.find('deo')  # Search the beginning where appears 'deo' = 11
frase.find('Android')  # Return -1, because the string doesn't exist
'Curso' in frase  # True/False (it's an operator)

frase.replace('Python', 'Android')  # Find and replace
frase.upper()  # Change the string to uppercase
frase.lower()  # Change the string to lowercase
frase.capitalize()  # Change the first letter to uppercase, and the rest to lowercase
frase.title()  # Capitalize word per word

frase = '   Learn Python  '  # With surplus spaces
frase.strip()  # Removes the spaces in the beginning and at the end = 'Learn Python'
frase.rstrip()  # l or r to remove the spaces in the left or right, consecutively

frase = 'Curso em Video Python'
frase.split()  # Split in the spaces, creating a list with the words = 'Curso','em',Video','Python'
'-'.join(frase)  # put the sentence back together with ' - '

#  -- To practice --
frase = 'Curso em Video Python'
print(frase[::2])
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase)  # Curso em Video Python
# Replace doesn't change the string, just change the instance
#  But we can do frase = frase.replace('Python', 'Android')

split = frase.split()
print(split)  # 'Curso','em',Video','Python'
print(split[0])  # Curso
