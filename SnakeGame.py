from turtle import Screen, Turtle
import time  
from scoreboard import Scoreboard
from Snake import Snake
from food import Food


screen = Screen()
screen.title(" SNAKE GAME ")
screen.setup(width = 600, height = 600)
screen.bgcolor("navy blue")
screen.tracer(0)

#S1 = Turtle(shape="square")
#S1.color('white')
#S1.goto(0 , 0)
#S2 = Turtle(shape="square")
#S2.color('white')
#S2.goto(-20 , 0)
#S3 = Turtle(shape="square")
#S3.color('white')
#S3.goto(-40 , 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#KEY CONTROLLING

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()  # snake movement

    #Detect collision with food
    if snake.head.distance(food) <15:
        food.new_food_location()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>300 or snake.head.xcor()< -300 or snake.head.ycor()>300 or snake.head.ycor()<-300 :
        game_is_on = False
        scoreboard.game_over()

    # detecting snake biting itself

    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on= False
            scoreboard.game_over()

screen.exitonclick()
