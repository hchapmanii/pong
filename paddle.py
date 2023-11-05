from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
R_PADDLE_X = 350
R_PADDLE_Y = 0
L_PADDLE_X = -350
L_PADDLE_Y = 0


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.paddles = [0]
        self.pad = self.paddles
        self.new_y = self.ycor()

    def r_paddle(self):
        self.goto(R_PADDLE_X, R_PADDLE_Y)
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=0)

    def l_paddle(self):
        self.goto(L_PADDLE_X, L_PADDLE_Y)
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=0)

    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
