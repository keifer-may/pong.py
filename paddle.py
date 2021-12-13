from turtle import Turtle

MOVEDISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize( stretch_wid=5, stretch_len=1)
        self.setx(x_position)


    def up(self):
        if self.ycor() < 240:
            old_y = self.ycor()
            self.sety(old_y+20)


    def down(self):
        if self.ycor() > -240:
            old_y = self.ycor()
            self.sety(old_y-20)

