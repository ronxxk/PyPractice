import turtle
from food import Food



class scores(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
      
    def over(self):
        self.goto (0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
        
                

    def inc_(self):
        self.score += 1
        self.clear()
        self.update()       