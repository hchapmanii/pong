from turtle import Turtle


class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_point = 0
        self.l_point = 0
        self.score_update()
        # self.goto(-150, 250)
        # self.write("Scoreboard : 0", True, align="center", font=('Arial', 14, 'normal'))
        # self.goto(150, 250)
        # self.write("Scoreboard : 0", True, align="center", font=('Arial', 14, 'normal'))

    def score_update(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Scoreboard : {self.l_point}", True, align="center", font=('Arial', 14, 'normal'))
        self.goto(150, 250)
        self.write(f"Scoreboard : {self.r_point}", True, align="center", font=('Arial', 14, 'normal'))

    def l_score(self):
        self.l_point += 1
        self.score_update()

    def r_score(self):
        self.r_point += 1
        self.score_update()
