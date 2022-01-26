# Import necessary modules
import random

# Make a random list
number = int(input("Please enter your number:"))
firstNumber = int(input("Please enter the begining number: "))
lastNumber = int(input("Please enter the last number: "))
myList = random.sample(range(firstNumber, lastNumber), number)
print(myList)

# Define a function to sort a list
def SortedList(x, y):
    for counter in range(0, y):
        mainNumber = x[counter]
        for counter2 in range(counter+1, y):
            secondNumber = x[counter2]
            if secondNumber < mainNumber:
                x[counter] = secondNumber
                x[counter2] = mainNumber
                mainNumber = secondNumber
                
    print(x)

# All parts together 
SortedList(myList, number)
        

        
