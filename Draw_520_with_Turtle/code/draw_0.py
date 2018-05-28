"""绘制图案0"""
from turtle import *


def draw():
    # 2移动到0的起点
    penup()
    backward(110)
    right(90)
    forward(10)
    pendown()
    right(90)

    # 绘制0
    pencolor("#ea4335")
    pensize(20)
    begin_fill()
    forward(60)
    left(90)
    forward(120)
    left(90)
    forward(60)
    left(90)
    forward(120)


if __name__ == "__main__":
    draw()
