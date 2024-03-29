from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, left_name, right_name):
        super().__init__()
        self.left = left_name 
        self.right = right_name 
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-270, 270)
        self.write(arg = (f"{self.left}:{self.l_score}"), align = "center", font = ("courier", 20, "normal"))    
        self.goto(270, 270)
        self.write(arg = (f"{self.right}:{self.r_score}"), align = "center", font = ("courier", 20, "normal"))  

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()   

    def end_game(self):
        self.clear()
        self.update_score()
        self.goto(0,0)
        self.write(arg = "GAME OVER", align = "center", font = ("courier", 40, "normal"))