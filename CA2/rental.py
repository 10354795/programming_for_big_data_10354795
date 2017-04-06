# Thomas O'Brien ID 10354795
# Class program for fleet manager that will be used to manage the rental of cars
# and keep a track of numbers rented and the profit earned.

# Define a class called CarFleet to capture details about cars that will be made available for rental.
# The class will include details electric, hybrid, petrol and diesel cars 

class CarFleet(object):

# Initialise the class variables and put opening stock into them
# Note that "max" variables are also initialised that will be used to ensure that 
# the UI program does not allow more cars to be returned than were originally in stock.
    
    def __init__(self):
        self.__cars = []   # set up an Array to hold cars.
        self.__numElectricAvailable = 4
        self.__maxElectricAvailable = self.__numElectricAvailable
        self.__numHybridAvailable = 8
        self.__maxHybridAvailable = self.__numHybridAvailable        
        self.__numPetrolAvailable = 20
        self.__maxPetrolAvailable = self.__numPetrolAvailable
        self.__numDieselAvailable = 8
        self.__maxDieselAvailable = self.__numDieselAvailable
# initialise variable to keep a track of the number of cars rented and the profit made
        self.__profit = 0.0
        self.__count = 0
        self.__totalAvailable = 0
# Initialise the profit that can be made per car
        self.__profit_per_car = 20.0
        
# Define getter methods to see data in private variables.

    def getProfit(self):
        return self.__profit
    
    def getCount(self):
        return self.__count
    
    def getTotalAvaliable(self):
        self.__totalAvailable = (self.__numElectricAvailable + self.__numHybridAvailable + self.__numPetrolAvailable + self.__numDieselAvailable)          
        return self.__totalAvailable
    
    def getNumElectricAvailable(self):
        return self.__numElectricAvailable
    
    def getNumHybridAvailable(self):
        return self.__numHybridAvailable    

    def getNumPetrolAvailable(self):
        return self.__numPetrolAvailable

    def getNumDieselAvailable(self):
        return self.__numDieselAvailable
    
    def getMaxElectricAvailable(self):
        return self.__maxElectricAvailable

    def getMaxHybridAvailable(self):
        return self.__maxHybridAvailable

    def getMaxPetrolAvailable(self):
        return self.__maxPetrolAvailable    

    def getMaxDieselAvailable(self):
        return self.__maxDieselAvailable

# use the following functions to reset the opening stock when called by the UI program

    def setElectricAvailable(self, numAvailable):
        self.__numElectricAvailable = numAvailable
        self.__maxElectricAvailable = self.__numElectricAvailable
        
    def setHybridAvailable(self, numAvailable):
        self.__numHybridAvailable = numAvailable
        self.__maxHybridAvailable = self.__numHybridAvailable

    def setPetrolAvailable(self, numAvailable):
        self.__numPetrolAvailable = numAvailable
        self.__maxPetrolAvailable = self.__numPetrolAvailable
        
    def setDieselAvailable(self, numAvailable):
        self.__numDieselAvailable = numAvailable 
        self.__maxDieselAvailable = self.__numDieselAvailable


        
# Define method to adjust the stock of cars when a car is rented. 
# Also calculate profit and keep a track of the number of cars rented.
# numCars is the number rented and is captured by the UI program.
# check that the number of cars rented does not deplete stock below zer0.

    def rentElectricCar(self, numCars):
        if self.__numElectricAvailable <= 0:
            print ('\nCannot rent any more Electric cars as none available. ')
        elif self.__numElectricAvailable - numCars < 0:
            print ('\nCannot rent that number of Electric cars as insufficient in stock. ')
        else:
            self.__numElectricAvailable = self.__numElectricAvailable - numCars
            self.__profit = self.__profit + (numCars * self.__profit_per_car)
            self.__count = self.__count + (numCars)            

    def rentHybridCar(self, numCars):
        if self.__numHybridAvailable <= 0:
            print ('\nCannot rent any more Hybrid cars as none available. ')
        elif self.__numHybridAvailable - numCars < 0:
            print ('\nCannot rent that number of Hybrid cars as insufficient in stock. ')
        else:
            self.__numHybridAvailable = self.__numHybridAvailable - numCars
            self.__profit = self.__profit + (numCars * self.__profit_per_car)
            self.__count = self.__count + (numCars)   
            
    def rentPetrolCar(self, numCars):
        if self.__numPetrolAvailable <= 0:
            print ('\nCannot rent any more Petrol cars as none available. ')
        elif self.__numPetrolAvailable - numCars < 0:
            print ('\nCannot rent that number of Petrol cars as insufficient in stock. ')
        else:
            self.__numPetrolAvailable = self.__numPetrolAvailable - numCars
            self.__profit = self.__profit + (numCars * self.__profit_per_car)
            self.__count = self.__count + (numCars)   

    def rentDieselCar(self, numCars):
        if self.__numDieselAvailable <= 0:
            print ('\nCannot rent any more Diesel cars as none available. ')
        elif self.__numDieselAvailable - numCars < 0:
            print ('\nCannot rent that number of Diesel cars as insufficient in stock. ')
        else:
            self.__numDieselAvailable = self.__numDieselAvailable - numCars
            self.__profit = self.__profit + (numCars * self.__profit_per_car)
            self.__count = self.__count + (numCars)   

# Define method to accept return of cars and increment the stock on hand.
# Check to ensure that the number of returns do not go above the numbers that
# were originally available.

    def returnElectricCar(self, numCars):
        if self.__numElectricAvailable + numCars > self.__maxElectricAvailable:
            print ('\nCannot return more Electric cars than was originally in stock.')
        else:
            self.__numElectricAvailable = self.__numElectricAvailable + numCars

    def returnHybridCar(self, numCars):
        if self.__numHybridAvailable + numCars > self.__maxHybridAvailable:
            print ('\nCannot return more Hybrid cars than was originally in stock.')
        else:
            self.__numHybridAvailable = self.__numHybridAvailable + numCars
        
    def returnPetrolCar(self, numCars):
        if self.__numPetrolAvailable + numCars > self.__maxPetrolAvailable:
            print ('\nCannot return more Petrol cars than was originally in stock.')
        else:
            self.__numPetrolAvailable = self.__numPetrolAvailable + numCars

    def returnDieselCar(self, numCars):
        if self.__numDieselAvailable + numCars > self.__maxDieselAvailable:
            print ('\nCannot return more Diesel cars than was originally in stock.')
        else:
            self.__numDieselAvailable = self.__numDieselAvailable + numCars
 
# The folllowing funtion prints the stock available whenever called.

    def printStock(self):
        print ('\nThe number of Electric Cars available is: ' + str(self.__numElectricAvailable))
        print ('The number of Hybrid Cars available is: ' + str(self.__numHybridAvailable))
        print ('The number of Petrol Cars available is: ' + str(self.__numPetrolAvailable))
        print ('The number of Diesel Cars available is: ' + str(self.__numDieselAvailable))
        print ('\nThe total number of Cars available is: ' + str(self.__numElectricAvailable + self.__numHybridAvailable + self.__numPetrolAvailable + self.__numDieselAvailable))        
        print('\nThe total number of cars rented so far is: ' + str(self.__count))
        print('The profit earned on these rentals so far is (Euro): ' + str(self.__profit))        
        
        


        
