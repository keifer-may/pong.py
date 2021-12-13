from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    def print_score(self):
        self.reset()
        self.penup()
        self.color("white")
        self.ht()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align="center", font=("Courier", 60, "normal"))

    def add_l_score(self):
        self.l_score += 1
        self.print_score()

    def add_r_score(self):
        self.r_score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=(f"GAME OVER"), move= False, align ="center", font=("Courier", 60, "normal"))