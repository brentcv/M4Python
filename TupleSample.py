'''
Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list 
and print a message saying that any ticket matching these four numbers 
or letters wins a prize.
'''

import random

# Make a list or tuple containing a series of 10 numbers and five letters.
prize_list = (6,12,19,25,29,37,42,47,55,64,'e','l','s','q','r','v')
#print(prize_list)

# Randomly select four numbers or letters from the list
random.sample(prize_list,4)

# and print a message saying that any ticket matching these four numbers 
# or letters wins a prize
print(f'Any ticket matching these {random.sample(prize_list,4)} wins the prize!')

