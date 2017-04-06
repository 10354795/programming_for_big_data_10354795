# Thomas O'Brien ID 10354795
# This program tests the funtions that are created in a program Class called CarFleet in rental.py
# It tests the functions by comparint the results obtained to a set of expected results for each operation.
# It also prints error messages to the console where you try to rent more cars than available
# or return more cars than was originally available.

import unittest

from rental import *

# test the rental functionality

class TestRental(unittest.TestCase):

# Test Diesel car variables and the rent & return functions.
        
    def test_Diesel_Variables(self):
        self.Diesel = CarFleet()
        print ('\n***** Diesel car testing - console error messages here *****')
# Test variable initialisation. 
# Set stock to 4 to ensure that initial stock is correct in case the stock in the init variables are changed in rental.py.      
        self.Diesel.setDieselAvailable(4)
        self.assertEqual(4, self.Diesel.getNumDieselAvailable())
        self.assertEqual(4, self.Diesel.getMaxDieselAvailable())
# Use Setter to set new count to 10 and test results
        self.Diesel.setDieselAvailable(10)
        self.assertEqual(10, self.Diesel.getNumDieselAvailable())
# Test rental function to rent two cars. Remaining stock should reduce from 10 be 8.
        self.Diesel.rentDieselCar(2)
        self.assertEqual(8, self.Diesel.getNumDieselAvailable())
# Test return function to return 1 car. Remaining stoct should increase from 8 to 9        
        self.Diesel.returnDieselCar(1)
        self.assertEqual(9, self.Diesel.getNumDieselAvailable())
# Test rental function to ensure that you cannot rent more than 9 available.
# Trying to rent 10 should give an error message in the console.
        self.Diesel.rentDieselCar(10)
        self.assertEqual(9, self.Diesel.getNumDieselAvailable())
# Test rental function to ensure that you cannot rent cars if 0 in stock.
# Trying to rent 10 should give an error message in the console.
        self.Diesel.setDieselAvailable(0)
        self.Diesel.rentDieselCar(5)
        self.assertEqual(0, self.Diesel.getNumDieselAvailable())
# Test rental function to ensure that you cannot return more cars than was originally in stock.
# Trying to return 5 should give an error message in the console.
        self.Diesel.setDieselAvailable(0)
        self.Diesel.returnDieselCar(5)
        self.assertEqual(0, self.Diesel.getNumDieselAvailable())
# Test to see that the profit and count variables are incremented when vehicles are rented.
# Set the stock to 10. Rent 2 cars and profit should be 40.
        self.Diesel.setDieselAvailable(10)
        self.assertEqual(40, self.Diesel.getProfit())        
        self.assertEqual(2, self.Diesel.getCount()) 
# Test to see that the total available cars calculates correctly when stock vales are set for each car type.
# Set the stock to 10 for each car type.  The total available should be 40.
# Note: This test is just performed once as no need to repeat for each car type below.
        self.Diesel.setElectricAvailable(10)
        self.Diesel.setHybridAvailable(10)
        self.Diesel.setPetrolAvailable(10)        
        self.Diesel.setDieselAvailable(10)
        self.assertEqual(40, self.Diesel.getTotalAvaliable())        

    
    
# Test Electric car variables and rental & return functions
    
    def test_Electric_Variables(self):
        self.Electric = CarFleet()
        print ('\n**** Electric car testing - console error messages there *****')
# Test variable initialisation. 
# Set stock to 4 to ensure that initial stock is correct in case the stock in the init variables are changed in rental.py.      
        self.Electric.setElectricAvailable(4)
        self.assertEqual(4, self.Electric.getNumElectricAvailable())
        self.assertEqual(4, self.Electric.getMaxElectricAvailable())
# Use Setter to set new count to 10 and test results
        self.Electric.setElectricAvailable(10)
        self.assertEqual(10, self.Electric.getNumElectricAvailable())
# Test rental function to rent two cars. Remaining stock should reduce from 10 be 8.
        self.Electric.rentElectricCar(2)
        self.assertEqual(8, self.Electric.getNumElectricAvailable())
# Test return function to return 1 car. Remaining stoct should increase from 8 to 9        
        self.Electric.returnElectricCar(1)
        self.assertEqual(9, self.Electric.getNumElectricAvailable())
# Test rental function to ensure that you cannot rent more than 9 available.
# Trying to rent 10 should give an error message in the console.
        self.Electric.rentElectricCar(10)
        self.assertEqual(9, self.Electric.getNumElectricAvailable())
# Test rental function to ensure that you cannot rent cars if 0 in stock.
# Trying to rent 10 should give an error message in the console.
        self.Electric.setElectricAvailable(0)
        self.Electric.rentElectricCar(5)
        self.assertEqual(0, self.Electric.getNumElectricAvailable())
# Test rental function to ensure that you cannot return more cars than was originally in stock.
# Trying to return 5 should give an error message in the console.
        self.Electric.setElectricAvailable(0)
        self.Electric.returnElectricCar(5)
        self.assertEqual(0, self.Electric.getNumElectricAvailable())
