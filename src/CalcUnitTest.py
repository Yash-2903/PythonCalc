import unittest
from Calc import Calc
from CSVReader import CSVReader
from pprint import pprint


class MyUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, Calc)

    def test_addition(self):
        test_add_data = CSVReader("/src/CSVFiles/Unit_Test_Addition.csv").data
        for row in test_add_data:
            self.assertEqual(self.calc.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_subtraction(self):
        test_sub_data = CSVReader("/src/CSVFiles/Unit_Test_Subtraction.csv").data
        for row in test_sub_data:
            self.assertEqual(self.calc.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_multiplication(self):
        test_multiple_data = CSVReader("/src/CSVFiles/Unit_Test_Multiplication.csv").data
        self.assertEqual(self.calc.sub(5, 10), 5)
        for row in test_multiple_data:
            self.assertEqual(self.calc.multiple(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
