import unittest
import Find_the_Bugs_Returning_Valid_Prices

class Testcase(unittest.TestCase):

    def test(self):
        self.assertEqual(Find_the_Bugs_Returning_Valid_Prices.has_valid_price({ "product": "Milk", "price": 1.50 }), True)
        self.assertEqual(Find_the_Bugs_Returning_Valid_Prices.has_valid_price({ "product": "Cheese", "price": -1 }), False)
        self.assertEqual(Find_the_Bugs_Returning_Valid_Prices.has_valid_price({ "product": "Eggs", "price": 0 }), True)
        self.assertEqual(Find_the_Bugs_Returning_Valid_Prices.has_valid_price({ "product": "Cereals", "price": "3.0" }), False)
        self.assertEqual(Find_the_Bugs_Returning_Valid_Prices.has_valid_price(None), False)
        
if __name__ == '__main__':
    unittest.main()