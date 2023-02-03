from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.goto(-80, 200)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align="left", font=("courier", 50, "normal"))
        self.goto(-340, 205)
        self.write("score", align="left", font=("courier", 50, "normal"))
    def l_point(self):
        self.l_score+= 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score+= 1
        self.clear()
        self.update_score()

    def winner_left(self):
        self.goto(-300,0)
        self.color("green")
        self.write("Left player has won the game", align="left", font=("courier", 30, "normal"))

    def winner_right(self):
        self.goto(-300, 0)
        self.color("green")
        self.write("Right player has won the game", align="left", font=("courier", 30, "normal"))