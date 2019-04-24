#write our amazing TDD tests here


    # Random list of tests
        #test for the data type
        #test for addition
        #test for subtraction
        #test for division
        #test for multiplication
        # test if last result was recorded

from calculator import *

#testing has 2 minimum sections:
 # setup
 #assertions


calculator_instance = Calculator()

#test for addition
print("This is the test for addition:")
print(calculator_instance.add(10,10) == 20)
print(calculator_instance.add(100,1) == 101)
print(type(calculator_instance.add(1,1)) == int)

#test for subtraction
print("This is the test for subtraction:")
print(calculator_instance.subtract(10,10) == 0)
print(calculator_instance.subtract(100,1) == 99)
print(type(calculator_instance.subtract(1,1)) == int)

#test for division
print("This is the test for division:")
print(calculator_instance.divide(10,10) == 1)
print(calculator_instance.divide(100,1) == 100)
print(type(calculator_instance.divide(1,1)) == int or calculator_instance.divide(1,1)== float)

#test for multiplication
print("This is the test for multiplication:")
print(calculator_instance.multiply(10,10) == 100)
print(type(calculator_instance.multiply(1,1)) == int)
print(calculator_instance.multiply(100,1) == 100)


#test if the last result was recorded
print("This is the test to see if the last result is 100:")
print(calculator_instance.last_result == 100)
