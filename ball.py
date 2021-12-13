from turtle import Turtle
import random
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        poss_directions = [10, -10]
        self.x_move = random.choice(poss_directions)
        self.y_move = random.choice(poss_directions)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def volley(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        time.sleep(0.5)
        self.x_move *= -1
        self.move()
