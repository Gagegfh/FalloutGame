# My first Python project: a calculator


#Defining the function to do the first calculation using 2 numbers

def startCalculator():
    print("Please select an operation -")
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Multiply")
    print("4 = Divide")
    print(" ")
    select = int(input("Which operation would you like to use?"))
    if select == 1:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        answer = num_1 + num_2
        print(str(num_1) + " + " + str(num_2) + " = " + str(answer))
    elif select == 2:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        answer = num_1 - num_2
        print(str(num_1) + " - " + str(num_2) + " = " + str(answer))
    elif select == 3:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        answer = num_1 * num_2
        print(str(num_1) + " x " + str(num_2) + " = " + str(answer))
    elif select == 4:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        answer = num_1 / num_2
        print(str(num_1) + " / " + str(num_2) + " = " + str(answer))
    else:
        print(" ")
        print("Human, please note that " + str(select) + " is not a valid choice.")
        print(" ")
        startCalculator()


# Defining additional calculations after the first one

def additionalCalculations(answer):
    print ("What would you like to do with " + str(answer) + "?")
    print("Please select an operation -")
    print("1 = Add a number to " + str(answer))
    print("2 = Subtract a number from " + str(answer))
    print("3 = Multiply a number by " + str(answer))
    print("4 = Divide a number by " + str(answer))
    print(" ")
    select = int(input("Which operation would you like to use?"))


#Running the calculator

startCalculator()

while True:
    additionalCalculations(answer)
    