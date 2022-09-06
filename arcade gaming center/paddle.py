from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("crimson")
        self.penup()
        self.shapesize(1, 5)
        self.goto(xcor, ycor)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def auto_v(self):
        for n in range(1):
            self.forward(20)
            if self.ycor() < -260:
                self.setheading(90)
            if self.ycor() > 260:
                self.setheading(270)

    def auto_h(self):
        for n in range(1):
            self.forward(20)
            if self.xcor() < -350:
                self.setheading(0)
            if self.xcor() > 350:
                self.setheading(180)
