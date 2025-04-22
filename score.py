from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0

    def player_score(self):
        self.score += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

class AiScore(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.goto(-100, 200)
        self.score_update()


    def ai_score(self):
        self.score += 1
        self.score_update()


