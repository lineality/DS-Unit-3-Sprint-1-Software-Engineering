#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import RandomProduct
from acme_report import list_length

#from acme import BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS



class AcmeProductTests(unittest.TestCase):

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
        
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_name(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        #this is producing a strange result...
        self.assertTrue(prod.name, "Tom")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Test default product price being 10."""
        generate_products()
        self.assertEqual(list_length, 29)

#    def test_legal_names(self):
#        """Test default product price being 10."""
#        generate_products()
#        self.assertEqual(products[1], str)

#    def test_legal_names(self):
#        """Test default product price being 10."""
#        generate_products()
#        self.assertEqual(products[1], str)

#    def test_default_glove_explodability(self):
#        """Test default product weight being 0.5."""
#        prod = BoxingGlove('Test Product')
#        self.assertEqual(prod.explode, "It's a glove")


if __name__ == '__main__':
    unittest.main()
