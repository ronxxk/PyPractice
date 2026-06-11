COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.cars = []
    
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_Car = Turtle()
            new_Car.shape("square")
            new_Car.shapesize(1, 2)
            new_Car.setheading(180)
            new_Car.color(random.choice(COLORS))
            new_Car.penup()
            yCOR = random.randint(-240, 240)
            new_Car.goto(300, yCOR)
            self.cars.append(new_Car)
            
    
    def move(self):
        for cars in self.cars:
            cars.fd(MOVE_INCREMENT)
        