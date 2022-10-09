from turtle import Turtle
snake_position = [(0, 0),(-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()

    def create_snake(self):
        for position in snake_position:
            self.control_snake(position)    

    def control_snake(self, position):
        snakes = Turtle('circle') 
        snakes.color('green') 
        snakes.penup() 
        snakes.goto(position)  
        self.snake_list.append(snakes)

    def reset_snake(self):
        self.snake_list.clear()
        self.create_snake()
        self.snake_list[0] = self.snake_list[0]    

    def snake_extend(self):
        self.control_snake(self.snake_list[-1].position())

    def move(self):
        for snake_pos in range(len(self.snake_list) - 1, 0, -1):
            x_position = self.snake_list[snake_pos - 1].xcor()
            y_position = self.snake_list[snake_pos - 1].ycor()
            self.snake_list[snake_pos].goto(x_position, y_position)
        self.snake_list[0].forward(20)

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)
    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN) 
    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)               