# Test to see that the profit and count variables are incremented when vehicles are rented.
# Set the stock to 10. Rent 2 cars and profit should be 40.
        self.Electric.setElectricAvailable(10)
        self.assertEqual(40, self.Electric.getProfit())        
        self.assertEqual(2, self.Electric.getCount())


# Test Hybrid car variables and the rent & return functions.
        
    def test_Hybrid_Variables(self):
        self.Hybrid = CarFleet()
        print ('\n**** Hybrid car testing - console error messages here *****')        
# Test variable initialisation. 
# Set stock to 4 to ensure that initial stock is correct in case the stock in the init variables are changed in rental.py.      
        self.Hybrid.setHybridAvailable(4)
        self.assertEqual(4, self.Hybrid.getNumHybridAvailable())
        self.assertEqual(4, self.Hybrid.getMaxHybridAvailable())
# Use Setter to set new count to 10 and test results
        self.Hybrid.setHybridAvailable(10)
        self.assertEqual(10, self.Hybrid.getNumHybridAvailable())
# Test rental function to rent two cars. Remaining stock should reduce from 10 be 8.
        self.Hybrid.rentHybridCar(2)
        self.assertEqual(8, self.Hybrid.getNumHybridAvailable())
# Test return function to return 1 car. Remaining stoct should increase from 8 to 9        
        self.Hybrid.returnHybridCar(1)
        self.assertEqual(9, self.Hybrid.getNumHybridAvailable())
# Test rental function to ensure that you cannot rent more than 9 available.
# Trying to rent 10 should give an error message in the console.
        self.Hybrid.rentHybridCar(10)
        self.assertEqual(9, self.Hybrid.getNumHybridAvailable())
# Test rental function to ensure that you cannot rent cars if 0 in stock.
# Trying to rent 10 should give an error message in the console.
        self.Hybrid.setHybridAvailable(0)
        self.Hybrid.rentHybridCar(5)
        self.assertEqual(0, self.Hybrid.getNumHybridAvailable())
# Test rental function to ensure that you cannot return more cars than was originally in stock.
# Trying to return 5 should give an error message in the console.
        self.Hybrid.setHybridAvailable(0)
        self.Hybrid.returnHybridCar(5)
        self.assertEqual(0, self.Hybrid.getNumHybridAvailable())
# Test to see that the profit and count variables are incremented when vehicles are rented.
# Set the stock to 10. Rent 2 cars and profit should be 40.
        self.Hybrid.setHybridAvailable(10)
        self.assertEqual(40, self.Hybrid.getProfit())        
        self.assertEqual(2, self.Hybrid.getCount())


# Test Petrol car variables and the rent & return functions.
        
    def test_Petrol_Variables(self):
        self.Petrol = CarFleet()
        print ('\n**** Petrol car testing - console error messages here *****')
# Test variable initialisation. 
# Set stock to 4 to ensure that initial stock is correct in case the stock in the init variables are changed in rental.py.      
        self.Petrol.setPetrolAvailable(4)
        self.assertEqual(4, self.Petrol.getNumPetrolAvailable())
        self.assertEqual(4, self.Petrol.getMaxPetrolAvailable())
# Use Setter to set new count to 10 and test results
        self.Petrol.setPetrolAvailable(10)
        self.assertEqual(10, self.Petrol.getNumPetrolAvailable())
# Test rental function to rent two cars. Remaining stock should reduce from 10 be 8.
        self.Petrol.rentPetrolCar(2)
        self.assertEqual(8, self.Petrol.getNumPetrolAvailable())
# Test return function to return 1 car. Remaining stoct should increase from 8 to 9        
        self.Petrol.returnPetrolCar(1)
        self.assertEqual(9, self.Petrol.getNumPetrolAvailable())
# Test rental function to ensure that you cannot rent more than 9 available.
# Trying to rent 10 should give an error message in the console.
        self.Petrol.rentPetrolCar(10)
        self.assertEqual(9, self.Petrol.getNumPetrolAvailable())
# Test rental function to ensure that you cannot rent cars if 0 in stock.
# Trying to rent 10 should give an error message in the console.
        self.Petrol.setPetrolAvailable(0)
        self.Petrol.rentPetrolCar(5)
        self.assertEqual(0, self.Petrol.getNumPetrolAvailable())
# Test rental function to ensure that you cannot return more cars than was originally in stock.
# Trying to return 5 should give an error message in the console.
        self.Petrol.setPetrolAvailable(0)
        self.Petrol.returnPetrolCar(5)
        self.assertEqual(0, self.Petrol.getNumPetrolAvailable())
# Test to see that the profit and count variables are incremented when vehicles are rented.
# Set the stock to 10. Rent 2 cars and profit should be 40.
        self.Petrol.setPetrolAvailable(10)
        self.assertEqual(40, self.Petrol.getProfit())        
        self.assertEqual(2, self.Petrol.getCount())        

         

        
if __name__ == '__main__':
    unittest.main()        


        
