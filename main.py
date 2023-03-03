from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Build Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 or ball.distance(paddle_left) < 10 or ball.distance(paddle_right) < 10:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset_position()
        scoreboard.point_left()

    if ball.xcor() < -450:
        ball.reset_position()
        scoreboard.point_right()

screen.exitonclick()
