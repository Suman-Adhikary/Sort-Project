from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen() 
screen.setup(width = 900, height = 900) 
screen.bgcolor('black')
screen.title("THE SNAKE GAME")
screen.tracer(0)

## Add line.
Tk = Turtle()
Tk = Turtle()
Tk.hideturtle()
Tk.shapesize(stretch_len=0.5, stretch_wid=0.5)
Tk.color('white')
Tk.penup()
Tk.goto(-450, 390)
Tk.pendown()
Tk.fd(890)

snake = Snake()
food = Food()
Score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

condition_check = True

while condition_check:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        Score.increase_score()
    if snake.snake_list[0].xcor() > 440 or snake.snake_list[0].xcor() < -450 or snake.snake_list[0].ycor() > 390 or snake.snake_list[0].ycor() < -440:
        condition_check = False
        Score.game_over()

    for snake_head in snake.snake_list[1:]:
        if snake.snake_list[0].distance(snake_head) < 10: 
            condition_check = False
            Score.game_over()

screen.exitonclick()