import turtle

screen = turtle.Screen()

jeff = turtle.Turtle()

is_moving = False

def move_fd():
    jeff.forward(1)

def move_bd():
    jeff.backward(1)   

def turn_lft():
    new_head = jeff.heading() + 10
    jeff.setheading(new_head)


def turn_rgt():
    new_head = jeff.heading() - 10
    jeff.setheading(new_head)


def clear():
    jeff.clear()
    jeff.penup()
    jeff.home()
    jeff.pendown()

jeff.screen.onkey(move_fd, "w")
jeff.screen.onkey(move_bd, "s")
jeff.screen.onkey(turn_lft, "a")
jeff.screen.onkey(turn_lft, "d")
jeff.screen.onkey(clear, "c")




jeff.screen.listen()


screen.mainloop()
