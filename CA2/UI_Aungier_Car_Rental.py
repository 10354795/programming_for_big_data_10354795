# Thomas O'Brien ID 10354795
# Car rental UI program
#
#
# This program creates a user interface to manage the rental and return of vehicles.
# It calls functions from a Class in rental.py.
#

from rental import *

# Instantiate variable for car rentalbased on CarFleet class.

car_rental = CarFleet()

# pop up a welcome message and explain what the program does when run.

print ('\n\n            Welcome to the Aungier Car Rental system.\n')
print ('This system allows you to manage the stock of vehicles available for rental.\n')
print ('It also providess functionality to manage renting and returning of cars.')

print ('\nFor your information the opening stock is as follows:-\n')


# Create a funtion to update the opening stock and validate inputs to ensure they are numeric

def enterstock():
    while True:
        stock = (raw_input('please enter number available: '))
        if input == '':
            continue
        else:
            try:
                stock = int(stock)
                if stock < 0:
                    print ('\n***** Please do not enter negative stock numbers. *****\n')
                    continue
                break
            except ValueError:
                print ('\n\n***** Please enter a valid numeric number. *****\n\n')
    return stock

# Create a function to check if the user would like to update the number of vehicles in stock.
# This funtion calls the enter stock funtion. 

def update_opening_stock_function():
    answer = raw_input('\nWould you like to change the number of vehicles available to rent (Y/N)? ')
    if answer.lower() == 'y':
        print ('\nFor electric cars')
        stock = enterstock()
        car_rental.setElectricAvailable(stock)
        print ('\nFor Hybrid cars')
        stock = enterstock()
        car_rental.setHybridAvailable(stock)
        print ('\nFor Petrol cars')
        stock = enterstock()
        car_rental.setPetrolAvailable(stock)
        print ('\nFor Diesel cars')
        stock = enterstock()
        car_rental.setDieselAvailable(stock)
        print ('\nThe updated opening stock is as follows:-\n')
        car_rental.printStock()
    else:
        print ('\nThe opening stock is OK, so we will go to the rental management section.\n')

# Create a function to manage the rental of cars.
# This calls funtions from car fleet Class in rental.py 
# It also validaes the data that's entered to ensure that it is approprite.
# It uses a "while" statement to continue usage until the user opts to end renting vehicles.

def car_rent_function():
    while True:
        if car_rental.getTotalAvaliable() <= 0:
            print ('\n\n****** Sorry, nothing available to rent. Please try again when some cars are returned. ******')
            break
        check = raw_input('\nWould you like to rent a car (Y/N)? ')
        if check.lower() == 'y':
            pick_car_type = raw_input('\nWhat type of Car would you like to rent? \nE = Electric\nH = Hybrid\nP = Petrol\nD = Diesel. \nPlease enter E, H, P or D to choose: ')
            if pick_car_type != 'E' and pick_car_type != 'H' and pick_car_type != 'P' and pick_car_type != 'D' and pick_car_type != 'e' and pick_car_type != 'h' and pick_car_type != 'p' and pick_car_type != 'd':
                print ('\nPlease only enter E, H, P, D to chose car type: ')
                continue
            rent_number = (raw_input('\nHow many cars would you like to rent? '))
            if rent_number == '':
                print ('\n***** Please enter a valid number of cars to rent. *****\n')
                continue
            else:
                try:
                    rent_number = int(rent_number)
                    if rent_number < 0:
                        print ('\n***** Please do not enter negative numbers when renting cars. *****\n')
                        continue
                except ValueError:
                    print ('\n***** Please enter a valid whole number of cars to rent. *****\n')
                    continue
            if pick_car_type.lower() == 'e':
                car_rental.rentElectricCar(rent_number)
            elif pick_car_type.lower() == 'h':
                car_rental.rentHybridCar(rent_number)
            elif pick_car_type.lower() == 'p':
                car_rental.rentPetrolCar(rent_number)
            elif pick_car_type.lower() == 'd':
                car_rental.rentDieselCar(rent_number)
            
            car_rental.printStock()
        elif check.lower() != 'n':
            print ('\n***** Please enter Y/N only *****')
            continue
        else:
            break

# Create a function to manage the return of cars.
# This calls funtions from car fleet Class in rental.py 
# It also validaes the data that's entered to ensure that it is approprite.
# It uses a "while" statement to continue usage until the user opts to end returning vehicles to stock.

def car_return_function():
    while True:
        check = raw_input('\nWould you like to return a car (Y/N)? ')
        if check.lower() == 'y':
            pick_car_type = raw_input('\nWhat type of Car would you like to return? \nE = Electric\nH = Hybrid\nP = Petrol\nD = Diesel. \nPlease enter E, H, P or D to choose: ')
            if pick_car_type != 'E' and pick_car_type != 'H' and pick_car_type != 'P' and pick_car_type != 'D' and pick_car_type != 'e' and pick_car_type != 'h' and pick_car_type != 'p' and pick_car_type != 'd':
                print ('\nPlease only enter E, H, P, D to chose car type: ')
                continue
            return_number = (raw_input('\nHow many cars would you like to return? '))
            if return_number == '':
                print ('\n***** Please enter a valid number of cars to return. *****\n')
                continue
            else:
                try:
                    return_number = int(return_number)
                    if return_number < 0:
                        print ('\n***** Please do not enter negative numbers when returning cars. *****\n')
                        continue
                except ValueError:
                    print ('\n***** Please enter a valid whole number of cars to return. *****\n')
            if pick_car_type.lower() == 'e':
                car_rental.returnElectricCar(return_number)
            elif pick_car_type.lower() == 'h':
                car_rental.returnHybridCar(return_number)
            elif pick_car_type.lower() == 'p':
                car_rental.returnPetrolCar(return_number)
            elif pick_car_type.lower() == 'd':
                car_rental.returnDieselCar(return_number)
            
            car_rental.printStock()
        elif check.lower() != 'n':
            print ('\n***** Please enter Y/N only *****')
            continue
        else:
            break

# The lines of code below call the various functions to run them.
# It uses a "while" statement to continue usage until the user opts to exit the program.

while True:
    car_rental.printStock()
    update_opening_stock_function()
    car_rent_function()
    car_return_function()
    check_continue = raw_input('\nWould you like to exit the program (Y/N)? ')
    if check_continue.lower() == 'y':
        break
    else:
        print ('\nIf you did not enter Y to exit, the program resumes.')
        continue

print ('\n\n*****You have exited the program *****')


