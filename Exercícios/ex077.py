words = ('Little', 'Big', 'Bob', 'Melantha', 'La Pluma')

for word in words:
    print(f'\033[31m{word}:\033[m ', end='')
    for i in range(0, len(word)):
        if word[i].lower() in 'aeiou':
            print(word[i], end=' ')
    print('')
