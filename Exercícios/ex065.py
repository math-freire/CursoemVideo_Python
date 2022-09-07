from time import sleep

numbers = []
key = None
while key != 'n':
    numbers.append(float(input('Enter a number: ')))
    key = input('\033[34mDo you want to continue entering numbers [y/n]?\033[0m\n').strip().lower()
    while key != 'y' and key != 'n':
        if key != 'n' and key != 'y':
            print('\033[31mInvalid input\033[0m')
        key = input('\033[34mDo you want to continue entering numbers [y/n]?\033[0m\n').strip().lower()

sleep(0.5)
print('\033[1;33mAnalyzing data...\033[0m')
sleep(2)

print('The average is {}, the highest value is {} and the lowest is {}'.format(sum(numbers)/len(numbers), max(numbers),
                                                                               min(numbers)))
