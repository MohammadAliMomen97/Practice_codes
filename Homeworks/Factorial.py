# Get the number
number = int(input("Please enter the number for factorial: "))

# Define a factorial function
def Factorial(x):
    if x == 1:
        return 1
    else:
        return x * Factorial(x-1)

fac = Factorial(number)
print(fac)
