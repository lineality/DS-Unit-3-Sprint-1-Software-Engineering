#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


"""
The explode method(function) should be
testable given one imput since there is only
one output for any input
"""
BoxinGlove(test_glove1, 10, 10, 10)
BoxinGlove(test_glove2, 10, 10, 10)
BoxinGlove(test_glove3, 10, 10, 10)

def test_explode_function():
    assert explode(test_glove1) == "It's a glove", "explode boxing method error"
    return

test_explode_function()

"""
The stealability function(method) has 3 possible outputs
and so should be tested 3 times
once for each output
"""
BoxinGlove(test_glove2, 10, 10, 10)

def test_stealability_function1():
    assert stealability(test_glove1) == "Not so stealable..."
    return

def test_stealability_function2():
    assert stealability(test_glove2) == "kinda stealable"
    return

def test_stealability_function3():
    assert stealability(test_glove3) == "Very stealable!"
    return

test_stealability_function1()
test_stealability_function2()
test_stealability_function3()


if __name__ == '__main__':
    unittest.main()
