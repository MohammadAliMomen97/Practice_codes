def EvenMean():

    # Get the numerical interval
    begin = int(input("Please enter the first number: "))
    finish = int(input("Please enter the last number: "))

    # Seprate even numbers
    evenNumbers = []
    counter = 0
    for x in range(begin, finish):
        if x%2 == 0:
            evenNumbers.append(x)
            counter += 1
     
    # Compute the mean
    sums = 0
    for i in evenNumbers:
        sums += i
    finallNumber = sums/counter

    # Show the finall number
    print(f"The mean is {finallNumber}")

EvenMean()

