import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

die6 = Die()

print("6-sided die:")

for roll in range(10):
    print(die6.roll_die())

die10 = Die(10)

print("\n10-sided die:")

for roll in range(10):
    print(die10.roll_die())

die20 = Die(20)

print("\n20-sided die:")

for roll in range(10):
    print(die20.roll_die())
