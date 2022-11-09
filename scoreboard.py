from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-100, y=220)
        self.write(self.l_score, align="center", font=("Blod", 50, "normal"))
        self.goto(x=100, y=220)
        self.write(self.r_score, align="center", font=("Blod", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.color("white")
        self.hideturtle()
        for i in range(16):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.penup()
        self.goto(0, 0)
        self.setheading(270)
        for i in range(16):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
