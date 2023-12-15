Terminate = False
while not Terminate:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter b number: "))

    while True:
        operation = input("Enter add / sub or quit for exit: ")
        if operation == "quit":
            Terminate = True
            break
        if operation not in ["add", "sub", "quit"]:
            print("Invalid")
        if operation == "add":
            print("Add result: ", num1 + num2)
            break
        if operation == "sub":
            print("Sub result: ", num1 - num2)
            break