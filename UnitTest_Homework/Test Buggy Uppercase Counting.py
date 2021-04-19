import unittest
import Buggy_Uppercase_Counting

class Testcase(unittest.TestCase):

    def test(self):
        self.assertEqual(Buggy_Uppercase_Counting.count_uppercase(["SOLO", "hello", "Tea", "wHat"]), 6)
        self.assertEqual(Buggy_Uppercase_Counting.count_uppercase(["little", "lower", "down"]), 0)
        self.assertEqual(Buggy_Uppercase_Counting.count_uppercase(["EDAbit", "Educate", "Coding"]), 5)
        
if __name__ == '__main__':
    unittest.main()