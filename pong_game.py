from turtle import*
import time
from paddle import Paddle
from ball import Ball
from scorebord_pong import Scorebord
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

rt_paddle= Paddle((350,0))
lt_paddle=Paddle((-350,0))
ball= Ball()
screen.listen()
screen.onkey(fun=rt_paddle.up, key="Up")
screen.onkey(fun=rt_paddle.down, key="Down")
screen.onkey(fun=lt_paddle.up, key="w")
screen.onkey(fun=lt_paddle.down, key="s")
game_on=True
score=Scorebord()
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(rt_paddle) <50 and ball.xcor()>330 or ball.distance(lt_paddle) <50 and ball.xcor()<-330:
        ball.paddle_colide()
    if ball.xcor()>355:
        time.sleep(0.5)
        ball.reset_pos()
        score.l_point()
        rt_paddle.goto(350, 0)
        lt_paddle.goto(-350, 0)
    if ball.xcor()<-355:
        time.sleep(0.5)
        score.r_point()
        ball.reset_pos()
        rt_paddle.goto(350, 0)
        lt_paddle.goto(-350, 0)
    if score.l_score>=5:
        score.winner_left()
        game_on=False
    if score.r_score>=5:
        score.winner_right()
        game_on=False
screen.exitonclick()