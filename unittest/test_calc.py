"""Calculator class
"""

import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    """Basic calculator with add, subrtract, multiply and divide functions
    """

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(20, 10), 30, "incorrect addition")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(20, 10), 10, "incorrect subtraction")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(20, 10), 200, "incorrect multiplication")

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 10), 2, "incorrect division")
        

if __name__ == '__main__':
    unittest.main()
