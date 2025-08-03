import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc=SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-3, -2),-1)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(-2, -2), -4)
        self.assertEqual(self.calc.multiply(0, 0), 0)
    def test_divination(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, -3), 3)
    def test_DivideByZero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    if __name__ == '__main__':
        unittest.main()
        
        
        
        