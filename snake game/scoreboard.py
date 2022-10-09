from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super(). __init__()
        self.score = 0
        self.highscore = 0
        self.color('white')
        self.penup()
        self.goto(0, 400)
        self.hideturtle()
        self.updat_score()

    def updat_score(self):
        self.clear()
        self.write(f"SCORE : {self.score}", align = "center", font = ("Courier", 24, "normal"))

    def increase_score(self): 
        self.score += 1
        self.clear()
        self.updat_score()    
    
    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font = ("Courier", 42, "normal"))