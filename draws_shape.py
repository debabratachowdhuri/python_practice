import turtle


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for j in range(1,37):
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
        brad.right(5)
    draw_circle()
    window.exitonclick()

draw_square()
