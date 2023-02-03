from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed=0.1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.speed(5)
        self.x=10
        self.y=10
    def move(self):
            newx=self.xcor()+ self.x
            newy=self.ycor()+ self.y
            self.goto(newx,newy)
    def bounce(self):
            self.y*= -1
    def paddle_colide(self):
            self.x*= -1
            self.ball_speed*=0.9
    def reset_pos(self):
        self.goto(0,0)
        self.paddle_colide()
        self.ball_speed=0.1