## Simple Dice Roll

import random
min = 1
max = int(input('Enter the required number of sides, e.g 6: '))
result = random.randint(min,max)
reroll = 'y'

print('Rolling the dice....')
print('Initial value is: %d' % result)

while reroll == 'y' or reroll == 'Y':

    reroll = input('Would you like to roll again? y/n')
    if reroll == 'y' or reroll == 'Y':
        result = random.randint(min,max)
        print('New value is: %d' % result)
