from turtle import Turtle, Screen, Terminator
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
try:
    while game_is_on:
        time.sleep(0.01)
        screen.update()
        ball.move()
        # Detect collision with  wall
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce()
        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        # Detect when paddle misses
        if ball.xcor() > 370:
            ball.goto(0,0)
            ball.bounce_x()
            scoreboard.r_score +=1
            scoreboard.update_scoreboard()
            # The game ends when a player reaches 3 points
            if scoreboard.r_score == 3 or scoreboard.l_score == 3:
                game_is_on = False
                scoreboard.game_over()
        if ball.xcor() < - 390:
            ball.goto(0,0)
            ball.bounce_x()
            scoreboard.l_score += 1
            scoreboard.update_scoreboard()
            # The game ends when a player reaches 3 points
            if scoreboard.r_score == 3 or scoreboard.l_score == 3:
                game_is_on = False
                scoreboard.game_over()
except Terminator:
    print("Fereastra a fost închisă")

screen.exitonclick()