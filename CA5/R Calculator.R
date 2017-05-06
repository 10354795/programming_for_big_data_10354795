# Thomas O'Brien ID 10354795
#
# Create a Calculator program in R to accept input and provide results to user.
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

divide <- function(x, y) {
  return(x / y)
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


# Print options and ask the user to input choice

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


choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))


# Ask user to enter first number for calculation.

num1 = as.integer(readline(prompt="Enter first number: "))

# Check to see if two numbers are required to be entered for menu options 1-5 only. 
# If yes, request user to input a second numbers.
# Also alert user not to put in zero for division (menu 4)

if(choice == 4){
  num2 = as.integer(readline(prompt="Enter second number *** not zero *** as division: "))
} else if(choice <= 5){
  num2 = as.integer(readline(prompt="Enter second number: "))
}

# Put guard on to protect against divide by zero error when doing calculations.

if(choice == 4)
{
  if(num2 == 0)
  {  
    print("Divide by zero error")
  } else {
    operator <- switch(choice,"+","-","*","/","to the power of","square root","square","cube","sine","cosine","tangent")
    result <- switch(choice, add(num1, num2), 
                     subtract(num1, num2), 
                     multiply(num1, num2), 
                     divide(num1, num2), 
                     exponent(num1, num2),
                     sqr_root(num1),
                     square(num1),
                     cube(num1),
                     sine(num1),
                     cosine(num1))
    
    if(choice <= 5){
      print(paste(num1, operator, num2, "=", result))
    } else { 
      print(paste(operator, num1, "=", result))
    }
  }
} else {
  operator <- switch(choice,"+","-","*","/","to the power of","square root","square","cube","sine","cosine","tangent")
  result <- switch(choice, add(num1, num2), 
                   subtract(num1, num2), 
                   multiply(num1, num2), 
                   divide(num1, num2), 
                   exponent(num1, num2),
                   sqr_root(num1),
                   square(num1),
                   cube(num1),
                   sine(num1),
                   cosine(num1))
  
  if(choice <= 5){
    print(paste(num1, operator, num2, "=", result))
  } else { 
    print(paste(operator, num1, "=", result))
  }
}

