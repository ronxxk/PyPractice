from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 220:      
            n_y = self.ycor() + 20
            self.goto(self.xcor(), n_y)
        else:
            self.goto(self.xcor(), self.ycor())
        
        
    def go_down(self): 
        if self.ycor() > -220:      
            n_y = self.ycor() - 20
            self.goto(self.xcor(), n_y)
        else:
            self.goto(self.xcor(), self.ycor())