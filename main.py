from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if right paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    #detect if left paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()









screen.exitonclick()