# Thomas O'Brien ID 10354795
# Calculator UI program
#
# This program uses the functions that are defined in the calculator program to run calculations.
# It provides a menu to the user to selct what function they wish to run.
# It also does error checking on the inputs to protect the program from invalid data.
#
# The program will run multiple times before ending if the users wants to do a number of calculations.

x=0
y=0

# Import funtions from the Calculator Class that's set up in the calculator.py program.
 
from calculator import Calculator

calculation = Calculator()


# Create a function to ask user which calculation they wish to perform and do error checking

def menu_input ():
#
# ask user which calculation they wish to perform and do error check if operand is not valid symbol
#
    print '\nThis program calculates the result based on which function you request'
    print '\n***** Please select menu number from below list. *****\n'
    print 'Input  1 for Add'
    print 'Input  2 for Subtract'
    print 'Input  3 for Multiply'
    print 'Input  4 for Divide'
    print 'Input  5 for Exponent'
    print 'Input  6 for Square Root'
    print 'Input  7 for Square'
    print 'Input  8 for Cube'
    print 'Input  9 for Sine'
    print 'Input 10 for Cosine'
    print 'Input 11 for Tangent'
    while True:
        menu = raw_input ('Please indicate the operation you wish to perform by entering menu number here: ')
        if input == '':
            continue
        else:
            try:
                operand = int(menu)
                if operand >= 1 and operand <= 11:
                    break
                else:
                    print '\n\n***** Please enter a number in range 1 - 11 only. *****\n\n'
            except ValueError:
                print '\n\n***** Please enter a valid number in range 1 - 11 only. *****\n\n'
    return operand

#
# Create a function to accept data for calculations and do error checking.
#
def check_input ():
    while True:
        input = raw_input ('Enter number: ')
        if input == '':
            continue
        else:
            try:
                input = float (input)
                break
            except ValueError:
                print 'please enter a valid number.'
    return input


# Create a function that can be called to capture the numbers and do the calculations.
# 
# Based on the menu selction, check if one or two numbers are required to execute the calculation.
#
# Menu options 1-5 require two numbers while 6-11 only require one number to be input.
#
def do_calculations():
    if operand >= 1 and operand <=5:
    # capture first number and assign to be x
        print '\nPlease enter two numbers below.'
        input_value = check_input()
        x = float (input_value)
    # capture second number and assign to be y        
        input_value = check_input()
        y = float (input_value)
 
    elif operand >=6 and operand <=10:
    # capture one number only and assign to be x
        print 'Please enter one number below.'
        input_value = check_input()
        x = float (input_value)
    elif operand == 11:
    # capture one number only and assign to be x
        print '\nFor Tan calculations, please exclude numbers such as 90 & 270 as these result in Tan calculation errors.'
        print '\nPlease enter one number below.'
        input_value = check_input()
        x = float (input_value)

    #
    # execute the calculation using the appropriate operand from Calculator program
    #
    
    if operand is 1:
        print 'n\The result for Adding numbers is: ', calculation.add(x,y)
    elif operand is 2:
        print '\nThe result for Subtracting numbers is: ', calculation.subtract(x,y)    
    elif operand is 3:
        print '\nThe result for Multiplying numbers is: ', calculation.multiply(x,y)
#
# Note: For division, additional error checking is included to avoid divide by zero errors.
#
    elif operand is 4:
        if y != 0:
            print '\nThe result for Dividing numbers is: ', calculation.divide(x,y)
        else:
            print '\n***** divide by zero error *****'
    elif operand is 5:
        print '\nThe result for Exponent of numbers is: ', calculation.exponent(x,y)
    elif operand is 6:
        print '\nThe result for Square Root of number is: ', calculation.square_root(x)
    elif operand is 7:
        print '\nThe result for Square of number is: ', calculation.square(x)
    elif operand is 8:
        print '\nThe result for Cube of number is: ', calculation.cube(x)
    elif operand is 9:
        print '\nThe result for Sine of number is: ', calculation.sin(x)
    elif operand is 10:
        print '\nThe result for Cosine of number is: ', calculation.cos(x)
    elif operand is 11:
        print '\nThe result for Tan of number is: ', calculation.tan(x)


# The following section executes the program by calling the defined functions.
#
# It als creates a while loop to keep running the program if the user wishes to do more calculations. 
# Enter upper or lower case "y" to continue. Inputing any other character will close the program. 

while True:
    operand = menu_input() # This calls the menu function
    do_calculations()      # This calls the calculations fucntion.
#
#The following code checks to see if the user wishes to do more calculations.
#
    check = raw_input('\nDo you wish to do another calculation? Input "y" to continue, otherwise hit enter to finish. ')
    if check.lower() == 'y':
        continue
    else:
        break    

print '\n***** End of program *****'
