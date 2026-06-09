import turtle
import time
import snake
import food
import color
import scoreboard

screen = turtle.Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake_= snake.Snake()
food_ = food.Food()
scoreboard_ = scoreboard.scores()

screen.listen()
screen.onkey(snake_.up, "Up")
screen.onkey(snake_.down, "Down")
screen.onkey(snake_.lft, "Left")
screen.onkey(snake_.rgt, "Right")



on = True


while on:
    screen.update()
    time.sleep(0.18)

    snake_.move()

    if snake_.seg[0].distance(food_) < 15:
        print("nom nom nom")
        food_.refresh()
        snake_.extend()
        scoreboard_.inc_()
    #Detect collision with wall.
    if snake_.seg[0].xcor() > 280 or snake_.seg[0].xcor() < - 280 or snake_.seg[0].ycor() > 280 or snake_.seg[0].ycor() < - 280:
        on = False
        scoreboard_.over()
        
    for segment in snake_.seg:
        if segment == snake_.seg[0]:
            pass
        elif snake_.seg[0].distance (segment) < 10:
            on = False
            scoreboard_.over()
            

screen.exitonclick()