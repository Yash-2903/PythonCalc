import unittest
from Calc import Calc


class MyUnitTest(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)
