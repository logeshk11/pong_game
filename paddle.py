from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5, outline=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor()<260:
            newy=self.ycor()+20
            self.goto(self.xcor(), newy)

    def down(self):
        if self.ycor()> -260:
            newy=self.ycor()-20
            self.goto(self.xcor(), newy)
