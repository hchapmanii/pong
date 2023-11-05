from turtle import Turtle

PONG_COLOR = "white"
PONG_SHAPE = "circle"
# SPEED = 10
# PONG_SPEED = [1, 3, 6, 10, 0]
# START_POSITION = [(0, 0), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (350, 260)]


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(PONG_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(PONG_COLOR)
        # self.goto(370, 220)
        # self.speed(SPEED)
        # self.test = self.update
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_pong(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def pong_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
