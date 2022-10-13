from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
from tkinter import *
import time

window = Tk()
window.title("USER DETAILS")

canvas = Canvas(width=790, height=580)
Img = PhotoImage(file='pong.gif')
canvas.create_image(400, 300, image = Img)
canvas.pack()

game_name = Label(text='PING PONG', font = ('courier', 40, 'bold'))
game_name.place(x=250, y=5)

l_player = Label(text=' PLAYER 1 ', fg='white', bg='black', borderwidth=0, font=('cascadia code', 12, 'normal'))
l_player.place(x = 20, y = 430) 
r_player = Label(text=' PLAYER 2 ', fg='white', bg='black', borderwidth=0, font=('cascadia code', 12, 'normal'))
r_player.place(x = 20, y = 500)
l_entry = Entry(width=20, bg='#002E94', fg='white', borderwidth=0, font=('cascadia code', 12, 'normal'))
l_entry.place(x=120, y = 430)
r_entry = Entry(width=20, bg='#002E94', fg='white', borderwidth=0, font=('cascadia code', 12, 'normal'))
r_entry.place(x = 120, y = 500)  

def Start_Game():
    
    Score = ScoreBoard(l_entry.get(), r_entry.get())

    screen = Screen()
    screen.bgcolor("#bde0fe")
    screen.setup(width = 800, height = 600)
    screen.title('PING PONG')
    screen.tracer(0)

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

        if game_ball.ycor() > 280:
            game_ball.y_bounce()

        if game_ball.ycor() < -280:
            game_ball.y_bounce()   

        if game_ball.distance(r_paddle) < 40 and game_ball.xcor() > 340:
            game_ball.x_bounce() 
            Score.r_point()

        if game_ball.distance(l_paddle) < 40 and game_ball.xcor() < -340:
            game_ball.x_bounce()    
            Score.l_point()

        if game_ball.xcor() > 380:
            game_ball.reset_pos()
            Score.end_game()
            game_is_on = False
            
        if game_ball.xcor() < -380:
            game_ball.reset_pos() 
            Score.end_game()
            game_is_on = False
    screen.exitonclick()

button = Button(text='Enter', relief=RAISED, font=('jetbrains mono', 12, 'normal'), command=Start_Game)
button.place(x=600, y=460)
window.mainloop()
