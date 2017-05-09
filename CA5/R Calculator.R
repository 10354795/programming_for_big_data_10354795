# Thomas O'Brien ID 10354795
#
# Create a Calculator program with user interface in R to accept input and provide results to user.
# 
# The program should perform the following functions 
# add, subtract, multiply, divide, exponent, square root, square, cube, sine, cosine, tangent

# Define function to do calculations

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

# Put guard on to protect against divide by zero error when doing calculations.

divide <- function(x, y) {
  if (y == 0) {
    return ("Error")
  } else {
    return(x / y)
  }
}

exponent <- function(x, y) {
  return(x ** y)
}

sqr_root <- function(x) {
  return(sqrt(x))
}

square <- function(x) {
  return(x*x)
}

cube <- function(x) {
  return(x*x*x)
}

# Note: We need to convert degrees to radians before calculating angular values with R.
# multiply angular values by pi/180 to convert to radions.


sine <- function(x) {
  return(sin(x*(pi/180)))  
}

cosine <- function(x) {
  return(cos(x*(pi/180)))
}

# Put guard on to protect against Tan errors for 90, 270 etc...

tangent <- function(x) {
  if (x %% 180 == 0){
    return (0)
  } else if (x %% 90 == 0) {
    return ("Error")
  } else {
  return(tan(x*(pi/180)))
  }
}

# Print options and ask the user to input their choice of calculations.

print("Please select the funtion you wish to perform.")
print(" 1.Add")
print(" 2.Subtract")
print(" 3.Multiply")
print(" 4.Divide")
print(" 5.Exponent")
print(" 6.Sqr_Root")
print(" 7.Square")
print(" 8.Cube")
print(" 9.Sine")
print("10.Cosine")
print("11.Tangent")

# Capture choice.

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10/11]: "))


# Ask user to enter first number for calculation.

num1 = as.numeric(readline(prompt="Enter first number: "))

# Check to see if two numbers are required (for menu options 1-5 only). 
# If yes, ask user to input a second numbers.

# Also alert users not to put in zero when doing division (menu 4)

# Change number entered to numeric (float) to accommodate floating numbers.

if(choice == 4){
  num2 = as.numeric(readline(prompt="Enter second number *** not zero if doing division ***: "))
} else if(choice <= 5){
  num2 = as.numeric(readline(prompt="Enter second number: "))
}


# Set up an array to store information about the operators that will be used for calculations .

operator <- switch(choice,"+","-","*","/","to the power of","square root","square","cube","sine","cosine","tangent")

# Execute calculations

result <- switch(choice, add(num1, num2), 
                 subtract(num1, num2), 
                 multiply(num1, num2), 
                 divide(num1, num2), 
                 exponent(num1, num2),
                 sqr_root(num1),
                 square(num1),
                 cube(num1),
                 sine(num1),
                 cosine(num1),
                 tangent(num1))

# Implement a guard to protect against divide by zero and Tan errors when printing results.

if (result == "Error"){
  print("Computational error, e.g. Divide by zero  or Tan (90 or 270) error.")
} else   if(choice <= 5){
  print(paste("Answer: ", num1, operator, num2, "=", round(result, digits = 4)))
} else { 
  print(paste("Answer: ", operator, num1, "=", round(result, digits = 4)))
}

