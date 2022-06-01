def select_op(choice):
    if choice=="+":
        return 1
    if choice=="-":
        return 2
    if choice=="*":
        return 3
    if choice=="/":
        return 4
    if choice=="^":
        return 5
    if choice=="%":
        return 6
    if choice=="$":
        return 7
    if choice=="#":
        return -1

# This function adds two numbers
def add(a,b):
    return a + b

# This function subtracts two numbers
def subtract(a, b):
    return a - b

# This function multiplies two numbers
def multiply(a, b):
    return a * b

# This function divides two numbers
def divide(a, b):
    return a / b

# This function returns power of two numbers
def power(a,b):
    return a**b

# This function returns reminder two numbers
def remainder(a,b):
    return a%b




while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
  

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    if(select_op(choice) == 7):
        continue
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()

    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if(select_op(choice) == 1):
        print(str(a)+choice+str(b)+" = " + str(add(a, b)))
    if(select_op(choice) == 2):
        print(str(a)+choice+str(b)+" = " + str(subtract(a, b)))
    if(select_op(choice) == 3):
        print(str(a)+choice+str(b)+" = " + str(multiply(a, b)))
    if(select_op(choice) == 4):
        print(str(a)+choice+str(b)+" = " + str(divide(a, b)))
    if(select_op(choice) == 5):
        print(str(a)+choice+str(b)+" = " + str(power(a, b)))
    if(select_op(choice) == 6):
        print(str(a)+choice+str(b)+" = " + str(remainder(a, b)))
    
