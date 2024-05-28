# My first Python project: a calculator

print("Welcome to the Python Calculator!")
print("In its current form, the Python calculator can handle whole numbers & decimals")
print("If a user input is anything other than a number, the program will result in an error.")


# Import needed modules

import sys


# Defining the user's global answer

globalAnswer = 0
            

#Defining the function to do the first calculation using 2 numbers

def startCalculator():
    global globalAnswer
    print(" ")
    print("Please select an operation -")
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Multiply")
    print("4 = Divide")
    print("5 = Exponent")
    print("6 = Exit the calculator")
    print(" ")
    select = int(input("Which operation would you like to use?"))
    if select == 1:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter the number you would like to add to " + str(num_1)))
        answer = num_1 + num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " + " + str(num_2) + " = " + str(answer))
    elif select == 2:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter the number you would like to subtract from " + str(num_1)))
        answer = num_1 - num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " - " + str(num_2) + " = " + str(answer))
    elif select == 3:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter the number you would like to multiply by " + str(num_1)))
        answer = num_1 * num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " x " + str(num_2) + " = " + str(answer))
    elif select == 4:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter the number you would like to divide by " + str(num_1)))
        answer = num_1 / num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " / " + str(num_2) + " = " + str(answer))
    elif select == 5:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter the number you would like to raise " + str(num_1) + " to:"))
        answer = num_1 ** num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " raised to the power of " + str(num_2) + " + " + str(answer))
    elif select == 6:
        sys.exit("You have chosen to exit the calculator. Goodbye!")
    else:
        print(" ")
        print("Human, please note that " + str(select) + " is not a valid choice.")
        print(" ")
        startCalculator()


# Defining additional calculations after the first one

def additionalCalculations():
    global globalAnswer
    print(" ")
    print ("What would you like to do with " + str(globalAnswer) + "?")
    print("Please select an operation -")
    print("1 = Add a number to " + str(globalAnswer))
    print("2 = Subtract a number from " + str(globalAnswer))
    print("3 = Multiply a number by " + str(globalAnswer))
    print("4 = Divide a number by " + str(globalAnswer))
    print("5 = Raise " + str(globalAnswer) + " to the power of a number")
    print("6 = Exit the calculator")
    print(" ")
    select = int(input("Which operation would you like to use?"))
    if select == 1:
        num1 = float(input("Enter the number you would like to add to " + str(globalAnswer) + ":"))
        answer = globalAnswer + num1
        print(" ")
        print(str(globalAnswer) + " + " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 2:
        num1 = float(input("Enter the number you would like to subtract from " + str(globalAnswer) + ":"))
        answer = globalAnswer - num1
        print(" ")
        print(str(globalAnswer) + " - " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 3:
        num1 = float(input("Enter the number you would like to multiply by " + str(globalAnswer) + ":"))
        answer = globalAnswer * num1
        print(" ")
        print(str(globalAnswer) + " x " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 4:
        num1 = float(input("Enter the number you would like to divide by " + str(globalAnswer) + ":"))
        answer = globalAnswer / num1
        print(" ")
        print(str(globalAnswer) + " / " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 5:
        num1 = float(input("Enter the number you would like to raise " + str(globalAnswer) + " to:"))
        answer = globalAnswer ** num1
        print(" ")
        print(str(globalAnswer) + " raised to the power of " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 6:
        sys.exit("You have chosen to exit the calculator. Goodbye!")
    else:
        print(" ")
        print("Human, please note that " + str(select) + " is not a valid choice.")
        print(" ")
        additionalCalculations()


#Running the calculator

startCalculator()

while True:
    additionalCalculations()
    