from first_and_second import test_uravnenie
import unittest
import math

class TestEquationSolver(unittest.TestCase):
    
    def test_normal_values(self):
        self.assertAlmostEqual(test_uravnenie(5, 1, 4, 2), 1)
        self.assertAlmostEqual(test_uravnenie(9, 1, 5, 1), 2)
    
    def test_minus_sqrt(self):
        with self.assertRaises(ValueError):
            test_uravnenie(1, 5, 4, 2)
    
    def test_zero(self):
        with self.assertRaises(ValueError):
            test_uravnenie(5, 1, 2, 2)
    
    def test_minus_low(self):
        self.assertAlmostEqual(test_uravnenie(6, 2, 1, 3), 1)
        self.assertAlmostEqual(test_uravnenie(10, 0, 2, 4), math.sqrt(10)/2)


if __name__ == '__main__':
    unittest.main()