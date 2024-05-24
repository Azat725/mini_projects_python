import unittest
import unittest.mock
from calculator import main

class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        input_values = ["1", "2", "3", "stop"]
        expected_result = 6
        
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            main()
            
            self.assertEqual(expected_result, 6)
            
    def test_subtraction(self):
        input_values = ["5", "2", "1", "stop"]
        expected_result = 2

        with unittest.mock.patch('builtins.input', side_effect=input_values):
            main()

            self.assertEqual(expected_result, 2) 

    def test_multiplication(self):
        input_values = ["2", "3", "4", "stop"]
        expected_result = 24

        with unittest.mock.patch('builtins.input', side_effect=input_values):
            main()

            self.assertEqual(expected_result, 24) 

    def test_division(self):
        input_values = ["10", "2", "stop"]
        expected_result = 5
        
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            main()
            
            self.assertEqual(expected_result, 5)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()