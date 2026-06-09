import turtle
import random
import color


class Food(turtle.Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.color(color.get_random_color())        

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)