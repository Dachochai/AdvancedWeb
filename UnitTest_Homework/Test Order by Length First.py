import unittest
import Order_by_Length_First

class Testcase(unittest.TestCase):

    def test(self):
        self.assertEqual(Order_by_Length_First.make_grlex(["small", "big"]), ["big", "small"])
        self.assertEqual(Order_by_Length_First.make_grlex(["cat", "ran", "for", "the", "rat"]), ["cat", "for", "ran", "rat", "the"])
        self.assertEqual(Order_by_Length_First.make_grlex(["this", "is", "a", "small", "test"]), ["a", "is", "test", "this", "small"])
        
if __name__ == '__main__':
    unittest.main()