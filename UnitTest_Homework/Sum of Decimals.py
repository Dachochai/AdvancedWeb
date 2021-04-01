import unittest
from unittest.case import TestCase

class Testcase(unittest.TestCase):

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def float_sum(self, A, B):
        return A + B

A = float(input("Enter Number 1: "))
B = float(input("Enter Number 2: "))

cal = Testcase(A, B)
print(cal.float_sum(A, B))

if __name__ == '__main__':
    unittest.main()