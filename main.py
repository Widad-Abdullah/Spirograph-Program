import random
import turtle
from turtle import Turtle,Screen
from random import randint

turtle.colormode(255)
tim=Turtle()
tim.shape("arrow")
tim.speed("fastest")


def spirograph(gap):
    # angles=[0,90,180,270]
    for _ in range(int(360/gap)):
        tim.pencolor(randint(0, 255),
                     randint(0, 255),
                     randint(0, 255))
        tim.circle(100)
        tim.setheading(tim.heading()+gap)


spirograph(5)

screen=Screen()
screen.exitonclick()
