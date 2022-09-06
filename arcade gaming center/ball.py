from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.setposition(position)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y
        new_x = self.xcor() + self.x
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
        self.move_speed *= 0.8

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.8

    def refresh(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        time.sleep(1)
