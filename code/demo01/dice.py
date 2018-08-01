# zc-cris
from random import randint


class Dice:
    def __init__(self, dice_num=6):
        self.dice_num = dice_num

    def play(self):
        return randint(1, self.dice_num)
