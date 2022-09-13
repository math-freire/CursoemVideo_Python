words = ('Little', 'Big', 'Bob', 'Melantha', 'La Pluma')

for word in words:
    print(f'\033[31m{word}:\033[m ', end='')
    for letter in word: # Every word is a list itself
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
    print('')
