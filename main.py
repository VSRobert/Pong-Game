from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)      #este necesar pentru a incetini "bila" in miscarea ei pe ecran
    screen.update()   #de fiecare updatam ecranul pentru ca am setat screen.tracer(0).
    #a fost necesar pentru a nu mai vedea animatia cand paddle pleaca din centru spre pozitia indicata de noi in centru dreapta
    ball.move()       #am creat o metoda in clasa ball pentru a muta bila din centru in dreapta-sus

    #Detectam limita de sus si limita de jos a ecranului cand avem coliziune cu bila
    if ball.ycor() > 275 or ball.ycor() < -275:    #extremitatile de sus si jos ale ecranului
        ball.bounce_y()

    #Detectam coliziunea cu paddle-urile
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()
        ball.bounce_y()

    #Daca evita paddle-urile, se va reseta la pozitia (0, 0), dar va pleca in directia opusa
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()








screen.exitonclick()