from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 50, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.score_update()

    def score_update(self):
        self.goto(-100, 200)
        self.write(self.score_left, False, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.score_right, False, align=ALIGN, font=FONT)

    def point_left(self):
        self.score_left += 1
        self.clear()
        self.score_update()

    def point_right(self):
        self.score_right += 1
        self.clear()
        self.score_update()


