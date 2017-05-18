# Thomas O'Brien ID 10354795
# Calculator UI program to execute maths functions on one or two list of data.

# Initialise two lists x & y with data that will be used in the calculations.

# The first list contains 90 which will trigger a Tan error.
# The second list contains a zero which will trigger a divide by zero error

x=[1,2,90,4]
y=[5,6,0,8]

# Import funtions from the Calculator Class that's set up in the calculator.py program.
 
from calculator_list import Calculator_List

calculation = Calculator_List()

print 'Adding x to y gives: ', calculation.add(x,y)

print 'Adding numbers using reduce gives: ', calculation.add_reduce(x,y)

print 'Subtracting y from x gives: ', calculation.subtract(x,y)    

print 'Multiplying x * y gives: ', calculation.multiply(x,y)

# Do error checking before division to avoid divide by zeror errors.

print 'Dividing x by y gives: ', calculation.divide(x,y)    

print 'Exponent of numbers in x ^ y gives: ', calculation.exponent(x,y)

print 'Square Root of numbers in x is: ', calculation.square_root(x)

print 'Square of numbers in x is: ', calculation.square(x)

print 'Cube of numbers in x is: ', calculation.cube(x)

print 'Sine of numbers in x is: ', calculation.sin(x)

print 'Cosine of numbers in x is: ', calculation.cos(x)

# Do do error pre-checking before calculating Tan and print error if any of them are factors of 90 or 270.

print "\nTan of numbers in x is: ", calculation.tan(x)