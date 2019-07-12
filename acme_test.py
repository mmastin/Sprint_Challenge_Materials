import unittest
from acme import Product
from acme_report import generate_products, adjective, noun

# wrote this earlier
# prod = Product('A Cool Toy')
#
# prod.name
# prod.price
# prod.weight
# prod.flammability
# prod.identifier
# prod.stealability
# prod.explode

class AcmeProductTests(unittest.TestCase):
    # making sure Acme products are the tops!

    def test_default_price(self):
        # test default product price being 10.

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        # ensuring stealability and explode functions work correctly
        prod = Product('Wile E Coyote Bomb', 1234, 1, 99)
        self.assertEqual(prod.explode(), '...BABOOM')
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        # checking list length = 30
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        # checking generated names are all valid possibilities
        products = generate_products()
        adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

        for product in products:
            product_name = product.name.split()
            adjective_used = product_name[0]
            noun_used = product_name[1]
            self.assertIn(adjective_used, adjective)
            self.assertIn(noun_used, noun)


if __name__ == '__main__':
    unittest.main()