import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

game_player = Player()
Car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(game_player.go_up, 'Up')
screen.onkey(game_player.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Car.create_car()
    Car.car_move()

    for car in Car.all_player:
        if car.distance(game_player) < 20:
            game_is_on = False
            score.game_over()

    if game_player.is_at_end_line():
        game_player.go_to_start()  
        Car.level_increase()  
        score.increase_level()    


screen.exitonclick()