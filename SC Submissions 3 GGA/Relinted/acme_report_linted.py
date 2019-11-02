#!/usr/bin/env python

import random
from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Pickle']


"""
- `name` should be a random adjective from `['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']` followed by a space and then a random noun from
  `['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']`, e.g. `'Awesome Anvil'`
  and `Portable Catapult'` are both possible

- `price` and `weight` should both be from 5 to 100 (inclusive and independent,
  and remember - they're integers!)

- `flammability` should be from 0.0 to 2.5 (floats)

"""

name_list = ['Shiny Disguise',
                'Awsome Anvil',
                'Portable Mousetrap',
                'Impressive Catapult']

"""
This class generates random products
"""


class RandomProduct(Product):
    def __init__(self, name='unnamed', price=None, weight=None, flammability=None, identifier=None):
        if identifier is None:
            identifier = random.randint(1000000, 9999999)
        if flammability is None:
            flammability = random.uniform(0.0, 2.5)
#            flammability = random.choice(flammability_list)
#            flammability = random.random(0.0, 2.5)
        if weight is None:
            weight = random.randint(5, 100)
        if price is None:
            price = random.randint(5, 100)
        if name == 'unnamed':
            name = random.choice(name_list)
        self.name = name  # string with no default
        self.price = price  # integer with default value 10
        self.weight = weight  # integer with default value 20
        self.flammability = flammability  # (float with default value 0.5
        self.identifier = identifier # random int between 1000000 & 9999999


"""
The two functions below generate a fictional report
first generating fake products
then producing a summary
"""


products = []
prices = []
weights = []
flammabilities = []
identifiers = []


def generate_products(num_products=30):

    i = 1
    while i < num_products:
        item = RandomProduct()

        name1 = item.name
        products.append(name1)

        price1 = item.price
#        price1 = int(price1)
        prices.append(price1)

        weight1 = item.weight
        weights.append(weight1)

        flammability1 = item.flammability
        flammabilities.append(flammability1)

        identifier1 = item.identifier
        identifiers.append(identifier1)

        i = i+1
    return products, prices, weights, flammabilities, identifiers

# runs function
generate_products()

# checking datatype
# isinstance(prices[3], int)

# print(prices)


def inventory_report(products):

    print("TOP SECRET ACME CORPORATION INVENTORY REPORT EXECUTIVE SUMMARY")

    #    print("Number of Unique product names")
    #    print("Number of unique product identifiers")
    #    products
    #    identifiers

    print("average price = ", (sum(prices) / len(prices)))

    print("average weight =", (sum(weights) / len(weights)))

    print("average flammability =", (sum(flammabilities) / len(flammabilities)))

    return  # TODO - your code! Loop over the products to calculate the report.

list_length = len(products)

if __name__ == '__main__':
    inventory_report(generate_products())
