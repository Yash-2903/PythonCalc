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
        test_data = CSVReader("/src/Unit_Test_Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calc.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CSVReader("/src/Unit_Test_Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calc.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
