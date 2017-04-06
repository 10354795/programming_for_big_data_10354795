# Thomas O'Brien ID 10354795
# Calculator test program

# This program runs a series of tests using test data to ensure that the calculations 
# are correct when run by the calculator.
#
# Note: for division, a check is included to identify dive by zero errors.

#Import unit test functionality.

import unittest

# Import calculation algorithms from the Calculator Class in calculator.py

from calculator import *

class TestCalculator(unittest.TestCase):   # test the calculator functionality

                 
    def setUp(self):
        self.calc = Calculator()

# Identify test calculation results and set up tests to validate the results.
# Note additional test included in the divide section to test for divide by zero.
# The tests are repeated for each of the funtions defined in the calculator.

	# this tests the add functionality
	# 2 + 2 = 4
	# 2 + 4 = 6
	# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

	# this tests the subtract functionality
	# 2 - 2 = o
	# 2 - 4 = -2
	# 2 - (-2) = 4
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -2)
        self.assertEqual(4, result)

	# this tests the multiplication functionality
	# 2 * 2 = 4
	# 2 * 4 = 8
	# 2 * (-2) = -4
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        
	# this tests the division functionality
	# 2 / 2 = 1
	# 9 / 0 = This should give an error as divide by zero
	# 2 / (-2) = -1
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(9,0)  # This line tests for divide by zero error condition
        self.assertEqual(None, result)  # "None" is returned when error occurs.
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)

	# this tests the exponent functionality
	# 2 ** 2 = 4
	# 2 ** 4 = 16
	# 3 ** 3 = 27
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,4)
        self.assertEqual(16, result)
        result = self.calc.exponent(3,3)
        self.assertEqual(27, result)

	# this tests the square root functionality
	# Sqrt 4 =2
	# Sqrt 81 = 9
	# sqrt 25 = 5
    def test_calculator_square_root_method_returns_correct_result(self):
        result = self.calc.square_root(4)
        self.assertEqual(2, result)
        result = self.calc.square_root(81)
        self.assertEqual(9, result)
        result = self.calc.square_root(9)
        self.assertEqual(3, result)
        
	# this tests the square functionality
	# 2 * 2 = 4
	# 5 * 5 = 25
	# 3 * 3 = 9
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(2)
        self.assertEqual(4, result)
        result = self.calc.square(5)
        self.assertEqual(25, result)
        result = self.calc.square(3)
        self.assertEqual(9, result)
        
	# this tests the cube functionality
	# 2 * 2 * 2 = 8
	# 5 * 5 * 5 = 125
	# 3 * 3 *3 = 27
    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube(2)
        self.assertEqual(8, result)
        result = self.calc.cube(5)
        self.assertEqual(125, result)
        result = self.calc.cube(3)
        self.assertEqual(27, result)

	# this tests the Sin conversion functionality
	# sin 0 = 0
	# sin 45 = 0.850903524534
	# sin 90 = 0.893996663601
    def test_calculator_sin_method_returns_correct_result(self):
        result = self.calc.sin(0)
        self.assertEqual(0, result)
        result = self.calc.sin(45)
        self.assertEqual(0.8509, round(result, 4)) # fix and compare result to 4 decimal places as result is very long. 
        result = self.calc.sin(90)
        self.assertEqual(0.894, round(result, 4)) # fix and compare result to 4 decimal places as result is very long.

	# this tests the cos conversion functionality
	# cos 0 = 1
	# cos 45 = 0.525321988818
	# cos 90 = -0.448073616129
    def test_calculator_cos_method_returns_correct_result(self):
        result = self.calc.cos(0)
        self.assertEqual(1, result)
        result = self.calc.cos(45)
        self.assertEqual(0.5253, round(result, 4)) # fix and compare result to 4 decimal places as result is very long. 
        result = self.calc.cos(90)
        self.assertEqual(-0.4481, round(result, 4)) # fix and compare result to 4 decimal places as result is very long.
      
	# this tests the tan conversion functionality
	# tan 0 = 0
	# tan 45 = 1  Note rounding error.  Actual calculation gives 0.9999 which is effectively 1.
   # tan 90 & 270 = error. The calculator returns None. The same applies to 270.
	# tan 180 = 0
    def test_calculator_tan_method_returns_correct_result(self):
        result = self.calc.tan(0)
        self.assertEqual(0, result)
        result = self.calc.tan(45)
        self.assertEqual(1, round(result, 0))
        result = self.calc.tan(90)
        self.assertEqual('Error', result) # Returns an error.
        result = self.calc.tan(180)
        self.assertEqual(0, round(result, 0))
        result = self.calc.tan(270)
        self.assertEqual('Error', result) # Returns an error. 
              

if __name__ == '__main__':
    unittest.main()