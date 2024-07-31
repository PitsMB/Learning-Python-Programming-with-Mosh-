import random


class Dice:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def roll(self):
        first = random.randint(self.start, self.end)
        second = random.randint(self.start, self.end)
        return (first, second)
    

dice = Dice(start=1, end=6)
print(dice.roll())
