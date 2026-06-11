import turtle
import os

data_path = os.path.join(os.path.dirname(__file__), "data.txt")

class scores(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(data_path) as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))
      
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(data_path, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
            
    def inc_(self):
        self.score += 1
        self.update()       