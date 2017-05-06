# Thomas O'Brien ID 10354795
#
# Create a Calculator program in R to accept input and provide results to user.
# 
# The program should perform the following 10 maths functions. 
# add, subtract, multiply, divide, exponent, square root, square, cube, sine, & cosine.

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

