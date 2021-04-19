import unittest
import Drunken_Python

class Testcase(unittest.TestCase):

    def test(self):
        self.assertEqual(Drunken_Python.int_to_str(4), "4")
        self.assertEqual(Drunken_Python.str_to_int("4"), 4)
        self.assertEqual(Drunken_Python.int_to_str(4), "4")
        
if __name__ == '__main__':
    unittest.main()