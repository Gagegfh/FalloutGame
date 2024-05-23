# My first Python project: a calculator


# Defining the user's global answer

globalAnswer = 0


#Defining the function to do the first calculation using 2 numbers

def startCalculator():
    global globalAnswer
    print("Welcome to the Python Calculator!")
    print("Please note, in its current form, the Python calculator can only handle whole numbers. (no decimal numbers)")
    print("This applys to user inputs. If the answer calculated becomes a decimal, it will work fine.")
    print(" ")
    print("Please select an operation -")
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Multiply")
    print("4 = Divide")
    print("5 = Exit the calculator")
    print(" ")
    select = int(input("Which operation would you like to use?"))
    if select == 1:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter the number you would like to add to " + str(num_1)))
        answer = num_1 + num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " + " + str(num_2) + " = " + str(answer))
    elif select == 2:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter the number you would like to subtract from " + str(num_1)))
        answer = num_1 - num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " - " + str(num_2) + " = " + str(answer))
    elif select == 3:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter the number you would like to multiply by " + str(num_1)))
        answer = num_1 * num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " x " + str(num_2) + " = " + str(answer))
    elif select == 4:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter the number you would like to divide by " + str(num_1)))
        answer = num_1 / num_2
        globalAnswer = answer
        print(" ")
        print(str(num_1) + " / " + str(num_2) + " = " + str(answer))
    elif select == 5:
        raise ValueError("You have chosen to exit the calculator. Goodbye!")
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
    print("5 = Exit the calculator")
    print(" ")
    select = int(input("Which operation would you like to use?"))
    if select == 1:
        num1 = int(input("Enter the number you would like to add to " + str(globalAnswer) + ":"))
        answer = globalAnswer + num1
        print(" ")
        print(str(globalAnswer) + " + " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 2:
        num1 = int(input("Enter the number you would like to subtract from " + str(globalAnswer) + ":"))
        answer = globalAnswer - num1
        print(" ")
        print(str(globalAnswer) + " - " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 3:
        num1 = int(input("Enter the number you would like to multiply by " + str(globalAnswer) + ":"))
        answer = globalAnswer * num1
        print(" ")
        print(str(globalAnswer) + " x " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 4:
        num1 = int(input("Enter the number you would like to divide by " + str(globalAnswer) + ":"))
        answer = globalAnswer / num1
        print(" ")
        print(str(globalAnswer) + " / " + str(num1) + " = " + str(answer))
        globalAnswer = answer
    elif select == 5:
        raise ValueError("You have chosen to exit the calculator. Goodbye!")
    else:
        print(" ")
        print("Human, please note that " + str(select) + " is not a valid choice.")
        print(" ")
        additionalCalculations()


#Running the calculator

startCalculator()

while True:
    additionalCalculations()
    