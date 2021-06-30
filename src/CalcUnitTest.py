import unittest
from Calc import Calc


class MyUnitTest(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)

    def test_add_method_Calc(self):
        calc = Calc()
        self.assertEqual(calc.add(2, 2), 4)

    def test_sub_method_Calc(self):
        calc = Calc()
        self.assertEqual(calc.sub(2, 2), 0)


if __name__ == '__main__':
    unittest.main()
