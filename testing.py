from first_and_second import divide_sqrt
import unittest
import math

class UnitTest(unittest.TestCase):
    
    def test_normal_numbers(self):
        self.assertEqual(divide_sqrt(5, 1, 4, 2), 1)
        self.assertEqual(divide_sqrt(10, 1, 4, 1), 1)

        
    def test_zero(self):
        self.assertEqual(divide_sqrt(5, 1, 2, 2), "Ошибка: Деление на ноль.")    


    def test_minus_sqrt(self):
        self.assertEqual(divide_sqrt(1, 5, 4, 2),"Ошибка: Невозможно вычислить логарифм или корень из отрицательного числа.")
            
             
    def test_minus_low(self):
        self.assertEqual(divide_sqrt(6, 2, 1, 3), -1)
        self.assertEqual(divide_sqrt(10, 0, 2, 4), math.sqrt(10)/(-2))


if __name__ == '__main__':
    unittest.main()