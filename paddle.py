from turtle import Turtle

Y_POS = 0
X_POS = 350
MOVEMENT = 20
SCREEN_HEIGHT = 300

class PlayerPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5 ,stretch_len=1)
        self.color('white')
        self.goto(x=X_POS, y=Y_POS)

    def up(self):
        if self.ycor() < SCREEN_HEIGHT - 70:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        if self.ycor() > -SCREEN_HEIGHT + 70:
            self.goto(x=self.xcor(), y=self.ycor() - 20)

class AiPaddle(PlayerPaddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-X_POS, y=Y_POS)

