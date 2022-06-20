#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                              Classic Snake Game                               # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Class snake game where your tail grows as you eat food.                               #
#                                                                                       #
# Guide:                                                                                #
# cd into project folder: cd snake_game                                                 #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#########################################################################################

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall -- original ends/closes game
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()

    # Detect collision with wall -- infinite wall, can use for testing or other games
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        new_x = -(snake.head.xcor())
        new_y = snake.head.ycor()
        snake.head.goto(new_x, new_y)
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        new_x = snake.head.xcor()
        new_y = -(snake.head.ycor())
        snake.head.goto(new_x, new_y)

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
