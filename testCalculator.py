import unittest
from fluentCalculator import Calculator

# -----------------------------------------------------------------
# TESTING CLASS FOR CALCULATOR 
# -----------------------------------------------------------------

class TestCalculator(unittest.TestCase):
    calc = Calculator()
    def test_good_add(self):
        self.assertEqual(self.calc.new().two().plus().one(), 3)
    
    def test_good_subtract(self):
        self.assertEqual(self.calc.new().four().minus().one(), 3)
        
    def test_good_multiply(self):
        self.assertEqual(self.calc.new().two().times().nine(), 18)
        
    def test_good_divide(self):
        self.assertEqual(self.calc.new().nine().divided_by().three(), 3)
        
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.new().four().divided_by().zero(), 0)
        
    def test_no_operator(self):
        self.assertEqual(self.calc.new().two().one(), None)
        
    def test_no_digits(self):
        self.assertEqual(type(self.calc.new().plus()), type(Calculator()))
        
    def test_random_order(self):
        self.assertEqual(self.calc.new().plus().two().one(), 3)
        
# MAIN
def main():
    unittest.main()

main()