from dice import *
from pool import *
import sys, re

def get_all_eote_dice():
    """Returns a list of all the dice in the Edge of the Empire game."""
    dlist = [
        Dice('Boost', ['', '', 'Success', ['Success', 'Advantage'], ['Advantage', 'Advantage'], 'Advantage']),
        Dice('Setback', ['', '', 'Failure', 'Failure', 'Threat', 'Threat']),
        Dice('Ability', ['', 'Success', 'Success', ['Success', 'Success'], 'Advantage', 'Advantage', ['Advantage', 'Success'], ['Advantage', 'Advantage']]),
        Dice('Difficulty', ['', 'Failure', ['Failure', 'Failure'], 'Threat', 'Threat', 'Threat', ['Threat', 'Threat'], ['Failure', 'Threat']]),
        Dice('Proficiency', ['', 'Success', 'Success', ['Success', 'Success'], ['Success', 'Success'], 'Advantage', ['Success', 'Advantage'], ['Success', 'Advantage'], ['Success', 'Advantage'], ['Advantage', 'Advantage'], ['Advantage', 'Advantage'], 'Triumph']),
        Dice('Challenge', ['', 'Failure', 'Failure', ['Failure', 'Failure'], ['Failure', 'Failure'], 'Threat', 'Threat', ['Failure', 'Threat'], ['Failure', 'Threat'], ['Threat', 'Threat'], ['Threat', 'Threat'], 'Despair' ]),
        Dice('Force', ['Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', ['Dark', 'Dark'], 'Light', 'Light', ['Light', 'Light'], ['Light', 'Light'], ['Light', 'Light']])
    ]

    return dlist

def main():
    dice_list = get_all_eote_dice()

if __name__ == '__main__':
    main()
