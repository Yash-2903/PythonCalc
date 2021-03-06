import unittest
from Calc import Calc
from CSVReader import CSVReader
from StaticProperties.StaticVariable import StaticVariable
from pprint import pprint


class MyUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calculator(self):
        pprint("Initial Test 1")
        self.assertIsInstance(self.calc, Calc)

    # Unit Test for Addition
    def test_addition(self):
        test_add_data = CSVReader(StaticVariable.unitTestAddition).data
        pprint("Addition Test")
        for row in test_add_data:
            self.assertEqual(self.calc.add(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    # Unit Test for Subtraction
    def test_subtraction(self):
        test_sub_data = CSVReader(StaticVariable.unitTestSubtraction).data
        pprint("Subtraction Test")
        for row in test_sub_data:
            self.assertEqual(self.calc.sub(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    # Unit Test for Multiplication
    def test_multiplication(self):
        test_multiple_data = CSVReader(StaticVariable.unitTestMultiplication).data
        pprint("Multiplication Test")
        for row in test_multiple_data:
            self.assertEqual(self.calc.multiple(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    # Unit Test for Division
    def test_division(self):
        test_div_data = CSVReader(StaticVariable.unitTestDivision).data
        pprint("Division Test")
        for row in test_div_data:
            self.assertAlmostEqual(self.calc.div(row[StaticVariable.value1], row[StaticVariable.value2]),
                                   float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    # Unit Test for Square
    def test_square(self):
        test_sq_data = CSVReader(StaticVariable.unitTestSquare).data
        pprint("Square Test")
        for row in test_sq_data:
            self.assertAlmostEqual(self.calc.sq(row[StaticVariable.value1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    # Unit Test for SquareRoot
    def test_squareRoot(self):
        test_sqrt_data = CSVReader(StaticVariable.unitTestSquareRoot).data
        pprint("SquareRoot Test")
        for row in test_sqrt_data:
            self.assertAlmostEqual(self.calc.sqrt(row[StaticVariable.value1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))


if __name__ == '__main__':
    unittest.main()
