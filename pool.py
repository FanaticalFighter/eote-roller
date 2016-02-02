from dice import *

class DicePool:
    """
    A pool of dice. That can be rolled.
    """

    def __init__(self, dice=[]):
        """
        Instantiates the dice pool object.

        dice: A list of dice in the pool.
        """

        if type(dice) is not list:
            raise TypeError('dice argument {} to DicePool object should be a list'.format(str(dice)))

        for d in dice:
            if type(d) is not Dice:
                raise TypeError('Element {} of dice argument to DicePool object should be a Dice'.format(str(d)))

        self.dice = dice

    def __repr__():
        return repr(self.dice)

    def __str__():
        return str(self.dice)

    def roll():
        """Returns a list of rolls of all the dice in the pool"""
        result = [die.roll() for die in dice]
        return result
