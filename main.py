import turtle
import time
from paddle import PlayerPaddle, AiPaddle
from ball import Ball
from score import ScoreBoard, AiScore

START_SPEED = 0.1
current_speed = START_SPEED
is_on = True
screen = turtle.Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
player_paddle = PlayerPaddle()
ai_paddle = AiPaddle()
ball = Ball()
player_score_board = ScoreBoard()
player_score_board.goto(100, 200)
player_score_board.score_update()
ai_score_board = AiScore()

screen.onkeypress(player_paddle.up, 'Up')
screen.onkeypress(player_paddle.down, 'Down')
screen.onkeypress(ai_paddle.up, 'w')
screen.onkeypress(ai_paddle.down, 's')

while is_on:
    screen.update()
    time.sleep(current_speed)
    ball.move()

    #Detects if the ball makes contact with the top and bottom of the screen
    ball.bounce_y()

    #Detect if ball makes contact with paddle
    if ball.distance(player_paddle) < 60 and ball.xcor() > 320 or ball.distance(ai_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()
        current_speed *= 0.7

    #Detect if player misses the ball
    if ball.xcor() > 380:
        ai_score_board.ai_score()
        current_speed = START_SPEED
        ball.home()


    #Detect if Ai misses the ball
    if ball.xcor() < -380:
        player_score_board.player_score()
        current_speed = START_SPEED
        ball.home()



screen.exitonclick()