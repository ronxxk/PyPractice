FONT = ("Courier", 24, "normal")
import turtle



class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("black")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)
      
    def over(self):
        self.goto (0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        
                

    def inc_(self):
        self.score += 1
        self.clear()
        self.update()       