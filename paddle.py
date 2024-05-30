from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.setposition(x=x, y=y)

    def y(self):
        return self.ycor()

    def up(self):
        if self.y() < 230:
            self.sety(self.y() + 20)

    def down(self):
        if self.y() > -230:
            self.sety(self.y() - 20)
