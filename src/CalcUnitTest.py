import unittest
from Calc import Calc
from CSVReader import CSVReader
from StaticVariable import StaticVariable


class MyUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, Calc)

    def test_addition(self):
        test_add_data = CSVReader(StaticVariable.unitTestAddition).data
        for row in test_add_data:
            self.assertEqual(self.calc.add(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_subtraction(self):
        test_sub_data = CSVReader(StaticVariable.unitTestSubtraction).data
        for row in test_sub_data:
            self.assertEqual(self.calc.sub(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_multiplication(self):
        test_multiple_data = CSVReader(StaticVariable.unitTestMultiplication).data
        for row in test_multiple_data:
            self.assertEqual(self.calc.multiple(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_division(self):
        test_div_data = CSVReader(StaticVariable.unitTestDivision).data
        for row in test_div_data:
            self.assertAlmostEqual(self.calc.div(row[StaticVariable.value1], row[StaticVariable.value2]),
                                   float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    def test_square(self):
        test_sq_data = CSVReader(StaticVariable.unitTestSquare).data
        for row in test_sq_data:
            self.assertAlmostEqual(self.calc.sq(row[StaticVariable.value1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    def test_squareRoot(self):
        test_sqrt_data = CSVReader(StaticVariable.unitTestSquareRoot).data
        for row in test_sqrt_data:
            self.assertAlmostEqual(self.calc.sqrt(row[StaticVariable.value1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))


if __name__ == '__main__':
    unittest.main()
