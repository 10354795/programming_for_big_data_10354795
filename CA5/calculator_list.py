# Thomas O'Brien ID 10354795
# Calculator class program to execute maths functions on one or two list of data.

# This program sets up a Class called Calculator_List that can be called from other programs to run calculations.
# The algroithm for each type of calculation is defined as a function that can be called from other programs.

# The maths function is imported to the program so that it can be used as required.
#
# Note 1: For division, an additional check is included in the UI program to identify divide by zero errors.
# Note 2: For Tan calculations, an additional check is included to identify Tan errors in the UI program.

import math

class Calculator_List(object):
    
    # Use reduce method to add numbers within one list

    def add_reduce(self, x, y):
        return reduce(lambda a,b:a+b, x)
    
    # Use map and lambda method to do addition, subtraction, multiply divide and exponent for two lists.

    def add(self, x, y):
        return map(lambda a,b:a+b, x,y)
    
    def subtract(self, x, y):
        return map(lambda a,b:a-b, x,y)
    
    def multiply(self, x, y):
        return map(lambda a,b:a*b, x,y)

    # Note: for the division, you have to guard against errors. See error checking in UI program.

    def divide(self, x, y):
        divide_by_zero_error_check = "false"
        for i in y:
            if i == 0:              # Test to see if element in "y" list is zero.
                divide_by_zero_error_check = "true"

        # If divide by zero error condition is not found above, then execute the division calculations below.

        if divide_by_zero_error_check != "true":
            return map(lambda a,b:round(float(a)/b,4), x,y)
        else:
            return "***** Divide by zero error as one of the list of values in 'y'is zero. *****"
            
    def exponent(self, x, y):
        return map(lambda a,b:a**b, x,y)

    # Use list comprehension method for square root and squared functions below.

    def square_root(self, x):
        return [round(math.sqrt(i),2) for i in x]
            
    def square(self, x):
        return [i**2 for i in x]

    # Use map on its own and call in calculation (result) which uses lambda 
      
    def cube(self, x):
        result = lambda a : a**3
        return map(result, x)
            
    # Use map and lambda method to do sin, cos and tan calculations

    def sin(self, x):
        return map(lambda a:round(math.sin(float(a)*3.1416/180),4), x)

    def cos(self, x):
        return map(lambda a:round(math.cos(float(a)*3.1416/180),4), x)     
    
    # Note: for the Tan function you have to guard against errors. 

    # You can use filter function to filter out numbers that will cause errors in lists.

    def tan(self, x):            
        tan_error_check = "false"     # Initialise tan error check variable

        for i in x:
            if i % 90 == 0:         # Test to see if x is an integer multiple of 90.
                if i % 180 != 0:    # If yes, test to see if x is not an integer multiple of 180. if not, it must be 90 or 270 or multiples of these. 
                    tan_error_check = "true"

        # If Tan error condition false above, then execute the tan calculations below.
        # Otherwise execute the filter function to remove offending numbers from the list

        if tan_error_check != "true":
                    return map(lambda a:round(math.tan(float(a)*3.1416/180),4), x)   # Use y as new list to do Tan.
        else:
            print "***** Tan error as one of the list of values is a multiple of 90 or 270. *****"
            print "\nThe tan of remaining numbers in x (using filter method) are below:"
            z = filter(lambda a: a % 90 != 0, x)    # Filter for factors of 90 and assign numbers to new list z
            return map(lambda a:round(math.tan(float(a)*3.1416/180),4), z)   # Use new list z to do Tan.

