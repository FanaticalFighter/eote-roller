import random

class Dice:
    """
    A dice. That you can roll. Can have arbitrary sides.
    """
    def __init__(self, name, sides):

        """
        Instantiates a Dice object.

        Arguments:
        sides: A list of the sides of the dice. Each object in this can be anything (an str, a list of str, etc)
        name: An str which is the 'name' of this kind of dice.
        """

        if type(sides) is not list:
            raise TypeError('sides argument {} to Dice object should be a list (is {})'.format(repr(sides), str(type(sides))))

        if type(name) is not str:
            raise TypeError('name argument {} to Dice object is not an str'.format(str(name)))

        self.sides = sides
        self.name = name

    def __str__(self):
        """Returns a nice string representation of the object."""
        return '{}: {}'.format(self.name, str(self.sides))

    def __repr__(self):
        """Returns a representation of the object."""
        return "\'{}\'".format(self.__str__())

    def roll(self):
        """Returns the result of a roll of the Dice."""

        rnum = random.randint(0, len(self.sides) - 1)
        return self.sides[rnum]
