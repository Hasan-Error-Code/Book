Terminate = False
while not Terminate:
    user = input("\n1. add \n2. sub \n3. quit \nEnter:  ")
    if user == "3":
        Terminate = False
        break
    else: 
        f_number = int(input("Enter first number: "))
        s_number = int(input("Enter second number: "))

        if user == "1":
            print(f"Some result: {f_number + s_number}")
            Terminate = True
        elif user == "2":
            print(f"Subtraciton result: {f_number - s_number}")
            Terminate = True