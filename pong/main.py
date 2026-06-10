from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scores
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

score_board = Scores()
        
        
screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")


on = True


while on:
    
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score_board.inc_()
            
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        score_board.inc_()
        
    elif ball.xcor() <= -420 or ball.xcor() >= 420:
        score_board.over()
        on = False


    
screen.exitonclick()