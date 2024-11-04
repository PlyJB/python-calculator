import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):    
        self.assertEqual(self.calc.add(-5,-3),-8)
    
    def test_add_Zero(self):    
        self.assertEqual(self.calc.add(1,0),1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(7,2),5)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-2,-8),6)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(2,5),10)

    def test_mul_Zero(self):
        self.assertEqual(self.calc.multiply(2,0),0)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(10,5),2)
    
    def test_div_zero(self):
        self.assertEqual(self.calc.divide(8,0),'error')
    
    def test_mod(self):
        self.assertEqual(self.calc.modulo(7,3),1)

    def test_mod_resultZero(self):
        self.assertEqual(self.calc.modulo(6,3),0)
    
if __name__ == '__main__':
    unittest.main()