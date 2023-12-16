def myfunc(x, y = 10, z = 0):
    print(f"x = {x}, y = {y}, z = {z}")
    x = 5
    y = 6
    z = 8
    myfunc(x, y, z)
    myfunc(x, y)
    myfunc(x)
