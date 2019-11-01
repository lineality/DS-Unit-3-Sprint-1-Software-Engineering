"""
Classes for very classy acme corp product info
This has been run through http://pep8online.com/checkresult
"""

from numpy import random


class Product:
    """
    defaults included where offers apply
    """

    def __init__(self, name='unnamed', price=10, weight=20, flammability=0.5, identifier=None):
        if identifier is None:
            identifier = random.randint(1000000, 9999999)
        self.name = name  # string with no default)
        self.price = price  # (integer with default value 10)
        self.weight = weight  # (integer with default value 20)
        self.flammability = flammability  # (float with default value 0.5)
        """
        (integer, automatically genererated as a random
        (uniform) number anywhere from 1000000 to 9999999,
        includisve)(inclusive).
        """
        self.identifier = identifier

    def stealability(self):
        stealable = price/weight
        if stealable < 0.5:
            print("Not so stealable...")
        if 0.5 < stealable < 1.0:
            print("kinda stealable")
        else:
            print("Very stealable!")
        return

    def explode(self):
        if flammability < 10:
            print("fizzle...)
        if 10 < flammability < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")
        return

"""
the 2 long lines below are too long, all attempts at wrapping 
caused run errors, no solutions found on google
"""


class BoxinGlove(Product):
    def __init__(self, name='unnamed', price=10, weight=10, flammability=0.5, identifier=None):
        if identifier is None:
            identifier = random.randint(1000000, 9999999)
        self.name = name  # string with no default)
        self.price = price  # (integer with default value 10)
        self.weight = weight  # (integer with default value 20)
        self.flammability = flammability  # (float with default value 0.5)

    def stealability(self):
        stealable = price/weight
        if stealable < 0.5:
            print("Not so stealable...")
        if 0.5 < stealable < 1.0:
            print("kinda stealable")
        else:
            print("Very stealable!")
        return

    def punch(self):
        if weight < 5:
            print("That tickles")
        if 5 < weight < 15:
            print("Haey tht hurt!")
        else:
            print("OUCH!")
        return

    def explode(self):
        return print("It's a glove")
