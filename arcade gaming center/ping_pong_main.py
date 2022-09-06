from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import random

no_of_balls = int(input("enter the number of balls you want\n"))
no_of_players = int(input("enter the number of players\n"))
screen = Screen()
screen.bgcolor("purple")
screen.setup(width=800, height=600)
screen.title(" PING-PONG")
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
up_paddle = Paddle(0, 280)
down_paddle = Paddle(0, -280)
r_paddle.setheading(90)
l_paddle.setheading(90)
l_score = Scoreboard((-300, 0))
r_score = Scoreboard((300, 0))
up_score = Scoreboard((0, 220))
down_score = Scoreboard((0, -260))
game_over = Scoreboard((800, 600))
ball = []

for b in range(no_of_balls):
    new_ball = Ball((random.randint(-50, 50), random.randint(-50, 50)))
    ball.append(new_ball)

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(up_paddle.move_left, "a")
screen.onkey(up_paddle.move_right, "d")
screen.onkey(down_paddle.move_left, "Left")
screen.onkey(down_paddle.move_right, "Right")


def wall_y():
    for i in range(len(ball)):
        if ball[i].ycor() > 280 or ball[i].ycor() < -280:
            ball[i].bounce_y()


def wall_x():
    for o in range(len(ball)):
        if ball[o].xcor() > 350:
            ball[o].bounce_x()


game_on = True
while game_on:
    screen.update()

    if no_of_players == 1:
        r_paddle.auto_v()
        up_paddle.auto_h()
        down_paddle.auto_h()
        wall_y()
        wall_x()
    elif no_of_players == 2:
        up_paddle.auto_h()
        down_paddle.auto_h()
        wall_y()
    elif no_of_players == 3:
        up_paddle.auto_h()

    for n in range(len(ball)):
        ball[n].move()
        time.sleep(ball[n].move_speed)
        if ball[n].ycor() > 260 and ball[n].distance(up_paddle) < 50 or ball[n].ycor() < -260 and ball[n].distance(
                down_paddle) < 50:
            ball[n].bounce_y()
        if ball[n].xcor() > 330 and ball[n].distance(r_paddle) < 50 or ball[n].xcor() < -330 and ball[n].distance(
                l_paddle) < 50:
            ball[n].bounce_x()

        if ball[n].xcor() > 390:
            ball[n].refresh()
            r_score.add_score()
        if ball[n].xcor() < -390:
            ball[n].refresh()
            l_score.add_score()
        if ball[n].ycor() > 290:
            ball[n].refresh()
            up_score.add_score()
        if ball[n].ycor() < -290:
            ball[n].refresh()
            down_score.add_score()

        if r_score.score == 5 or l_score.score == 5 or up_score.score == 5 or down_score.score == 5:
            game_over.game_over()
            game_on = False

screen.exitonclick()
