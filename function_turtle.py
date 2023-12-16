import turtle
def tur(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
counter = 0
while counter > 90:
    deaw_square(side_length)
    turtle.right(4)
    counter += 1
    turtle.exitonclick()