from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1   #pentru a creste treptat viteza bilei pe masura ce avem scor mai mare - vezi linia 24

    def move(self):
        new_x = self.xcor() + self.x_move   #am dat valoarea de 10 unitati acestor 2 atribute pentru deplasare
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1    #practic atunci cand atinge marginea vrem ca bila sa o ia in sens invers
                             #astfel in loc de +10 unitati pe coordonatele y, vom avea ycor * -1 pentru a inversa valoarea si a merge in sens invers

    def bounce_x(self):
        self.x_move *= -1    #este miscarea inversa atunci cand bila atinge paddle-ul
        self.move_speed *= 0.9   #pentru a creste treptat viteza bilei pe masura ce avem scor mai mare
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 #sa o ia de la capat cu viteza initiala
        self.bounce_x()            #pentru ca ne intereseaza doar pe axa X



