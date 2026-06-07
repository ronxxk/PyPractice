import turtle
import random
from statistics import median as med

screen = turtle.Screen()
screen.setup(1000, 800)
choose = screen.textinput(title="Bet", prompt="Which turtle would you choose")

color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle_t = []


x = -460
y = -200

for i in color:
    y += 57
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.color(i)
    t.goto(x, (y))
    turtle_t.append(t)

on = False
median = []

if choose: 
    on = True
    
while on:

    
    for t in turtle_t:
        if t.xcor() > 460:
            on = False
            color_won = t.pencolor()
            print(f"The wining Turtle is {color_won}!\n")
            if color_won == choose:
                print("Your Turtle Won!\n")
            else:
                print("You lost!\n")
                
        step = random.randint(10, 40)  
        median.append(step)
        t.fd(step)



print("Median steps:", {med(median)})



screen.exitonclick()