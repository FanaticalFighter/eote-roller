from dice import *
from pool import *
import sys, re

def get_all_eote_dice():
    """Returns a dict of all the dice in the Edge of the Empire game."""
    ddict = {
        'Boost': Dice('Boost', ['', '', 'Success', ['Success', 'Advantage'], ['Advantage', 'Advantage'], 'Advantage']),
        'Setback': Dice('Setback', ['', '', 'Failure', 'Failure', 'Threat', 'Threat']),
        'Ability': Dice('Ability', ['', 'Success', 'Success', ['Success', 'Success'], 'Advantage', 'Advantage', ['Advantage', 'Success'], ['Advantage', 'Advantage']]),
        'Difficulty':Dice('Difficulty', ['', 'Failure', ['Failure', 'Failure'], 'Threat', 'Threat', 'Threat', ['Threat', 'Threat'], ['Failure', 'Threat']]),
        'Proficiency': Dice('Proficiency', ['', 'Success', 'Success', ['Success', 'Success'], ['Success', 'Success'], 'Advantage', ['Success', 'Advantage'], ['Success', 'Advantage'], ['Success', 'Advantage'], ['Advantage', 'Advantage'], ['Advantage', 'Advantage'], 'Triumph']),
        'Challenge': Dice('Challenge', ['', 'Failure', 'Failure', ['Failure', 'Failure'], ['Failure', 'Failure'], 'Threat', 'Threat', ['Failure', 'Threat'], ['Failure', 'Threat'], ['Threat', 'Threat'], ['Threat', 'Threat'], 'Despair' ]),
        'Force': Dice('Force', ['Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', ['Dark', 'Dark'], 'Light', 'Light', ['Light', 'Light'], ['Light', 'Light'], ['Light', 'Light']])
    }

    return ddict

def main():
    dice_dict = get_all_eote_dice()

if __name__ == '__main__':
    main()
