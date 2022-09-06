from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(pos)
        self.score_board()
        self.hideturtle()

    def score_board(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="CENTER", font=FONT)
