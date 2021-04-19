import unittest
import Sum_of_Decimals

class Testcase(unittest.TestCase):

    def test(self):
        self.assertEqual(Sum_of_Decimals.float_sum(0.3, 0.7), 1)
        self.assertEqual(Sum_of_Decimals.float_sum(0.35, 0.75), 1.1)
        self.assertEqual(Sum_of_Decimals.float_sum(1.234, 5.6789), 6.9129)
        
if __name__ == '__main__':
    unittest.main()