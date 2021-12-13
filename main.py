from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

RIGHT = 350
LEFT = -350

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
game_points = screen.numinput("Game Points", "How many points will you play to? Give me anumber: ", 7, minval=1, maxval=20)
screen.tracer(0)

right_paddle = Paddle(x_position=RIGHT)
left_paddle = Paddle(x_position=LEFT)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()
    if ball.xcor() >= 335 and ball.distance(right_paddle) <= 50:
        ball.volley()
    if ball.xcor() <= -335 and ball.distance(left_paddle) <= 50:
        ball.volley()
    if ball.xcor() >= 360:
        scoreboard.add_l_score()
        ball.refresh()
    if ball.xcor() <= -360:
        scoreboard.add_r_score()
        ball.refresh()
    if scoreboard.l_score == game_points or scoreboard.r_score == game_points:
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()
