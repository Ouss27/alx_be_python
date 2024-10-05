import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):

    #Set up a SimpleCalculator instance for use in all tests
    def set_up(self):
        self.calc = SimpleCalculator()

    #test addition method
    def test_addition(self):
        self.assertEqual(self.calc.add(1,2),3)
        self.assertEqual(self.calc.add(1,-3),-2)
        self.assertEqual(self.calc.add(0,0),0)

    #test substraction method
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    #test multiplication method
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    #test division method
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 1), 3)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero

if __name__ == '__main__':
    unittest.main()