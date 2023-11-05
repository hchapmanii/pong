from turtle import Turtle, Screen
from pong import Pong
from score import Scores
from paddle import Paddle
import time

WIDTH = 800
HEIGHT = 600
COLOR = "black"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title("Pong the Game")
screen.tracer(0)

tur = Turtle()
pong = Pong()
score = Scores()
r_pad = Paddle()
l_pad = Paddle()

screen.listen()
# Right Paddle Keys
screen.onkey(r_pad.up, key="Up")
screen.onkey(r_pad.down, key="Down")

# Left Paddle Keys
screen.onkey(l_pad.up, key="a")
screen.onkey(l_pad.down, key="z")
r_pad.r_paddle()
l_pad.l_paddle()

game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move_pong()
    # print(f"{pong.ycor()} is y")
    # print(f"{pong.xcor()} is x")

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    if pong.distance(r_pad) < 50 and pong.xcor() > 320 or pong.distance(l_pad) < 50 and pong.xcor() < - 320:
        pong.bounce_x()

    if pong.xcor() > 390:
        pong.pong_reset()
        score.r_score()

    if pong.xcor() < -390:
        pong.pong_reset()
        score.l_score()


screen.exitonclick()
