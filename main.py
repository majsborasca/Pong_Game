from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle1.go_up, key="Up")
screen.onkey(fun=paddle1.go_down, key="Down")
screen.onkey(fun=paddle2.go_up, key="w")
screen.onkey(fun=paddle2.go_down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.b_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.increase_score(2)

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.increase_score(1)

screen.exitonclick()
