from turtle import Turtle, Screen
from paddles import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard, Line

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
scoreboard = Scoreboard()
ball = Ball()
line = Line()
screen.listen()
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor()<-350:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()
screen.exitonclick()
