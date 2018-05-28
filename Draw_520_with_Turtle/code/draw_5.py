"""绘制图案5"""
from turtle import *


def draw():
    bgcolor("#fbbc05")
    penup()
    back(200)
    pendown()
    color("#4285f4", "#4285f4")
    begin_fill()
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    right(90)
    forward(60)
    right(90)
    forward(80)
    right(90)
    forward(20)
    right(90)
    forward(60)
    left(90)
    forward(20)
    left(90)
    forward(60)
    right(90)
    forward(100)
    right(90)
    forward(80)
    right(90)
    forward(20)
    end_fill()


if __name__ == "__main__":
    draw()
