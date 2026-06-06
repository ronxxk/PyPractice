import turtle
import random

jimmy = turtle.Turtle()
jimmy.shape("turtle")
jimmy.pensize(10)
jimmy.speed("fastest")

def rand_color():
    x = random.random()
    y = random.random()
    z = random.random()
    return x, y, z
    
    
for i in range(3, 6):
    right_ = 360/i

    jimmy.color(rand_color())
    for u in range(i):
        jimmy.forward(100)
        jimmy.right(right_)

angle = [0 , 90, 180, 270]

for i in range(500):
    
    steps = int(random.random() * 100)

    jimmy.color(rand_color())
    
    jimmy.setheading(random.choice(angle))
    jimmy.fd(steps)
    
turtle.exitonclick()