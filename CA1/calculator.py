# Thomas O'Brien ID 10354795
# Calculator UI program

# this program sets up a Class called Calculator that can be called from other programs to run calculations.
# The algroithm for each type of calculation is defined as a function that can be called from other programs.

# The maths function is imported to program so that itcan be used as required.
#
# Note: For division, an additional check is included to identify divide by zero errors.
# Note: For Tan an additional check is included to identify errors.

import math

class Calculator(object):
 
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
    
    def multiply(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError

    def divide(self, x, y):
        number_types = (int, long, float, complex)
#
# Note: for division, include divide by zero check to avoid errors.
#
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y != 0:
                return x / y
            else:
                print '\n\n***** divide by zero error *****'
        else:
            raise ValueError 


    def exponent(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError

    def square_root(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.sqrt(x)
        else:
            raise ValueError
            
    def square(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x * x
        else:
            raise ValueError
      
    def cube(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x * x * x
        else:
            raise ValueError
            
    def sin(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.sin(x)
        else:
            raise ValueError
            
    def cos(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.cos(x)
        else:
            raise ValueError      
#
# Note: for the Tan function you have to guard against errors as 90 and 270 would return an error.
# Use the modulus calculation (%) to exclude 90, 270 and multiple of those numbers except 0 and 180.
# You also need to convert numbers entered  to Radians first or Python will give wrong answer for Tan
#
            
    def tan(self, x):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types):
            if x % 180 == 0:
                return 0
            elif x % 90 == 0:
                return 'Error'
            else:            
                return math.tan(math.radians(x))
        else:
            raise ValueError             
