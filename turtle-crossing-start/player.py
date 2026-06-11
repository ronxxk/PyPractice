STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.penup()
        self.goto(position)
        
    def move(self):
        self.fd(10)