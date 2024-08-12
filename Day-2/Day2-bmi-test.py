# test_bmi_calculator.py

import unittest

from Bmi_calculator import Bmi_cal

class TestBmiCalculator(unittest.TestCase):
    
    def test_bmi_cal(self):
        # Test case 1: Normal inputs
        result = Bmi_cal(1.75, 70)
        self.assertAlmostEqual(result, 22.86, places=2)
        
        # Test case 2: Very low weight
        result = Bmi_cal(1.75, 50)
        self.assertAlmostEqual(result, 16.33, places=2)
        
        # Test case 3: Very high weight
        result = Bmi_cal(1.75, 100)
        self.assertAlmostEqual(result, 32.65, places=2)
        
        # Test case 4: Zero height (edge case)
        with self.assertRaises(ZeroDivisionError):
            Bmi_cal(0, 70)
        
        # Test case 5: Non-numeric input
        with self.assertRaises(ValueError):
            Bmi_cal('invalid', 70)

if __name__ == '__main__':
    unittest.main()
