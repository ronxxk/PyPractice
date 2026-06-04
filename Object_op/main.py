import turtle

joe = turtle.Turtle()
print(joe)
joe.shape("turtle")

my_screen = turtle.Screen()
print(my_screen.canvheight)

on = True



while on:

    joe.forward(1)
    inpu = input("press A/D to turn")

    if inpu == "a":
        joe.right(90)
    elif inpu == "d":
        joe.left(90)
    elif inpu == "off":
        on = False
my_screen.exitonclick()