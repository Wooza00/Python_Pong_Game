import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()
score = Score()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

speed = 0.1
game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(speed)

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        speed -= 0.005

    elif ball.xcor() > 350:
        score.l_point()
        time.sleep(2)
        ball.reset_pos()
        speed = 0.1

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.005

    elif ball.xcor() < -350:
        score.r_point()
        time.sleep(2)
        ball.reset_pos()
        speed = 0.1

screen.exitonclick()
