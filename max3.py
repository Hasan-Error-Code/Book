number = 0
for i in range(101):
    if i % 5 == 0:
        print(i)
        number = number + i
print("Sum is: ", number)