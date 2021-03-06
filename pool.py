from dice import *

class ContainerEmptyError(Exception):
    """Raised whenever an operation is attempted on an empty container object which should only be attempted when the container is not empty"""
    pass

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
            if not isinstance(d, Dice):
                raise TypeError('Element {} of dice argument to DicePool object should be a Dice'.format(str(d)))

        self.dice = dice

    def __repr__(self):
        return repr(self.dice)

    def __str__(self):
        return str(self.dice)

    def add_dice(self, dice):
        """Adds the dice to the pool. dice must be a Dice object"""

        if not isinstance(dice, Dice):
            raise TypeError('dice argument {} to add_dice() must be a Dice'.format(str(dice)))

        self.dice.append(dice)

    def rem_dice(self, dice):
        """Removes one dice which is identical to the argument dice from the
        Dice Pool"""

        try:
            self.dice.remove(dice)
        except ValueError as e:
            raise ValueError('dice {} is not in the DicePool, so can\'t be removed'.format(str(dice)))

    def roll(self):
        """Returns a list of rolls of all the dice in the pool"""

        if len(self.dice) <= 0:
            raise ContainerEmptyError('DicePool {} is empty, and can\'t be rolled'.format(str(self)))

        result = [die.roll() for die in self.dice]
        return result
