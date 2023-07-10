from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.update_write()

    def update_write(self):
        self.goto(-100, 200)
        self.write(self.paddle2_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.paddle1_score, align=ALIGN, font=FONT)

    def increase_score(self, player):
        if player == 1:
            self.paddle1_score += 1
            self.clear()
            self.update_write()
        else:
            self.paddle2_score += 1
            self.clear()
            self.update_write()


