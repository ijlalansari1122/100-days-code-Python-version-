import unittest
from Bmi_calculator import Bmi_cal  # Import your function

class TestBmiCalculator(unittest.TestCase):
    
    def test_bmi_cal(self):
        # Test with direct inputs, no manual input needed
        result = Bmi_cal(1.75, 70)
        self.assertAlmostEqual(result, 22.86, places=2)
        
        result = Bmi_cal(1.75, 50)
        self.assertAlmostEqual(result, 16.33, places=2)
        
        result = Bmi_cal(1.75, 100)
        self.assertAlmostEqual(result, 32.65, places=2)
        
        with self.assertRaises(ZeroDivisionError):
            Bmi_cal(0, 70)
        
        with self.assertRaises(ValueError):
            Bmi_cal('invalid', 70)

if __name__ == '__main__':
    unittest.main()
