# Thomas O'Brien ID 10354795
# Calculator_List test program

# This program runs a series of tests using test data in the x & y test data lists below
# to ensure that the calculations are correct. 
#
# Note: for division, a check is included to identify dive by zero errors and a 
# check is also included to check for tan 90 and 270 erros.

#Import unit test functionality.

import unittest

# Import calculation algorithms from the Calculator_List Class in calculator_lists.py

# Set up test data in two lists

x=[1,2,270,4]
y=[5,6,0,8]

# Import functions from the calculator_list program

from calculator_list import Calculator_List

class TestCalculatorList(unittest.TestCase):   # test the calculator functionality

                 
    def setUp(self):
        self.calc = Calculator_List()
    

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(x,y)
        self.assertEqual([6,8,270,12], result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(x, y)
        self.assertEqual([-4, -4, 270, -4], result)

    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(x,y)
        self.assertEqual([5, 12, 0, 32], result)

    def test_calculator_divide_method_returns_correct_result(self):
        divide_by_zero_error_check = "false"    # Initialise Error Check Variable.
        for i in y:
            if i == 0:              # Test to see if element in "y" list is zero.
                divide_by_zero_error_check = "true"

        # Only execute the division test calculations below if divide by zero erro is false, i.e. no zeror in list.

        if divide_by_zero_error_check == "true":
            print "\n***** Divide by zero error as one of the list of values in 'y'is zero. *****\n"
        else:
            result = self.calc.divide(x,y)
            self.assertEqual("error", result)

    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent(x,y)
        self.assertEqual([1, 64, 1, 65536], result)

    def test_calculator_square_root_method_returns_correct_result(self):
        result = self.calc.square_root(x)
        self.assertEqual([1.0, 1.41, 16.43, 2.0], result)
        
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(x)
        self.assertEqual([1, 4, 72900, 16], result)

    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube(x)
        self.assertEqual([1, 8, 19683000, 64], result)

    def test_calculator_sin_method_returns_correct_result(self):
        result = self.calc.sin(x)
        self.assertEqual([0.0175, 0.0349, -1.0, 0.0698], result)

    def test_calculator_cos_method_returns_correct_result(self):
        result = self.calc.cos(x)
        self.assertEqual([0.9998, 0.9994, 0.0, 0.9976], result)

    # Test data before running Tan calculations to ensure no error conditions arise.

    def test_calculator_tan_method_returns_correct_result(self):
        tan_error_check = "false"       # Initialise Tan error check variable.

        for i in x:
            if i % 90 == 0:         # Test to see if x is an integer multiple of 90.
                if i % 180 != 0:    # If yes, test to see if x is not an integer multiple of 180. if not, it must be 90 or 270 or multiples of these. 
                    tan_error_check = "true"

        # Only execute the tan calculations below if Tan error check is false, i.e. not 90, 270 or multiple of those values.

        if tan_error_check == "true":
            print "***** Tan error as one of the list of values is a multiple of 90 or 270. *****"
        else:
            result = self.calc.tan(x)
            self.assertEqual("Error", result)

if __name__ == '__main__':
    unittest.main()