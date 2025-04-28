'''
Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times.
'''
# Make a class Die with one attribute called sides, which has a default value of 6
import random

class Die():

    def __init__(self, die_sides=6):
        self.die_sides = die_sides

    # method called roll_die() that prints a random number between 1 and the number of sides the die has
    def roll_die(self):
        return random.randint(1,self.die_sides)

# instance
six_die = Die()
tw_die = Die(12)

# calls
# roll 6-sided die 10 times
print(six_die.roll_die())

for i in range (10):
    print(six_die.roll_die())
