import turtle


def drawFlower():
    pointer = turtle.Turtle()

    for i in range(1,37):
        for j in range(1,5):
            pointer.forward(100)
            pointer.right(90)
        pointer.right(10)
    pointer.exitonclick()

drawFlower()