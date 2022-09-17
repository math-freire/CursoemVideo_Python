import random
from time import sleep

rn = random.randrange(0, 10)
num, count = None, 0

while num != rn:
    count += 1
    num = int(input('State a number between 0 and 10: '))
    print("\033[34mPROCESSANDO...")
    sleep(1)
    if rn == num:
        print('\033[32mCongrats! You are right. And after only {} attempts'.format(count))
    else:
        print('\033[31mYou are not that smart, huh?', end='. ')
        if num < rn:
            print('Try a little more...\033[0m')
        else:
            print('Too high...\033[0m')
    if count == 5 and rn != num:
        print("\033[33mLuck isn't by your side today...\033[0m")
