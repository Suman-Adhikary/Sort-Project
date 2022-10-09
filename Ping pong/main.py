from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
from tkinter import *
import time

window = Tk()
window.title("USER DETAILS")
window.minsize(width=500, height=300)
window.config(padx=80, pady=80)
l_player = Label(text='Left player : ')
l_player.grid(row=1, column=0)
r_player = Label(text='Right player : ')
r_player.grid(row=2, column=0)
l_entry = Entry(width=30)
l_entry.grid(row=1, column=1)
r_entry = Entry(width=30)
r_entry.grid(row=2, column=1)  
def Start_Game():
    
    Score = ScoreBoard(l_entry.get(), r_entry.get())

    screen = Screen()
    screen.bgcolor("#9932CC")
    # screen.bgpic("giphy.gif")
    screen.setup(width = 800, height = 600)
    screen.title('PING PONG')
    screen.tracer(0)
    # screen.tracer(8)

    l_paddle = Paddle((-380, 0))
    r_paddle = Paddle((380, 0))
    game_ball = Ball()

    screen.listen()
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')  
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')  

    game_is_on = True
    while game_is_on:
        time.sleep(game_ball.move_speed)
        screen.update()
        game_ball.move()

        if game_ball.ycor() > 280 or game_ball.ycor() < -280:
            game_ball.y_bounce()

        if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 340 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -340:
            game_ball.x_bounce() 

        if game_ball.xcor() > 380:
            game_ball.reset_pos()
            Score.l_point()
            Score.end_game()
            game_is_on = False
            
        if game_ball.xcor() < -380:
            game_ball.reset_pos() 
            Score.r_point()
            Score.end_game()
            game_is_on = False
    screen.exitonclick()

button = Button(text='Enter', command=Start_Game)
button.grid(column=1, row=3)
window.mainloop()