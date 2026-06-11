import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player((0, -280))
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

car = CarManager()
score_board = Scoreboard()

game_is_on = True

lvl_multiplyer = 1

while game_is_on:
    time.sleep(0.1  * lvl_multiplyer)
    screen.update()
    car.create_car()

    car.move()
    
    for car_single in car.cars:
            
        if player.distance(car_single) < 20:
            game_is_on = False
            print("Squish! Game Over.")
            score_board.over()
        elif player.ycor() > 280:
            score_board.inc_()
            player.setposition(0, -280)
            lvl_multiplyer = 0.9
            
screen.exitonclick()
